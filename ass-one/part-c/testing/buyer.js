const { LegacyTransaction } = require("@ethereumjs/tx");
const { Web3 } = require("web3");
const abi = require("./abi.json");
const { Common, Chain } = require("@ethereumjs/common");
require("dotenv").config();

const network = "sepolia";
const privateKey = new Buffer.from(process.env.PRIVATE_KEY, "hex");
const contractAddress = process.env.CONTRACT_ADDRESS;

const provider = `https://${network}.infura.io/v3/${process.env.INFURA_API_KEY}`;
const web3Provider = new Web3.providers.HttpProvider(provider);
const web3 = new Web3(web3Provider);

const myContract = new web3.eth.Contract(abi, contractAddress);
myContract.defaultChain = network;

const send = async (txMethod, value) => {
  try {
    const txCount = await web3.eth.getTransactionCount(process.env.WALLET_ADDRESS);

    const txObj = {
      nonce: web3.utils.toHex(txCount),
      to: contractAddress,
      from: process.env.WALLET_ADDRESS,
      gasPrice: web3.utils.toHex(await web3.eth.getGasPrice()),
      gasLimit: web3.utils.toHex(1000000),
      data: txMethod.encodeABI(),
      value: web3.utils.toHex(value),
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

const buyTicket = () => {
  const numTickets = 2;
  const txMethod = myContract.methods.buyTicket("test@test.com", numTickets);
  send(txMethod, numTickets * 1000000000000);
};

module.exports = { buyTicket };
