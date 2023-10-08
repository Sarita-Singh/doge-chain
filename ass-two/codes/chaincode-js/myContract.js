"use strict";

const { Contract } = require("fabric-contract-api");

class MyContract extends Contract {
  constructor() {
    super("MyContract");
  }

  async AddBalance(ctx, org, amount) {
    var balanceBytes = await ctx.stub.getState(org);
    let balance = 0;
    if (balanceBytes && balanceBytes.length > 0) {
      balance = parseInt(balanceBytes.toString());
    }
    balance += parseInt(amount);
    await ctx.stub.putState(org, Buffer.from(balance.toString()));
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

  async AddItem(ctx, itemName, itemNum, itemPrice) {
    const itemEntry = {
      name: itemName,
      qty: itemNum,
      price: itemPrice,
    };
    const compositeKey = ctx.stub.createCompositeKey("_implicit_org", [itemName]);
    await ctx.stub.putPrivateData("_implicit_org", compositeKey, Buffer.from(JSON.stringify(itemEntry)));
  }

  async GetItem(ctx, itemName) {
    const compositeKey = ctx.stub.createCompositeKey("_implicit_org", [itemName]);
    var itemBytes = await ctx.stub.getPrivateData("_implicit_org", compositeKey);
    if (!itemBytes || itemBytes.length == 0) throw new Error(`Inventory entry not found for ${itemName}`);
    return itemBytes.toString();
  }
}

module.exports = MyContract;
