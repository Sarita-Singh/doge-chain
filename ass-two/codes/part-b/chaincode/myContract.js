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
      throw new Error("balance amount not found in the transient map");
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
    const clientOrg = ctx.clientIdentity.getMSPID();
    const compositeKey = ctx.stub.createCompositeKey("private_collection_", [itemName]);
    const collectionName = clientOrg + "PrivateCollection";
    var itemBytes = await ctx.stub.getPrivateData(collectionName, compositeKey);
    let itemEntry = jsonFromString;
    if (itemBytes && itemBytes.length > 0) {
      const itemBytesJSON = JSON.parse(itemBytes.toString());
      itemEntry.qty = (parseInt(itemBytesJSON.qty) + parseInt(itemEntry.qty)).toString();
    }

    await ctx.stub.putPrivateData(collectionName, compositeKey, Buffer.from(JSON.stringify(itemEntry)));
  }

  async GetItem(ctx) {
    const clientOrg = ctx.clientIdentity.getMSPID();
    const collectionName = clientOrg + "PrivateCollection";
    const partialKey = "private_collection_";
    const attr = [];
    var iterator = ctx.stub.getPrivateDataByPartialCompositeKey(collectionName, partialKey, attr);
    const inventory = [];
    for await (const queryResult of iterator) {
      inventory.push(queryResult.value.toString("utf8"));
    }
    return JSON.stringify(inventory);
  }

  async QueryItem(ctx, itemName) {
    const clientOrg = ctx.clientIdentity.getMSPID();
    const compositeKey = ctx.stub.createCompositeKey("private_collection_", [itemName]);
    const collectionName = clientOrg + "PrivateCollection";
    var itemBytes = await ctx.stub.getPrivateData(collectionName, compositeKey);
    if (itemBytes && itemBytes.length > 0) {
      return itemBytes.toString();
    }
    const itemEntry = {
      name: itemName,
      qty: "0",
      price: "0",
    };
    return JSON.stringify(itemEntry);
  }

  async AddToMarket(ctx) {
    const clientOrg = ctx.clientIdentity.getMSPID();

    const transientMap = ctx.stub.getTransient();
    const transientItemJSON = transientMap.get("item_entry");
    if (transientItemJSON.length === 0) {
      throw new Error("balance amount not found in the transient map");
    }

    const jsonBytesToString = String.fromCharCode(...transientItemJSON);
    const jsonFromString = JSON.parse(jsonBytesToString);
    if (jsonFromString.name.length == 0) {
      throw new Error("name field must be a non-empty string");
    }
    if (jsonFromString.qty.length == 0) {
      throw new Error("qty field must be a non-empty string");
    }

    const itemName = jsonFromString.name;
    const price = jsonFromString.qty;
    const compositeKey = ctx.stub.createCompositeKey("private_collection_", [itemName]);
    const collectionName = clientOrg + "PrivateCollection";
    var itemBytes = await ctx.stub.getPrivateData(collectionName, compositeKey);

    if (!itemBytes || itemBytes.length === 0) {
      throw new Error(`Item '${itemName}' not found in the inventory.`);
    }

    var marketplace = [];
    var marketplaceBytes = await ctx.stub.getState("marketplace");
    if (marketplaceBytes && marketplaceBytes.length > 0) {
      marketplace = JSON.parse(marketplaceBytes.toString());
    }

    marketplace.push({
      itemName: itemName,
      price: price,
      owner: clientOrg,
    });

    await ctx.stub.putState("marketplace", Buffer.from(JSON.stringify(marketplace)));

    // await ctx.stub.deletePrivateData(collectionName, compositeKey);
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
}

module.exports = MyContract;
