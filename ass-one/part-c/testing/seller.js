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

const send = async (txMethod) => {
  try {
    const txCount = await web3.eth.getTransactionCount(process.env.WALLET_ADDRESS);

    const txObj = {
      nonce: web3.utils.toHex(txCount),
      to: contractAddress,
      from: process.env.WALLET_ADDRESS,
      gasPrice: web3.utils.toHex(await web3.eth.getGasPrice()),
      gasLimit: web3.utils.toHex(50000),
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

const getBuyerAmountPaid = () => {
  myContract.methods
    .getBuyerAmountPaid(process.env.BUYER_ADDRESS)
    .call()
    .then(function (output) {
      console.log(output);
    });
};

const withdrawFunds = () => {
  const txMethod = myContract.methods.withdrawFunds();
  send(txMethod);
};

const refundTicket = () => {
  const txMethod = myContract.methods.refundTicket(process.env.BUYER_ADDRESS);
  send(txMethod);
};

const kill = () => {
  const txMethod = myContract.methods.kill();
  send(txMethod);
};

module.exports = { getBuyerAmountPaid, withdrawFunds, refundTicket, kill };
