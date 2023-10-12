/*
 * Copyright IBM Corp. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

"use strict";

const { Gateway, Wallets } = require("fabric-network");
const FabricCAServices = require("fabric-ca-client");
const path = require("path");
const { buildCAClient, registerAndEnrollUser, enrollAdmin } = require("./CAUtil.js");
const { buildCCPOrg1, buildWallet, prettyJSONString } = require("./AppUtil.js");

const RED = "\x1b[31m";
const GREEN = "\x1b[32m";
const BLUE = "\x1b[34m";
const RESET = "\x1b[0m";

const channelName = "doge-chain";
const chaincodeName = "part-a";
const mspOrg1 = "Org1MSP";
const walletPath = path.join(__dirname, "wallet");
const org1UserId = "appUser";

/**
 * To see the SDK workings, try setting the logging to show on the console before running
 *        export HFC_LOGGING='{"debug":"console"}'
 */
async function main() {
  try {
    // build an in memory object with the network configuration (also known as a connection profile)
    const ccp = buildCCPOrg1();

    // build an instance of the fabric ca services client based on
    // the information in the network configuration
    const caClient = buildCAClient(FabricCAServices, ccp, "ca.org1.example.com");

    // setup the wallet to hold the credentials of the application user
    const wallet = await buildWallet(Wallets, walletPath);

    // in a real application this would be done on an administrative flow, and only once
    await enrollAdmin(caClient, wallet, mspOrg1);

    // in a real application this would be done only when a new user was required to be added
    // and would be part of an administrative flow
    await registerAndEnrollUser(caClient, wallet, mspOrg1, org1UserId, "org1.department1");

    // Create a new gateway instance for interacting with the fabric network.
    // In a real application this would be done as the backend server session is setup for
    // a user that has been verified.
    const gateway = new Gateway();

    try {
      // setup the gateway instance
      // The user will now be able to create connections to the fabric network and be able to
      // submit transactions and query. All transactions submitted by this gateway will be
      // signed by this user using the credentials stored in the wallet.
      await gateway.connect(ccp, {
        wallet,
        identity: org1UserId,
        discovery: { enabled: true, asLocalhost: true }, // using asLocalhost as this gateway is using a fabric network deployed locally
      });

      // Build a network instance based on the channel where the smart contract is deployed
      const network = await gateway.getNetwork(channelName);

      // Get the contract from the network.
      const contract = network.getContract(chaincodeName);

      const args = process.argv.slice(2);
      const command = args[0];

      if (command === "ADD_MONEY") {
        const amount = args[1];
        let balanceData = { balance: amount };
        let statefulTxn = contract.createTransaction("AddBalance");
        let tmapData = Buffer.from(JSON.stringify(balanceData));
        statefulTxn.setTransient({
          balance_amount: tmapData,
        });
        await statefulTxn.submit();
        console.log(`${GREEN}\n--> Money added to global state.${RESET}`);
      } else if (command === "ADD_ITEM") {
        const itemName = args[1];
        const itemCount = args[2];
        const itemPrice = args[3];
        let itemEntry = {
          name: itemName,
          qty: itemCount,
          price: itemPrice,
        };
        let tmapData = Buffer.from(JSON.stringify(itemEntry));
        let statefulTxn = contract.createTransaction("AddItem");
        statefulTxn.setTransient({
          item_entry: tmapData,
        });
        statefulTxn.setEndorsingOrganizations(mspOrg1);
        await statefulTxn.submit();
        console.log(`${GREEN}\n--> Added Item as private data to ${mspOrg1}.${RESET}`);
      } else if (command === "QUERY_BALANCE") {
        const organization = args[1];
        const result = await contract.evaluateTransaction("GetBalance", organization);
        console.log(`${GREEN}\n--> Fetched balance of ${organization}.${RESET}`);
        console.log(`${BLUE}Result: ${prettyJSONString(result.toString())}${RESET}`);
      } else if (command === "GET_ITEM") {
        const result = await contract.evaluateTransaction("GetItem");
        console.log(`${GREEN}\n--> Fetched all items.${RESET}`);
        console.log(`${BLUE}Result: ${prettyJSONString(result.toString())}${RESET}`);
      }
    } finally {
      // Disconnect from the gateway when the application is closing
      // This will close all connections to the network
      gateway.disconnect();
    }
  } catch (error) {
    console.error(`${RED}******** FAILED to run the application: ${error}${RESET}`);
  }
}

main();
