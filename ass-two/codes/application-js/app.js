// terminal-app.js
const { Gateway, Wallets, X509WalletMixin } = require('fabric-network');
const FabricCAServices = require('fabric-ca-client');
const fs = require('fs');
const path = require('path');
const contractName = 'mySecondCC';
const channelName = 'mychannel';
const caURL = 'https://ca.org1.example.com:7054';
const caName = 'ca.org1.example.com';
const mspOrg1 = 'Org1MSP';
const adminUserId = 'admin';
const adminUserPasswd = 'adminpw';
const userID = 'user1';
async function main() {
  try {
    const ccpPath = path.resolve(__dirname, 'connection-org1.json');
    const ccpJSON = fs.readFileSync(ccpPath, 'utf8');
    const ccp = JSON.parse(ccpJSON);
    const caInfo = ccp.certificateAuthorities[caName];
    const caTLSCACerts = caInfo.tlsCACerts.pem;
    const caClient = new FabricCAServices(caInfo.url, { trustedRoots: caTLSCACerts, verify: false }, caInfo.caName);

    const walletPath = path.join(__dirname, 'wallet');
    const wallet = await Wallets.newFileSystemWallet(walletPath);
    const identity = await wallet.get(adminUserId);
    if (!identity) {
      const enrollment = await caClient.enroll({ enrollmentID: adminUserId, enrollmentSecret: adminUserPasswd });
      const x509Identity = {
        credentials: {
          certificate: enrollment.certificate,
          privateKey: enrollment.key.toBytes(),
        },
        mspId: orgMspId,
        type: 'X.509',
      };
      await wallet.put(adminUserId, x509Identity);
    }
    const userIdentity = await wallet.get(userID);
    if (!userIdentity) {
      const adminIdentity = await wallet.get(adminUserId);
      if (!adminIdentity) {
        console.log('An identity for the admin user does not exist in the wallet');
        console.log('Enroll the admin user before retrying');
        return;
      }
      const provider = wallet.getProviderRegistry().getProvider(adminIdentity.type);
      const adminUser = await provider.getUserContext(adminIdentity, adminUserId);

      // Register the user, enroll the user, and import the new identity into the wallet.
      // if affiliation is specified by client, the affiliation value must be configured in CA
      const secret = await caClient.register({
        affiliation: 'org1.department1',
        enrollmentID: userID,
        role: 'client'
      }, adminUser);
      const enrollment = await caClient.enroll({
        enrollmentID: userID,
        enrollmentSecret: secret
      });
      const x509Identity = {
        credentials: {
          certificate: enrollment.certificate,
          privateKey: enrollment.key.toBytes(),
        },
        mspId: mspOrg1,
        type: 'X.509',
      };
      await wallet.put(userID, x509Identity);
      console.log(`Successfully registered and enrolled user ${userID} and imported it into the wallet`);
    }

    const gateway = new Gateway();
    await gateway.connect(ccp, {
      wallet,
      identity: userID, // Use the user identity for this organization
      discovery: { enabled: true, asLocalhost: true },
    });

    const network = await gateway.getNetwork(channelName);
    const contract = network.getContract(contractName);

    const args = process.argv.slice(2);
    const command = args[0];

    if (command === 'ADD_MONEY') {
      const organization = args[1];
      const amount = args[2];
      await contract.submitTransaction('AddBalance', organization, amount);
    } else if (command === 'ADD_ITEM') {
      const itemName = args[1];
      const itemCount = args[2];
      const itemPrice = args[3];
      await contract.submitTransaction('AddItem', itemName, itemCount, itemPrice);
    } else if (command === 'QUERY_BALANCE') {
      const organization = args[1];
      const result = await contract.evaluateTransaction('GetBalance', organization);
      console.log(result.toString());
    } else if (command === 'GET_ITEM') {
      const itemName = args[1];
      const result = await contract.evaluateTransaction('GetItem', itemName);
      console.log(result.toString());
    }

    gateway.disconnect();
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

main();
