const { Web3 } = require("web3");
const abi = require("./abi.json");
require("dotenv").config();

const network = "sepolia";
const contractAddress = "0x17195a486B3c25CedFa8716CF1fb94aE64208Db9";

const provider = `https://${network}.infura.io/v3/${process.env.INFURA_API_KEY}`;
const web3Provider = new Web3.providers.HttpProvider(provider);
const web3 = new Web3(web3Provider);

const myContract = new web3.eth.Contract(abi, contractAddress);
myContract.defaultChain = network;

const seller = () => {
  myContract.methods
    .seller()
    .call()
    .then(function (output) {
      console.log(output);
    });
};

const numTicketsSold = () => {
  myContract.methods
    .numTicketsSold()
    .call()
    .then(function (output) {
      console.log(output);
    });
};

const quota = () => {
  myContract.methods
    .quota()
    .call()
    .then(function (output) {
      console.log(output);
    });
};

const price = () => {
  myContract.methods
    .price()
    .call()
    .then(function (output) {
      console.log(output);
    });
};

module.exports = { seller, numTicketsSold, quota, price };
