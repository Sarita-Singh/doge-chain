var { Web3 } = require("web3");
require("dotenv").config();

var provider = `https://mainnet.infura.io/v3/${process.env.INFURA_API_KEY}`;
var web3Provider = new Web3.providers.HttpProvider(provider);
var web3 = new Web3(web3Provider);
web3.eth.getBalance("0xBaF6dC2E647aeb6F510f9e318856A1BCd66C5e19").then((value) => console.log(value));
