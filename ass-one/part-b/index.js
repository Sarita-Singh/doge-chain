const { LegacyTransaction } = require("@ethereumjs/tx");
const { Web3 } = require("web3");
const abi = require("./abi.json");
const { Common, Chain } = require("@ethereumjs/common");
require("dotenv").config();

const network = "sepolia";
const privateKey = new Buffer(process.env.PRIVATE_KEY, "hex");
const contractAddress = "0xF98bFe8bf2FfFAa32652fF8823Bba6714c79eDd4";

const provider = `https://${network}.infura.io/v3/${process.env.INFURA_API_KEY}`;
const web3Provider = new Web3.providers.HttpProvider(provider);
const web3 = new Web3(web3Provider);

const myContract = new web3.eth.Contract(abi, contractAddress);
myContract.defaultChain = network;

const getRollForGivenAddress = () => {
  myContract.methods
    .get("0x328Ff6652cc4E79f69B165fC570e3A0F468fc903")
    .call()
    .then(function (output) {
      console.log(output);
    });
};

const getMyRoll = () => {
  myContract.methods
    .getmine()
    .call({
      from: process.env.WALLET_ADDRESS,
    })
    .then(function (output) {
      console.log(output);
    });
};

const setMyRoll = async () => {
  const txMethod = myContract.methods.update("20CS10020");

  try {
    const txCount = await web3.eth.getTransactionCount(process.env.WALLET_ADDRESS);

    const txObj = {
      nonce: web3.utils.toHex(txCount),
      to: contractAddress,
      from: process.env.WALLET_ADDRESS,
      gasPrice: web3.utils.toHex(await web3.eth.getGasPrice()),
      gasLimit: web3.utils.toHex(await txMethod.estimateGas()),
      data: txMethod.encodeABI(),
    };

    const tx = LegacyTransaction.fromTxData(txObj, { common: new Common({ chain: Chain.Sepolia }) });
    const signedTx = tx.sign(privateKey);
    const serializedTx = signedTx.serialize();

    web3.eth.sendSignedTransaction(serializedTx).then((receipt) => {
      console.log(receipt);
      console.log(`https://${network}.etherscan.io/tx/${receipt.transactionHash}`);
    });
  } catch (err) {
    console.log(err);
  }
};

module.exports = { getRollForGivenAddress, getMyRoll, setMyRoll };
