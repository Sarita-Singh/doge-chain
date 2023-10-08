const FabricCAServices = require("fabric-ca-client");
const { Wallets, Gateway } = require("fabric-network");
const fs = require("fs");
const path = require("path");

const ADMIN_ENROLLMENT_ID = "admin";
const ADMIN_ENROLLMENT_SECRET = "password";
const CLIENT_ENROLLMENT_ID = "client";
const CHANNEL = "doge-chain";
const CONTRACT = "testing-js-3";

async function main() {
  try {
    // Org1 connection profile
    const ccpPath = path.resolve(__dirname, "connection-org1.json");
    const ccp = JSON.parse(fs.readFileSync(ccpPath, "utf8"));

    // Org1 Ca
    const caInfo = ccp.certificateAuthorities["ca.org1.example.com"];
    const caTLSCACerts = caInfo.tlsCACerts.pem;
    const ca = new FabricCAServices(caInfo.url, { trustedRoots: caTLSCACerts, verify: false }, caInfo.caName);

    const walletPath = path.join(__dirname, "wallet");
    const wallet = await Wallets.newFileSystemWallet(walletPath);

    var adminIdentity = await wallet.get(ADMIN_ENROLLMENT_ID);
    if (!adminIdentity) {
      // Enroll Admin
      const enrollment = await ca.enroll({
        enrollmentID: ADMIN_ENROLLMENT_ID,
        enrollmentSecret: ADMIN_ENROLLMENT_SECRET,
      });
      const x509Identity = {
        credentials: {
          certificate: enrollment.certificate,
          privateKey: enrollment.key.toBytes(),
        },
        mspId: "Org1MSP",
        type: "X.509",
      };

      await wallet.put(ADMIN_ENROLLMENT_ID, x509Identity);
      console.log("Admin enrolled and saved into wallet successfully");

      adminIdentity = await wallet.get(ADMIN_ENROLLMENT_ID);
    }

    var userIdentity = await wallet.get(CLIENT_ENROLLMENT_ID);
    if (!userIdentity) {
      // Enroll user
      const provider = wallet.getProviderRegistry().getProvider(adminIdentity.type);
      const adminUser = await provider.getUserContext(adminIdentity, ADMIN_ENROLLMENT_ID);

      const secret = await ca.register(
        { affiliation: "org1.department1", enrollmentID: CLIENT_ENROLLMENT_ID, role: "client" },
        adminUser
      );
      const enrollment = await ca.enroll({ enrollmentID: CLIENT_ENROLLMENT_ID, enrollmentSecret: secret });

      const x509Identity = {
        credentials: { certificate: enrollment.certificate, privateKey: enrollment.key.toBytes() },
        mspId: "Org1MSP",
        type: "X.509",
      };

      await wallet.put(CLIENT_ENROLLMENT_ID, x509Identity);
      console.log("Enrolled appUser and saved to wallet");

      userIdentity = await wallet.get(CLIENT_ENROLLMENT_ID);
    }

    // Connect to gateway
    const gateway = new Gateway();
    await gateway.connect(ccp, {
      wallet,
      identity: CLIENT_ENROLLMENT_ID,
      discovery: { enabled: true, asLocalhost: true },
    });

    // connect to channel
    const network = await gateway.getNetwork(CHANNEL);

    // select the contract
    const contract = network.getContract(CONTRACT);

    const args = process.argv.slice(2);
    const command = args[0];

    if (command === "ADD_MONEY") {
      const organization = args[1];
      const amount = args[2];
      await contract.submitTransaction("AddBalance", organization, amount);
    } else if (command === "ADD_ITEM") {
      const itemName = args[1];
      const itemCount = args[2];
      const itemPrice = args[3];
      await contract.submitTransaction("AddItem", itemName, itemCount, itemPrice);
    } else if (command === "QUERY_BALANCE") {
      const organization = args[1];
      const result = await contract.evaluateTransaction("GetBalance", organization);
      console.log(result.toString());
    } else if (command === "GET_ITEM") {
      const itemName = args[1];
      const result = await contract.evaluateTransaction("GetItem", itemName);
      console.log(result.toString());
    }

    gateway.disconnect();
  } catch (err) {
    console.log("Error: ", err);
  }
}

main();
