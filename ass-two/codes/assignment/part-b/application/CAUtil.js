/* Code taken from https://github.com/hyperledger/fabric-samples/blob/main/test-application/javascript/CAUtil.js */

/*
 * Copyright IBM Corp. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

"use strict";

const RED = "\x1b[31m";
const GREEN = "\x1b[32m";
const BLUE = "\x1b[34m";
const RESET = "\x1b[0m";

const adminUserId = "admin";
const adminUserPasswd = "adminpw";

const logging = process.env.DEBUG;

/**
 *
 * @param {*} FabricCAServices
 * @param {*} ccp
 */
exports.buildCAClient = (FabricCAServices, ccp, caHostName) => {
  // Create a new CA client for interacting with the CA.
  const caInfo = ccp.certificateAuthorities[caHostName]; //lookup CA details from config
  const caTLSCACerts = caInfo.tlsCACerts.pem;
  const caClient = new FabricCAServices(caInfo.url, { trustedRoots: caTLSCACerts, verify: false }, caInfo.caName);

  if (logging) console.log(`${GREEN}--> Built a CA Client named ${caInfo.caName}${RESET}`);
  return caClient;
};

exports.enrollAdmin = async (caClient, wallet, orgMspId) => {
  try {
    // Check to see if we've already enrolled the admin user.
    const identity = await wallet.get(adminUserId);
    if (identity) {
      if (logging) console.log(`${GREEN}--> An identity for the admin user already exists in the wallet${RESET}`);
      return;
    }

    // Enroll the admin user, and import the new identity into the wallet.
    const enrollment = await caClient.enroll({ enrollmentID: adminUserId, enrollmentSecret: adminUserPasswd });
    const x509Identity = {
      credentials: {
        certificate: enrollment.certificate,
        privateKey: enrollment.key.toBytes(),
      },
      mspId: orgMspId,
      type: "X.509",
    };
    await wallet.put(adminUserId, x509Identity);
    if (logging) console.log(`${GREEN}--> Successfully enrolled admin user and imported it into the wallet${RESET}`);
  } catch (error) {
    console.error(`${RED}*** Failed to enroll admin user : ${error}${RESET}`);
  }
};

exports.registerAndEnrollUser = async (caClient, wallet, orgMspId, userId, affiliation) => {
  try {
    // Check to see if we've already enrolled the user
    const userIdentity = await wallet.get(userId);
    if (userIdentity) {
      if (logging) console.log(`${GREEN}--> An identity for the user ${userId} already exists in the wallet${RESET}`);
      return;
    }

    // Must use an admin to register a new user
    const adminIdentity = await wallet.get(adminUserId);
    if (!adminIdentity) {
      if (logging) console.log(`An identity for the admin user does not exist in the wallet`);
      if (logging) console.log(`${BLUE}--> Enroll the admin user before retrying${RESET}`);
      return;
    }

    // build a user object for authenticating with the CA
    const provider = wallet.getProviderRegistry().getProvider(adminIdentity.type);
    const adminUser = await provider.getUserContext(adminIdentity, adminUserId);

    // Register the user, enroll the user, and import the new identity into the wallet.
    // if affiliation is specified by client, the affiliation value must be configured in CA
    const secret = await caClient.register(
      {
        affiliation: affiliation,
        enrollmentID: userId,
        role: "client",
      },
      adminUser
    );
    const enrollment = await caClient.enroll({
      enrollmentID: userId,
      enrollmentSecret: secret,
    });
    const x509Identity = {
      credentials: {
        certificate: enrollment.certificate,
        privateKey: enrollment.key.toBytes(),
      },
      mspId: orgMspId,
      type: "X.509",
    };
    await wallet.put(userId, x509Identity);
    if (logging)
      console.log(
        `${GREEN}--> Successfully registered and enrolled user ${userId} and imported it into the wallet${RESET}`
      );
  } catch (error) {
    console.error(`${RED}*** Failed to register user : ${error}${RESET}`);
  }
};
