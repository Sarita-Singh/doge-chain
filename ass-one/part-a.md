## Part A

### 1. Query the current gas price in wei

- Answer: 5739970681
- JSON RPC payload:

  ```json
  {
    "jsonrpc": "2.0",
    "method": "eth_gasPrice",
    "params": [],
    "id": 1
  }
  ```

- Response:
  ```json
  {
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x156210079"
  }
  ```

### 2. Query the current latest block number (converted to decimal)

- Answer: 4281630
- JSON RPC payload:

  ```json
  {
    "jsonrpc": "2.0",
    "method": "eth_getBlockByNumber",
    "params": ["latest", false],
    "id": 1
  }
  ```

- Response:
  ```json
  {
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "baseFeePerGas": "0x15620fae7",
        "difficulty": "0x0",
        "extraData": "0xd883010c02846765746888676f312e32302e37856c696e7578",
        "gasLimit": "0x1c9c380",
        "gasUsed": "0x407386",
        "hash": "0x1f1ed2cec192df4ab2cee438c2a5856bebd15c52aa56951ba488931c2b98e69d",
        "logsBloom": "0x00000080081000000008100000840000100040100008000000000000080001000000000301820000000288001008000000000000000240000030a102082400000000002000000500400801880a000000009000000000425000000000000000010c000000120040040200000c0000080002018800001000004d0002100000000000000141002030042000000000000040040020881040110000050000041000010e0800000000000000000000000000003000020000000000800010008400c08001040042030100000000101103004000000048040000010000001400000060000090000040020012a00000000002081010080001000008000000004002000040",
        "miner": "0x8b0c2c4c8eb078bc6c01f48523764c8942c0c6c4",
        "mixHash": "0xf840925f28f27fb5dbcdacc32f61142f4e62104f8a0e92d98f9cab7f715d9b3a",
        "nonce": "0x0000000000000000",
        "number": "0x41551e",
        "parentHash": "0x400967494b0f0e602de04929290c753151f541a78693e8f800042286c27f4ada",
        "receiptsRoot": "0x3d4eee9f2eefcc14dc3ba130426a4afd1e8cb97b874f7cc9d982f7b855b0702c",
        "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        "size": "0xef34",
        "stateRoot": "0x7e3648e8da7d1586f55595665fa5b9e5d3d3cf3898c50e359d98d22cd3bfb9bc",
        "timestamp": "0x6501f00c",
        "totalDifficulty": "0x3c656d23029ab0",
        "transactions": [
            "0x65e598c85cd17fd5aa77d050f8ab9bebd773d5ab30d126f2b7607eb7f79d9200",
            "0x3bb1dca1fcaa51dc20153852a66ee1d373b341f9e24fa51ca0b18950effce680",
            "0x4e1364e6e7c2ac668aab6581629d6ab05c2e30ef071c9991353a88ef78a26bfe",
            "0xa71833090243a5b52e0487d23eaa832692a32aa3df066efb85e60efe533cc291",
            "0x5bc27fdbd5630bce7c1e70a97787bda71070f3dcebf715f66923d59fa115f742",
            "0xcbd6ffc0525d97f4238288b573ab7cb0d0411e05ea7326e47061ca56babe570a",
            "0xf414441e1f9dc320a5ecbf9b6ce27b10d86f94a9582243c0b203382cd1a2dc07",
            "0x319b64e2ab32591174fffc15170a5d5c58a193e897185872472d87a43a66ea13",
            "0xbc7bc121030df9fc0c2ad3896e2158ab08ef30cdeb64e1e7429c8b331774a530",
            "0x1918c1c6ee74b13f5253a68b51c8be62dee7c9a7f4adcdb1a14edb69f0a09183",
            "0xa3cc2f162dee2d56dff1ee0574aa02b23c627fc4c86420ce2531ccdb13ad28d2",
            "0x6bb2aa0ee5ac03ec036e2a42929e5aa40e4bc42bcbb23a81ce97f45859083425",
            "0xdf7e66394adac626e04d42e4565ffe6f87dc1f6ffe20da1f43c0f9890e902e5e",
            "0x697f0fc487a2921daa6364193371e4593562027af12913f16a0bfb7e1cc4e276",
            "0x29d6478947bf7cf6cf4645b74e88a4492bcea1840ffaaec9c802226957f93447",
            "0x7f9db68093004518d968a2bb271c94207003788658fe789632a845c59ff57b33",
            "0xe069e7c69b8f25056e1b611a36dcf09f942f5de9a3f93dee53f77c309246abbe",
            "0xcbd5a757e3c80229105999f3d960b1175ae6b762f39c90e76d334bd971f700d4",
            "0xdb3ac14e06f7948d3dd4871851d18d6594393a648c54249358539346866463ad",
            "0x49ecbf57d43f2360c17e6b2a2a9aaaee92c33bec51b2129a572c75175a8fb131",
            "0x71b9406ad30ba1f5854b9308c87e89635c9b547d6e25011b49c6093de782a20b",
            "0xe9650a177983b80f502f870965ccec49a1a0b9203da362fc6fc4061aee571454",
            "0xac7ce69d37074bdab2594d359fd676ad92a5dab79741b759a644fc50cd6198a5",
            "0xdf9484b3674777e15211defa5638c997a6a46904212c0ac5ecf3eb4c04d44c14",
            "0x1d27a4e07c2fb7409e27c1cf54a35523fa5168d384ab9c1b469d16cd27159704",
            "0x6f2c8cae47ca5e63dc1d9384752f426087f4e4e56d5de13a42da341bcf1aea99",
            "0xccaaa558b0bf10968b9ff073de925bc8a108711165768bfd478e06da6356a0db",
            "0x5f4264255da0beccab07229aec9a19b3a484e659452d97d3b67b66571154fa76",
            "0x32c38bbb3983ce1e7b73ee13085e546a2a084668dbc649752272a1a0288130ac",
            "0x2640a290f8932118fc8ff64188f0baa13fcccccbe459693910b0a76db3306c68"
        ],
        "transactionsRoot": "0x50a1945a26c0fc352263d602885b3632498f0f3a28b55b7c187b5507856d758b",
        "uncles": [],
        "withdrawals": [
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08be",
                "validatorIndex": "0x1c2"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08bf",
                "validatorIndex": "0x1c8"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08c0",
                "validatorIndex": "0x1cc"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08c1",
                "validatorIndex": "0x1d0"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08c2",
                "validatorIndex": "0x1d2"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08c3",
                "validatorIndex": "0x1df"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08c4",
                "validatorIndex": "0x1e2"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08c5",
                "validatorIndex": "0x1e3"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08c6",
                "validatorIndex": "0x1e4"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08c7",
                "validatorIndex": "0x1e6"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xefc",
                "index": "0x13b08c8",
                "validatorIndex": "0x1e7"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xb3d",
                "index": "0x13b08c9",
                "validatorIndex": "0x1e9"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xb3d",
                "index": "0x13b08ca",
                "validatorIndex": "0x1ea"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xb3d",
                "index": "0x13b08cb",
                "validatorIndex": "0x1ec"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xb3d",
                "index": "0x13b08cc",
                "validatorIndex": "0x1ef"
            },
            {
                "address": "0x25c4a76e7d118705e7ea2e9b7d8c59930d8acd3b",
                "amount": "0xb3d",
                "index": "0x13b08cd",
                "validatorIndex": "0x1f0"
            }
        ],
        "withdrawalsRoot": "0x8c46071216707584dad7033195481f4fd53b32fde6e3ec8158f19b2350761b52"
    }
  }
  ```

### 3. Find the balance (In Integer) of the account of a given address

- Answer: 3227582331817560200 (Mainnet Balance), 0 (Sepolia Balance)

- JSON RPC payload:
  ```json
  {
    "jsonrpc": "2.0",
    "method": "eth_getBalance",
    "params": ["0xBaF6dC2E647aeb6F510f9e318856A1BCd66C5e19", "latest"],
    "id": 1
  }
  ```
- Response:
  ```json
  {
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x2ccaad07c3500888"
  }
  ```

### 4. Query the information about a transaction requested by transaction hash

- Number of transactions made by the sender prior to this one in the block: 48970

- Value transferred in Wei: 29901491478085619

- JSON RPC payload:
  ```json
  {
    "jsonrpc": "2.0",
    "method": "eth_getTransactionByHash",
    "params": [
      "0xdcae4a84a5780f62f18a9afb07b3a7627b9a28aa128a76bfddec72de9a0c2606"
    ],
    "id": 1
  }
  ```
- Response:
  ```json
  {
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "accessList": [],
        "blockHash": "0x53d920959cf1ee6f569fcdeba03c9d91c54f4c34e893cd937536f7ae8c60be9a",
        "blockNumber": "0x1132aea",
        "chainId": "0x1",
        "from": "0xbaf6dc2e647aeb6f510f9e318856a1bcd66c5e19",
        "gas": "0x565f",
        "gasPrice": "0x4cc13ee7c",
        "hash": "0xdcae4a84a5780f62f18a9afb07b3a7627b9a28aa128a76bfddec72de9a0c2606",
        "input": "0x",
        "maxFeePerGas": "0x4cc13ee7c",
        "maxPriorityFeePerGas": "0x0",
        "nonce": "0xbf4a",
        "r": "0x3c54f1d468465af6d4ad737ca626399a3b8180a510479585873531b5cfe0443e",
        "s": "0x7dc4757678d30c50ce1932c9d0603274cfcb6719c64c0c1603834a43eadbf961",
        "to": "0x388c818ca8b9251b393131c08a736a67ccb19297",
        "transactionIndex": "0x73",
        "type": "0x2",
        "v": "0x0",
        "value": "0x6a3b3f81ce3ff3",
        "yParity": "0x0"
    }
  }
  ```

### 5. Find the number of peers connected currently to your Geth client (in Infura).

- Answer: 100

- JSON RPC payload:

  ```json
  {
    "jsonrpc": "2.0",
    "method": "net_peerCount",
    "params": [],
    "id": 1
  }
  ```

- Response:
  ```json
  {
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x64"
  }
  ```

### 6. Query transaction receipt for the transaction with hash.

- blockNumber: 18033386

- blockHash: `0x53d920959cf1ee6f569fcdeba03c9d91c54f4c34e893cd937536f7ae8c60be9a`

- cumulativeGasUsed: 16298877

- transactionIndex: 111

- JSON RPC payload:

  ```json
  {
    "jsonrpc": "2.0",
    "method": "eth_getTransactionReceipt",
    "params": [
      "0x5d692282381c75786e5f700c297def496e8e54f0a96d5a4447035f75085933cb"
    ],
    "id": 1
  }
  ```

- Response:
  ```json
  {
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
      "blockHash": "0x53d920959cf1ee6f569fcdeba03c9d91c54f4c34e893cd937536f7ae8c60be9a",
      "blockNumber": "0x1132aea",
      "contractAddress": null,
      "cumulativeGasUsed": "0xf8b37d",
      "effectiveGasPrice": "0x4cf0edefc",
      "from": "0x6887246668a3b87f54deb3b94ba47a6f63f32985",
      "gasUsed": "0x1ab988",
      "logs": [],
      "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "status": "0x1",
      "to": "0xff00000000000000000000000000000000000010",
      "transactionHash": "0x5d692282381c75786e5f700c297def496e8e54f0a96d5a4447035f75085933cb",
      "transactionIndex": "0x6f",
      "type": "0x2"
    }
  }
  ```

### 7. Find out the number of transactions in the block with the given block: 0x1132aea

- Answer: 116

- JSON RPC payload:

  ```json
  {
    "jsonrpc": "2.0",
    "method": "eth_getBlockTransactionCountByNumber",
    "params": ["0x1132aea"],
    "id": 1
  }
  ```

- Response:

  ```json
  {
    "jsonrpc": "2.0",
    "id": 1,
    "result": "0x74"
  }
  ```
