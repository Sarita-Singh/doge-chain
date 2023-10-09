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
  async AddItem(ctx, MSPID, itemName, itemNum, itemPrice) {
    const compositeKey = ctx.stub.createCompositeKey("private_collection_", [itemName]);
    const collectionName = MSPID + "PrivateCollection";
    var itemBytes = await ctx.stub.getPrivateData(collectionName,compositeKey);
    let quantity = 0;
    if(itemBytes && itemBytes.length > 0){
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

  async GetItem(ctx, MSPID) {
    
    const collectionName = MSPID + "PrivateCollection";
    var iterator = await ctx.stub.getPrivateDataByRange(collectionName,'','');
    const inventory = [];
    for await (const queryResult of iterator){
      inventory.push(queryResult.value.toString('utf8'));
    }
    return JSON.stringify(inventory);
  }
}

module.exports = MyContract;
