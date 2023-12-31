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
const { buildCCPOrg1, buildWallet, prettyJSONString, buildCCPOrg2 } = require("./AppUtil.js");
const { exit } = require("process");
const fs = require("fs");

const RED = "\x1b[31m";
const GREEN = "\x1b[32m";
const BLUE = "\x1b[34m";
const RESET = "\x1b[0m";

const args = process.argv.slice(2);

if (args.length < 1) exit(1);

const channelName = "doge-chain";
const chaincodeName = "part-b";

const mspOrg1 = "Org1MSP";
const mspOrg2 = "Org2MSP";

const org1UserId = "appUserOrg1";
const org2UserId = "appUserOrg2";

const MSP = args[0] === "1" ? mspOrg1 : mspOrg2;
const userId = `${MSP === mspOrg1 ? org1UserId : org2UserId}-b`;

const walletPath = path.join(__dirname, "wallet", MSP);
const caHostName = MSP === mspOrg1 ? "ca.org1.example.com" : "ca.org2.example.com";
const affiliation = MSP === mspOrg1 ? "org1.department1" : "org2.department1";
const wishlistFile = MSP + "-wishlist.txt";

async function main() {
  try {
    // build an in memory object with the network configuration (also known as a connection profile)
    const ccp = MSP === mspOrg1 ? buildCCPOrg1() : buildCCPOrg2();

    // build an instance of the fabric ca services client based on
    // the information in the network configuration
    const caClient = buildCAClient(FabricCAServices, ccp, caHostName);

    // setup the wallet to hold the credentials of the application user
    const wallet = await buildWallet(Wallets, walletPath);

    // in a real application this would be done on an administrative flow, and only once
    await enrollAdmin(caClient, wallet, MSP);

    // in a real application this would be done only when a new user was required to be added
    // and would be part of an administrative flow
    await registerAndEnrollUser(caClient, wallet, MSP, userId, affiliation);

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
        identity: userId,
        discovery: { enabled: true, asLocalhost: true }, // using asLocalhost as this gateway is using a fabric network deployed locally
      });

      // Build a network instance based on the channel where the smart contract is deployed
      const network = await gateway.getNetwork(channelName);

      // Get the contract from the network.
      const contract = network.getContract(chaincodeName);

      const command = args[1];

      // For running AddBalance
      if (command === "ADD_MONEY") {
        const amount = args[2];
        let balanceData = { balance: amount };

        let statefulTxn = contract.createTransaction("AddBalance");
        let tmapData = Buffer.from(JSON.stringify(balanceData));

        statefulTxn.setTransient({
          balance_amount: tmapData,
        });
        await statefulTxn.submit();

        console.log(`${GREEN}\n--> Money added to global state for ${MSP}.${RESET}`);
      }

      // For running AddItem
      else if (command === "ADD_ITEM") {
        const itemName = args[2];
        const itemCount = args[3];
        const itemPrice = args[4];
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
        statefulTxn.setEndorsingOrganizations(MSP);
        await statefulTxn.submit();
        console.log(`${GREEN}\n--> Added Item as private data to ${MSP}.${RESET}`);
      }

      // For running GetBalance
      else if (command === "QUERY_BALANCE") {
        const organization = args[2];
        const result = await contract.evaluateTransaction("GetBalance", organization);
        console.log(`${GREEN}\n--> Fetched balance of ${organization}.${RESET}`);
        console.log(`${BLUE}Result: ${prettyJSONString(result.toString())}${RESET}`);
      }

      // For running GetItem
      else if (command === "GET_ITEM") {
        const result = await contract.evaluateTransaction("GetItem");
        console.log(`${GREEN}\n--> Fetched all items of ${MSP}.${RESET}`);
        console.log(`${BLUE}Result: ${prettyJSONString(result.toString())}${RESET}`);
      }

      // For running GetItemsInMarket
      else if (command === "ALL_ITEMS") {
        const result = await contract.evaluateTransaction("GetItemsInMarket");
        console.log(`${GREEN}\n--> Fetched all items from marketplace.${RESET}`);
        console.log(`${BLUE}Result: ${prettyJSONString(result.toString())}${RESET}`);
      }

      // For running AddToMarket
      else if (command === "ENLIST_ITEM") {
        const itemName = args[2];
        const itemPrice = args[3];
        let statefulTxn = contract.createTransaction("AddToMarket");
        statefulTxn.setEndorsingOrganizations(MSP);
        await statefulTxn.submit(itemName, itemPrice);
        console.log(`${GREEN}\n--> ${MSP} added ${itemName} to marketplace.${RESET}`);
      }

      // For running BuyFromMarket. Debugging function
      else if (command === "BUY_ITEM") {
        const itemName = args[2];
        let statefulTxn = contract.createTransaction("BuyFromMarket");
        statefulTxn.setEndorsingOrganizations(MSP);
        await statefulTxn.submit(itemName);
        console.log(`${GREEN}\n--> ${MSP} bought ${itemName} from marketplace.${RESET}`);
      }

      // For adding to wishlist
      else if (command === "WISHLIST") {
        const itemName = args[2];

        if (fs.existsSync(wishlistFile)) {
          fs.appendFile(wishlistFile, `${itemName}\n`, (error) => {
            if (error) console.log(`${RED}******** FAILED to append to wishlist file: ${error}${RESET}`);
            else console.log(`${GREEN}\n--> Added ${itemName} to wishlist of ${MSP}.${RESET}`);
          });
        } else {
          fs.writeFile(wishlistFile, `${itemName}\n`, (error) => {
            if (error) console.log(`${RED}******** FAILED to write to wishlist file: ${error}${RESET}`);
            else console.log(`${GREEN}\n--> Added ${itemName} to wishlist of ${MSP}.${RESET}`);
          });
        }
      }

      // Wait for new item to be added
      else {

        const listener = async (event) => {
          console.log(
            `${BLUE}--> Contract Event Received: ${event.eventName} - ${prettyJSONString(event.payload.toString())}${RESET}`
          );
          if (event.eventName === "AddItemToMarketplace") {
            console.log(`${BLUE}--> Required Event Detected${RESET}`)
            const addedItems = JSON.parse(event.payload.toString());

            if (fs.existsSync(wishlistFile)) {
              const lines = fs.readFileSync(wishlistFile).toString().split("\n")

              await addedItems.forEach(async (addedItem) => {
                console.log(`${BLUE}DEBUG - ${addedItem.name}, ${lines}${RESET}`)
                if (lines.includes(addedItem.name)) {
                  console.log(`${GREEN}\n--> Item "${addedItem.name}" in wishlist of ${MSP}. Trying to buy.${RESET}`);

                  let statefulTxn = contract.createTransaction("BuyFromMarket");
                  statefulTxn.setEndorsingOrganizations(MSP);
                  const itemName = addedItem.name;
                  var exec = require('child_process').exec;
                  var command = 'node index.js ' + args[0] + ' BUY_ITEM ' + itemName;
                  console.log(command);
                  exec(command,
                    function (error, stdout, stderr) {
                      console.log('stdout: ' + stdout);
                      console.log('stderr: ' + stderr);
                      if (error !== null) {
                        console.log('exec error: ' + error);
                      }
                    });
                  // console.log((await statefulTxn.submit(itemName)).toString());
                  console.log(`${GREEN}\n--> ${MSP} bought ${addedItem.name} from marketplace.${RESET}`);

                }
              })
            } else {
              if (error) console.log(`${RED}******** No wishlist file found. No action taken.${RESET}`);
            }
          }
        };

        await contract.addContractListener(listener);
        while (1) { }
      }
    } finally {
      // The inevitable
      // Disconnect from the gateway when the application is closing
      // This will close all connections to the network
      gateway.disconnect();
    }
  } catch (error) {
    // The unknown
    console.error(`${RED}******** FAILED to run the application: ${error}${RESET}`);
  }
}

main();
