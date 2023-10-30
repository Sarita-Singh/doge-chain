"use strict";

const { Contract } = require("fabric-contract-api");

class MyContract extends Contract {
  constructor() {
    super("MyContract");
  }

  async AddBalance(ctx) {
    const transientMap = ctx.stub.getTransient();
    const transientBalanceJSON = transientMap.get("balance_amount");

    if (transientBalanceJSON.length === 0) {
      throw new Error("balance amount not found in the transient map");
    }

    const jsonBytesToString = String.fromCharCode(...transientBalanceJSON);
    const jsonFromString = JSON.parse(jsonBytesToString);
    if (jsonFromString.balance.length == 0) {
      throw new Error("balance field must be a non-empty string");
    }

    const clientOrg = ctx.clientIdentity.getMSPID();
    var balanceBytes = await ctx.stub.getState(clientOrg);

    let balance = 0;
    if (balanceBytes && balanceBytes.length > 0) {
      balance = parseInt(balanceBytes.toString());
    }

    balance += parseInt(jsonFromString.balance);

    await ctx.stub.putState(clientOrg, Buffer.from(balance.toString()));
  }

  async GetBalance(ctx, org) {
    var balanceBytes = await ctx.stub.getState(org);
    let balance = 0;
    if (balanceBytes && balanceBytes.length > 0) {
      balance = parseInt(balanceBytes.toString());
    } else {
      throw new Error(`Balance not found for ${organization}`);
    }

    return JSON.stringify({ org, balance });
  }

  async AddItem(ctx) {
    const transientMap = ctx.stub.getTransient();
    const transientItemJSON = transientMap.get("item_entry");

    if (transientItemJSON.length === 0) {
      throw new Error("item not found in the transient map");
    }

    const jsonBytesToString = String.fromCharCode(...transientItemJSON);
    const jsonFromString = JSON.parse(jsonBytesToString);
    if (jsonFromString.name.length == 0) {
      throw new Error("name field must be a non-empty string");
    }
    if (jsonFromString.qty.length == 0) {
      throw new Error("qty field must be a non-empty string");
    }
    if (jsonFromString.price.length == 0) {
      throw new Error("price field must be a non-empty string");
    }

    const itemName = jsonFromString.name;
    const itemNum = parseInt(jsonFromString.qty);
    const itemPrice = jsonFromString.price;
    const clientOrg = ctx.clientIdentity.getMSPID();

    const compositeKey = ctx.stub.createCompositeKey("private_collection_", [itemName]);
    const collectionName = clientOrg + "PrivateCollection";
    var itemBytes = await ctx.stub.getPrivateData(collectionName, compositeKey);
    let quantity = 0;
    if (itemBytes && itemBytes.length > 0) {
      const itemJSON = JSON.parse(itemBytes.toString());
      quantity = parseInt(itemJSON.qty);
    }
    quantity += itemNum;
    const itemEntry = {
      name: itemName,
      qty: quantity,
      price: itemPrice,
    };

    await ctx.stub.putPrivateData(collectionName, compositeKey, Buffer.from(JSON.stringify(itemEntry)));
  }

  async GetItem(ctx) {
    const clientOrg = ctx.clientIdentity.getMSPID();
    const collectionName = clientOrg + "PrivateCollection";
    const partialKey = "private_collection_";
    var iterator = ctx.stub.getPrivateDataByPartialCompositeKey(collectionName, partialKey, []);
    const inventory = [];
    for await (const queryResult of iterator) {
      const resBytesToString = String.fromCharCode(...queryResult.value);
      const jsonFromString = JSON.parse(resBytesToString);
      inventory.push({
        name: jsonFromString.name,
        qty: jsonFromString.qty,
        price: jsonFromString.price,
      });
    }
    return JSON.stringify(inventory);
  }

  async AddToMarket(ctx, item, price) {
    const clientOrg = ctx.clientIdentity.getMSPID();
    const compositeKey = ctx.stub.createCompositeKey("private_collection_", [item]);
    const collectionName = clientOrg + "PrivateCollection";
    var itemBytes = await ctx.stub.getPrivateData(collectionName, compositeKey);

    if (!itemBytes || itemBytes.length === 0) {
      throw new Error(`Item '${item}' not found in the inventory.`);
    }
    const itemJSON = JSON.parse(itemBytes.toString());

    var marketplace = [];
    var marketplaceBytes = await ctx.stub.getState("marketplace");
    if (marketplaceBytes && marketplaceBytes.length > 0) {
      marketplace = JSON.parse(marketplaceBytes.toString());
    }

    marketplace.push({
      name: item,
      price: price,
      qty: itemJSON.qty,
      owner: clientOrg,
    });

    const buffer = Buffer.from(JSON.stringify(marketplace));

    await ctx.stub.putState("marketplace", buffer);
    ctx.stub.setEvent("AddItemToMarketplace", buffer);

    await ctx.stub.deletePrivateData(collectionName, compositeKey);
  }

  async GetItemsInMarket(ctx) {
    var marketplaceBytes = await ctx.stub.getState("marketplace");
    let marketplace = [];
    if (marketplaceBytes && marketplaceBytes.length > 0) {
      marketplace = JSON.parse(marketplaceBytes.toString());
    } else {
      throw new Error(`marketplace not found`);
    }

    return JSON.stringify(marketplace);
  }

  async BuyFromMarket(ctx, item) {
    const clientOrg = ctx.clientIdentity.getMSPID();

    const buyerBalanceString = await this.GetBalance(ctx, clientOrg);
    var buyerBalance = JSON.parse(buyerBalanceString).balance;

    const marketplaceString = await this.GetItemsInMarket(ctx);
    const marketplace = JSON.parse(marketplaceString);

    var canBuy = false;
    var itemToBuy = null;

    const newMarketplace = marketplace.filter((existingItem) => {
      if (existingItem.name !== item || existingItem.owner === clientOrg) return true;
      if (existingItem.price * existingItem.qty > buyerBalance) return true;
      canBuy = true;
      itemToBuy = existingItem;
      return false;
    });

    if (canBuy) {
      await ctx.stub.putState("marketplace", Buffer.from(JSON.stringify(newMarketplace)));

      if (itemToBuy === null) {
        throw new Error(`some error happened. item was found null`);
      } else {
        buyerBalance -= itemToBuy.price * itemToBuy.qty;
        await ctx.stub.putState(clientOrg, Buffer.from(buyerBalance.toString()));

        const sellerBalanceString = await this.GetBalance(ctx, itemToBuy.owner);
        var sellerBalance = JSON.parse(sellerBalanceString).balance;
        sellerBalance += itemToBuy.price * itemToBuy.qty;
        await ctx.stub.putState(itemToBuy.owner, Buffer.from(sellerBalance.toString()));

        const compositeKey = ctx.stub.createCompositeKey("private_collection_", [itemToBuy.name]);
        const collectionName = clientOrg + "PrivateCollection";
        var itemBytes = await ctx.stub.getPrivateData(collectionName, compositeKey);

        let quantity = 0,
          price = null;
        if (itemBytes && itemBytes.length > 0) {
          const itemJSON = JSON.parse(itemBytes.toString());
          quantity = parseInt(itemJSON.qty);
          price = parseInt(itemJSON.price);
        }

        quantity += itemToBuy.qty;
        const itemEntry = {
          name: itemToBuy.name,
          qty: quantity,
          price: price !== null ? price : itemToBuy.price,
        };

        await ctx.stub.putPrivateData(collectionName, compositeKey, Buffer.from(JSON.stringify(itemEntry)));
      }
    }
  }
}

module.exports = MyContract;
