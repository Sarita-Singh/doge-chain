/*
 * Copyright IBM Corp. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

"use strict";

const fs = require("fs");
const path = require("path");

const RED = "\x1b[31m\n";
const GREEN = "\x1b[32m\n";
const BLUE = "\x1b[34m";
const RESET = "\x1b[0m";

exports.buildCCPOrg1 = () => {
  // load the common connection configuration file
  const ccpPath = path.resolve(
    __dirname,
    "..",
    "..",
    "fabric",
    "fabric-samples",
    "test-network",
    "organizations",
    "peerOrganizations",
    "org1.example.com",
    "connection-org1.json"
  );
  const fileExists = fs.existsSync(ccpPath);
  if (!fileExists) {
    throw new Error(`${RED}*** no such file or directory: ${ccpPath}${RESET}`);
  }
  const contents = fs.readFileSync(ccpPath, "utf8");

  // build a JSON object from the file contents
  const ccp = JSON.parse(contents);

  console.log(`${GREEN}--> Loaded the network configuration located at ${ccpPath}${RESET}`);
  return ccp;
};

exports.buildCCPOrg2 = () => {
  // load the common connection configuration file
  const ccpPath = path.resolve(
    __dirname,
    "..",
    "..",
    "test-network",
    "organizations",
    "peerOrganizations",
    "org2.example.com",
    "connection-org2.json"
  );
  const fileExists = fs.existsSync(ccpPath);
  if (!fileExists) {
    throw new Error(`${RED}*** no such file or directory: ${ccpPath}${RESET}`);
  }
  const contents = fs.readFileSync(ccpPath, "utf8");

  // build a JSON object from the file contents
  const ccp = JSON.parse(contents);

  console.log(`${GREEN}--> Loaded the network configuration located at ${ccpPath}${RESET}`);
  return ccp;
};

exports.buildWallet = async (Wallets, walletPath) => {
  // Create a new  wallet : Note that wallet is for managing identities.
  let wallet;
  if (walletPath) {
    wallet = await Wallets.newFileSystemWallet(walletPath);
    console.log(`${GREEN}--> Built a file system wallet at ${walletPath}${RESET}`);
  } else {
    wallet = await Wallets.newInMemoryWallet();
    console.log(`${GREEN}--> Built an in memory wallet${RESET}`);
  }

  return wallet;
};

exports.prettyJSONString = (inputString) => {
  if (inputString) {
    return JSON.stringify(JSON.parse(inputString), null, 2);
  } else {
    return inputString;
  }
};
