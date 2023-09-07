## Part A

### 1. Query the current gas price in wei

- Answer: 919
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
    "result": "0x397"
  }
  ```

### 2. Query the current latest block number (converted to decimal)

- Answer: 9653078
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
      "baseFeePerGas": "0xa",
      "difficulty": "0x0",
      "extraData": "0x506f776572656420627920626c6f58726f757465",
      "gasLimit": "0x1c9c380",
      "gasUsed": "0x3cb181",
      "hash": "0xd24b6e5d306d762e126205aaf51333240fd840585ac4229fa05c52fdfc187ba7",
      "logsBloom": "0x340080200040d08000504012081000040028014294140040004600000051000014040470008008220011000810048ea800c2252005000a0102901604102020044010010c66040080c888230a400280260400204452023802881101044008002030108108128800c0010810000004080c003840c100824008000a0118000001c10608208001814c08602c40000120040c4001008012000000218f041004032014522c480890014005022010260280030c140001120008018400e10822208100010280400701817209030804010c1212180560000402892a000002042060102000c0100209200a00810020000020000c04128144101900800140080a0428000280",
      "miner": "0x8dc847af872947ac18d5d63fa646eb65d4d99560",
      "mixHash": "0xdea32c258822201f7b99a2f0d9cd03a0fd44c7786fc5a21471593007e11a4d31",
      "nonce": "0x0000000000000000",
      "number": "0x934b56",
      "parentHash": "0xca31215e8f86c48f9187e97636bfeaa3baa7c97c92ea07b2e2e53c836d8d0d05",
      "receiptsRoot": "0xfa955dd6424a8fb0f04ba21d27c9922b89e89b75710cf1b6cf3037b8b0af89d1",
      "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
      "size": "0xb642",
      "stateRoot": "0x1ae11b3b5a20e099fdfcb0c4ea129b8c641ca02613e6568d9bb89a0854ec4a4a",
      "timestamp": "0x64f9d700",
      "totalDifficulty": "0xa4a470",
      "transactions": [
        "0x372aaa39210c61014c5a0c60fcd5594785f67cf308e32b94fe3445c29d4e734e",
        "0x40b584b0d935d80af0905290a38c4d962dd2f199e651f4a45300d4f3e8edaca8",
        "0x54a67a1945db6a4e0415c977918f5d15d599db129d1a0755cac1ef1d59e49fd7",
        "0x5c04020dcb56300bc295b749a79f4b3edb65fa8bfa2f30cbaeeeb5c9b67a5c1a",
        "0x0e8788a2df672d394a54765b808ab5ed94e48eea8fd9fd7f08b0e336e2e8aa57",
        "0xf1a36c9f63540c580c30d6f7dd3a721add92aa8dc7b157d402eb3694271999e0",
        "0x615a8ba1f1d63eb5aaae509cedaff1592158f7f4d62acfe9af9fc664b7eecf91",
        "0x3b80f53a09aad8a7b2ed58bd640890c14ab6cecccd54f14d47709b0ee7cf4af0",
        "0x997c0b2f605195b70cffd3de89726430466541198a8bf51f4bd3f1d479dea7ef",
        "0xeb9f0a368e9c3371200b199516273a76c5dea67b4587db87bdce26f58fa164ba",
        "0xb309ed7eaa937f0caf51c9b4f9fef53a8e4dfc4dbea2cdf8ddedcfcabdccf25a",
        "0x667e4e1490bf2b733da69b748b53b3424eff36d5ae1bb5d094c65580e79efa2d",
        "0x99d4107c1a3d7a5f99ac142c969786c9392a7644a6708d6f3dcaaf225b5d412b",
        "0x6b155cb4af437674a0eceedd83e33ec61864b7c2a259b44d4dfe1125793e0ec3",
        "0xfa356deb422c05a5e4b9f9a81d18196ebe6572b3be308e7a9a959639afbff8ef",
        "0x72f74f2d4bbb3a38f0276a9d87a923c48a733693bb8a4c3f741c4f52787c57d8",
        "0x5a4c61c5c8a1dfa9ec6f5c1b1192e32874edaa78c78af4c79eedb54a7902b4ad",
        "0xf5c90a946c15c8e50105f72a4b3b60bb6cbabe4bdbbe98c2a03fed7ebe7edd24",
        "0x019ebcdd23e4eafdcce26d7dbd0bf22e64b621ee099ded1ede884e83ad2b4c7c",
        "0x7ddde0a0dc00335616fbf0dd77376c9c9fdb305e93304568ba93cbcb87372bce",
        "0x1ddf408ef575cee945d8920793e69046d34c86852a092905e42821aa6625d74f",
        "0x6d9e264ae337fe8999eb310855adba860f4c02440e5e792a84316bb35109c877",
        "0x491da2a74f1ba44b1178de9c0cd46a3a4d3bcf1d25b4c3172183488e2f3b8ef9",
        "0x93eb36f7ac6e621ca15569ff5b9eb78222b31700f8a50c4e3e15a2062c797b5f",
        "0x858995f3cf42fe873959a767a75d025d501d0c2907c5a071371c4ab263d340c3",
        "0x91df7b846092da62ed09ed09e8b153f29bde5e1f7a981f04c56007f5e89e2a41",
        "0x871236a1a2fc47ecfe76eaa655d824aade7f022454975e913e6e4689617bc130",
        "0xf3b6c39b5850f402b263d6e34c77b71b70013c93e3ba75040b220e5f3ea9f2f3",
        "0xea3c5c2d2d9748c5bbd9e750309cd72d29631357254861bdc60cf85a98c4a32b",
        "0xe582b15e80e04638e0ad1f911d3814a156182dffe6c23b9f785a7a68e994ae22",
        "0x8cffe57cb3c0011a34ba682b7073ddfdb77a2d02f462e3fe5c992ad7e490f94c",
        "0x31f9f508e70b7ff054d0cbb9b8d29a03244f28d55b67a9d5b7283002e8e3cbdb",
        "0xb3137006ac2f338aeb9c0a4b1a4f9e26eb20d116f2f577391b56eb8e47c28ed5",
        "0x64c859bf59ccc90141f2fa203b8e94951e47735f44e04e8a6249172303a51cfa",
        "0x7b94f8b28bb5791b681b630a6d02f7a35b81176db711d3e50e3b4fe51ff47113",
        "0xb6d1c59d4ba59c4e631edab0769d25a464a88aece5040954d1911dfde12b5d17",
        "0x29fd73c3366df1b10471568fd48e5db3b2dfd498593c64ddf0653be166585d47",
        "0x8dd78fffa11f741694d322fd4875c26bfbf69f27b529d1406ef8d2db0a8fc571",
        "0x6355b166054a947e54fade220552cdfdfb6c9bf52869fd785be0a14ed5fd0c72",
        "0x7408c4d540ace228cd7816c861a679bd83de3b100c1ad7da0b2c07d5a1b97c68",
        "0xd1287821fea422f820951bef751e29343a44f5bd72ddc9e7b797c86a37085a94",
        "0xb668ea5f352e3104950c56f202bec9c2a0ca42af5924c106f0adb591d339c948",
        "0xff4121e78149b4669f4ab8dafc6b75ab624b814882133960b54a1047437c3508",
        "0x46a8180f7d492a50bc0eb33b86ac3485fdcde696800f51251df17d88627ea1bd",
        "0xabccce4f56416ceb47199c588945a025986ac5e34b8f1ecc3c2b2c80eeb6e4a7",
        "0x8ae0d6b65b4fc730b5d4a129857ecfbfcaefd961f911b54d0450c11df20c8b3d"
      ],
      "transactionsRoot": "0x0d1d2d1df49dbc37f981b47d53458711f33f2449157e610ffe6ef2ae7f912a64",
      "uncles": [],
      "withdrawals": [
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2f1020",
          "index": "0xf2f3ec",
          "validatorIndex": "0x79575"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2efd43",
          "index": "0xf2f3ed",
          "validatorIndex": "0x79588"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2e6045",
          "index": "0xf2f3ee",
          "validatorIndex": "0x79589"
        },
        {
          "address": "0x000000005504f0f5cf39b1ed609b892d23028e57",
          "amount": "0x1bae9c6",
          "index": "0xf2f3ef",
          "validatorIndex": "0x7958a"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2f44f6",
          "index": "0xf2f3f0",
          "validatorIndex": "0x7958b"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2e8a02",
          "index": "0xf2f3f1",
          "validatorIndex": "0x7958c"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2e83e7",
          "index": "0xf2f3f2",
          "validatorIndex": "0x7958d"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2dce9c",
          "index": "0xf2f3f3",
          "validatorIndex": "0x7958e"
        },
        {
          "address": "0xad09d80bb20627ce9e394b17e67f46aa0a6420f1",
          "amount": "0x2f0037",
          "index": "0xf2f3f4",
          "validatorIndex": "0x7958f"
        },
        {
          "address": "0xad09d80bb20627ce9e394b17e67f46aa0a6420f1",
          "amount": "0x2f011b",
          "index": "0xf2f3f5",
          "validatorIndex": "0x79590"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2e8032",
          "index": "0xf2f3f6",
          "validatorIndex": "0x79591"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2d23d7",
          "index": "0xf2f3f7",
          "validatorIndex": "0x79592"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2d3903",
          "index": "0xf2f3f8",
          "validatorIndex": "0x79593"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2d9815",
          "index": "0xf2f3f9",
          "validatorIndex": "0x79594"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2d93fd",
          "index": "0xf2f3fa",
          "validatorIndex": "0x79595"
        },
        {
          "address": "0x45085d65eaee8792357aef01d1c0eb8641ae09c5",
          "amount": "0x2e623b",
          "index": "0xf2f3fb",
          "validatorIndex": "0x79596"
        }
      ],
      "withdrawalsRoot": "0x705b5b140ef4f948e541c47fe846240ab7a950a86e244395dc77d91334894b33"
    }
  }
  ```

### 3. Query the current latest block number (converted to decimal)

- Answer: 1141819585802838800

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
    "result": "0xfd88edd195ca310"
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
    "params": ["0xdcae4a84a5780f62f18a9afb07b3a7627b9a28aa128a76bfddec72de9a0c2606"],
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
    "params": ["0x5d692282381c75786e5f700c297def496e8e54f0a96d5a4447035f75085933cb"],
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
    "method": "eth_getBlockByNumber",
    "params": ["0x1132aea", false],
    "id": 1
  }
  ```

- Response:
  ```json
  {
    "id": 1,
    "jsonrpc": "2.0",
    "result": {
      "baseFeePerGas": "0x4cc13ee7c",
      "difficulty": "0x0",
      "extraData": "0x4d616465206f6e20746865206d6f6f6e20627920426c6f636b6e6174697665",
      "gasLimit": "0x1c9c380",
      "gasUsed": "0xfbabbf",
      "hash": "0x53d920959cf1ee6f569fcdeba03c9d91c54f4c34e893cd937536f7ae8c60be9a",
      "logsBloom": "0x09efd652f50b706c59e280e1e21c5de3b0254bd8cdddefd1044b60e322f20d620c6dafcdeb0edfc4d5b407239055fd152e8c19458820ad10754ea86683b4c5aa614f9d8d7dbcd87bead3eb2e88893234cc3945af905c5858a1ba92a7a7f64bda1455c8697a07d75f899db4add441181ba419ce72bdb13f804ed86a7b8b8a4eec6e9884ae6337511bed6997c219e266fed71dd5ab79009f7e86352c69dcb086309bb7677413a82c92408e42f17ff6ad556a679404ec2ba30e63c2aa2371feb21c4fb846b2b0874f85a2e83ae704c7a9d536f98a097d2d27308675238a2d7ce42c5058a5dd755609cc65de1be26ae4dba2a172d22b5f5d117609349d836b994eeb",
      "miner": "0xbaf6dc2e647aeb6f510f9e318856a1bcd66c5e19",
      "mixHash": "0x721d4d1abe562f4cc19683beeecac0dcf8ec7aad16dbe2bae0827b1e99fb8043",
      "nonce": "0x0000000000000000",
      "number": "0x1132aea",
      "parentHash": "0xeeb19e2af95b5e8dae6835e40e8450c6e4fbf9b59c44d5222c23c0580dfa34e6",
      "receiptsRoot": "0x1f3bff61e72eb14a903b4eef09d2d0f07ce1bcd7c24275808a1b849cab373c7b",
      "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
      "size": "0xa05d0",
      "stateRoot": "0x629cacd9ade5b461db3a4a1570174b3fcf1014d0d2f971c6a9be24dddb6411ae",
      "timestamp": "0x64f05053",
      "totalDifficulty": "0xc70d815d562d3cfa955",
      "transactions": [
        "0x21039516b3b688ea647873885fe50bf0bc41f38bf597baeaeabc6853eab45bc5",
        "0x2c987feaeb98f97903acc901a364928687f9b956f5775f3129a589846d9ecd57",
        "0x443242ae9919a13a69ac3df69e3a580aa976feb5713294030b7bc1112c7039fc",
        "0x41573baf88f90f539fb4d7278b8f95b6a04e3412be7354944b85ebd65aefb212",
        "0xffae8c48a3dda9956230beec3e9970f8df21827428810cd2352375d0ab137249",
        "0xc18d7d6a45f07e924c54e2ea4b3ef3bd357ff5f62e9750b092afed2a15ce3d47",
        "0x111531add2c28e914ad93b4aeb8fd8e666ec5b541b7cec03b68f90af5ec550bc",
        "0x5c9d435154fae55984016f53af12355c2fef0a214cbe0fa1ce0b5dfc19e3c92b",
        "0x0b29f515c5f756fc15922c5880a80ef0a00704ae50c045e7499cf21f8fee5be4",
        "0xe1625056fb7eabe545cc4136508a165456a98f790246b9efdcafb711ea4c188c",
        "0xdf5ae9d50cb48cb717e98b0494cbaae243ce7009edfe8056615e4ae53cd01120",
        "0x7a5dfc3b8f67dd3debe84984c857ecf53274b232cd4c44e2dd94867331411a99",
        "0x3ee248ffdc99bbcc73e4a733f4979961377c0e58654a69b10fb0ea0d8695fe75",
        "0x6869b5c831b988eb5bfae3714bb16a22ca8676a3d185cc1c08d2af0ecb205fb4",
        "0xce5facda894c303022b558930c68909f30cd037307cae91b808773cb245ba8cf",
        "0x7cd502cd6d2c72ac598db51725b5ed87fe8746d337f6c4dd93ed280bc23efa6d",
        "0x1176e3a1147ee6c15af23d3753bf495d3f060ae5ef86c7c3fcb964c05be40dea",
        "0x975e23829e5d2a8c4b9543c09c2017baaf25d3e98d6cf9af1ff9b2f19b3a3be3",
        "0x93bc9ff2b5046aa9c15d27dcd5d4074a7c902b1a5158b5965ac6bf511d483d86",
        "0x16cab89ae85aa61a72a8d69fee65b9b2e94057fa8d270e2bde7b8a33dd810dd9",
        "0x92e1c8a38a72878639a94eb2e304ddbbaa5610a5ae082699d75a33fd1effab69",
        "0x9cff2b7548fe7ed636a5bfe8ecb4070e1ea1ccb18c024e55ba76be708a5b4fc2",
        "0xd95c041e9d0e6539c9b7335e994bd0a380e9ae38aef17fa2ee34c1f48493e6f4",
        "0x306c98e071b93ab9e4c5ee2aff7d6a5fffbde3dab5ef1bc7055c8d6d3d4d1177",
        "0x307980eebc4d3b171b038fe57073f7dcb1b6206f65bf1bb948ff62a0c3eb1534",
        "0xcc55743932d38b02a020431ca412ed897bbaf7b9cf2d20086b11163e394fa288",
        "0xb4ca4735d580bdd8eaf81eb10452c3052f196d6423ac55e65b7d1041b4c6ff23",
        "0xc2d8ae2132b6ea827077f584a6d907fc6f9fe89e347f0d5e5c84f8651777ef5c",
        "0xed4448708c0d0580918649d97481b4ed47e7136b470243285755967963790c44",
        "0x1481fe4a7eb23912c5ee457b8ac1a09e39993f481d4176057930699013d63376",
        "0x497c74ec07f34e81e3c8d97d626b3b6c2c2bcd03cecbdc54185c3f3035b23ab6",
        "0x52d88495eef75d818022cf03754998e9aa0f5a606af9adbf5563ecc18d7a9a14",
        "0xde9a6629801730f0e60cc19d1155eccff444883c0ffacd6d1edf48abf5377c7a",
        "0x5e05a89614e90c799957d889a551b47500eaee0f705fc2843165fd79c8643e8e",
        "0x1761e16ce23dea3a49162c7c2b123126f78c76657cf16d4b1394b367f7812524",
        "0x5b6d05f76c86bbdcaa8bc2c735b78e376b34e2aa493a71a678851ea3888554f9",
        "0x21746e5303813c0f8724e68a70061842436102ace37ee884f76efca091ace18d",
        "0x2de66c175b4e909fca70064cc605c3b2195431ce33c4bd74f0fb26dde7a302f9",
        "0xab05cb54177b52e30d0a7e9cdb6021fdb38bd7524f293ef409e5bebe7bdd52a1",
        "0x647093e316ae5521f6272db4af2bfb79472574322559cb7ef2c6735e715d666a",
        "0x961a5622e6e2ee4bcf9d65786f7c68151e02a6cd9469cd51f8402950bda93e7d",
        "0xfce3a2eda6c7b8ce69ec3ba76b9446c11ff4adda9f25e72b6942b3465d68689c",
        "0x924a15dc40d3e03a2082b3e0edca1f616eeff07f07cf24c2cbb803d204913854",
        "0xcd1b69441f83b45f2a9f252f1ae283962a09c61d111e4676870bf57b75317f46",
        "0x28493845d05e087f0aedea52e8bd1b00acf7275653cc2c2d05ead6d743ffbcbd",
        "0xf6c567be6ec3b7ad6064be42e04afaeb1dddc27acc52dd38e849b9de573fb9a4",
        "0x281aa7fb89c3990f22ba3cd7d4f363922267d66121cfedbeeaff7f914e7f8271",
        "0x3596be220ca66d862ba4e7c8a3de01ff3afa32731affde0b581f7c83e77f6992",
        "0x727476bd711e4ef4556690714a4c941f5d964fdaeb87f2caf377888b87d4c70f",
        "0x7181d29b37ef527afd91f5e499c51a2c366537a76fc6fe795b0b969ca29df024",
        "0xc35dc9d2e6bc7084d587162bd0a741215c1628d0b0cbfdcadb2e2bd3e6f3ac9e",
        "0x8005f7dc35fd17391c693c73cff38f92ea52e2127bd96861f78f08d3582cedbf",
        "0x994c77f102b1c1bcb07afdb833b4ce9b96c1bd03b87d98bfc210f8f3b4e29687",
        "0xe46d996e86e19e7a6034434ff6d88cc0499369eb93f007a6d5dac24d4453c70d",
        "0x40050a5afececd2ce2cda20a6d573bdd12120fcaf857d2f24260d443106e982c",
        "0x2c86ed0c1dfae3be07dae70f337a2b197e940189fb1ca13126fb5b3cbc6cca05",
        "0x4e466f7a8df6bafea37c8caa6284537927f269e5845561dca7b063e83f47f64a",
        "0x9df4f5f567399e1973557b2fa7274393c22a7e274af35ab0e3320cc7a69f32e0",
        "0x8f623df69d027c9d2440da3d9a36d0473d04c9ce2a28b105e5d3914adebdfe3c",
        "0xc025d09c9f03136f112531b5784d83305576b060ad72f1a8721c193e189d91b3",
        "0xeb510a40565cf5871cac499f1e9bdda69cddb6179366f353cd61a30394167c8f",
        "0x0c413be6cb8d8b2be3ed72c5ab6b7997bd33b244fa54d91fa292f7c38fddce6a",
        "0xd9d9e8805b21dd9a72daa8a6a03a20eea769a70a3e9a0a4063566da91bc48caf",
        "0xe636792f819ec3e5a2760aab43437200833b27f5455554da3051e30cd3a0ebba",
        "0xb2c73a50cba2426a1cb8d47bb0cdbccd1a1ae4a6991d975a24a63d3b0153089e",
        "0x29c2357dc45b1e1eb5a1ea5a3c2923909fa2e64cef5f3ba1b3c57c31de023d1a",
        "0x184c7dfc19d607d85cf3a7185b1948323cff17121793ac06781df47523343557",
        "0x0a1818d45ff97aa61d073d37b7d1c5423468f6a4640f75113195502dd9fd068c",
        "0x6a91092fe38f12f92f984299972efe288c1693e3eb10d29678fa7dae55a8e040",
        "0x2dcd4e258270686b1d9de3b8535d85a4431df811d1774617dadaf9d90d497c30",
        "0x6b0a8f3e55dd3ee7fbca62038d3024de4f437e89445a1891b59e54d68ddfb05a",
        "0xd4bd7b4574ac970d363c12bc96de6a53b129dda97022e4244abf2fbb038edb83",
        "0x20978303c10212abe06944a2dfcb97df3b3fc7916211ff56608939ec26070281",
        "0x457274c0fe79337988f6bd41b5e48dac78f9de8adefc27b148a326ad7a3f0234",
        "0x80a16394dbd18cbcadb5b27edbdf329b353a43acd45982f50ac4046d2080d588",
        "0xd0b9d072bd883f12d08112d9c08ffda6f1efb2069499579a7be9dab14b65f4c7",
        "0x714027545d26b573f08be72523e357733e8d2068791faaf7ea681eec010c2b84",
        "0x7137080f13ccfc42c9199323ed20ed3f55439a86832139736d8605ecf7bceeed",
        "0x1924727e52d45fb8afee199fcde1c60dac3994485e2e944d066f9bbfe46f18b7",
        "0xa538b5ac3397e85610e8daf394b3a9f3ae623d6558479e69ce79689c4dded70b",
        "0x78c900e897735e2574fa2561fbb8a6ac668d017a18e010b68cddebc31da266df",
        "0x23541cff9e8a7ade1dd8b1a0af89e2bb4083d477c7912e6d36ee836e58bd4763",
        "0xe5eb9d561bfc3df93ba32e80e234673b42cad79c13390173d7b437aadaee5bcf",
        "0x2e14305363ae9805437d6b1e147d92046d019a315879261eddeec97115aaa887",
        "0xeba6789f70c09e1bd034783d03caa69bbc4be21348e43f8f260f1234bc0a9b83",
        "0x6a3b4d0ba5b42fcf3d22eab20a4210f132f216f86e9c5aee87dad2982699a7c4",
        "0xed934af3a24fc021c88dd1d8b9145ca14a31c8826eb98a3d81a5814f7094b846",
        "0xd4145bb9ea4f62e06cc8893997a35bce33ffcaf163d71eaccf78b04ca043415a",
        "0x2c76869360a4b55ceac959e2e69084ef6bcad8f97633999122dbc6d1c3297faa",
        "0xc427faf786488d73ab352369346013618a0bb9cbfe0eab607cf4b9b912ec7bf5",
        "0x4f74e3b7ac306a3b161a764095ec50a53f2c5a4da604f9d0c526aa45df83e88e",
        "0x1b2eb6aa4742964776349e516a08b0cf204ff1d42c2057e31965768f0eec55ad",
        "0xe71b36a8c7e496b1d853cddb29ee4a76d1561bcf58a8e30f87a9b2f3f08ec1d0",
        "0x42440d9f1a4214066e607f18d2036c6e516dc8d16134c7daf67528426569fdfe",
        "0x855b3838e280f8a1cd6dd930c8c7beba6a38c9de65ae148e95863c1f90ca4c24",
        "0xde15bb644d9aff4be60cfb76c2a76b952da8aab28997a698a9c4a7c974bb32b7",
        "0xc8705e0fd0791cafe458a6d08b4724f9f24443086ab6aedff937edc22d54c31c",
        "0x3b4acdff0f9ae1a1533063c78026329a63e818b791dea2b83f59bf36de32252f",
        "0x3cb98d033ae2bfec8b7c3a82c5925e3f61f9ee12e194c33ed46d9b18e93ccce8",
        "0x52f8d88569db8cbe3052ad1e87e093408cd9ade9fcdb4f1c03e3249bffa17f7b",
        "0x8895bc2f421aab5a099298b12c7d329f7d1a6f971b2769903ed26881454c78d2",
        "0x9e68e390330b9d9ef53308a88628a63e133da89d11ed827f051245f2522a332d",
        "0xbae89e39581394cebba683f0133d66dc727fd8f54ff3bfb331ad82af8a2c3cec",
        "0xf29a4f9ef1a2446001df58f5f2d170c829518b383c51deefba476f9e696dbd44",
        "0x860ac0db2a13853a29bd71e1e05aacd8f712e00bc65b9545879a3d8c7de714c5",
        "0x7705a9072b2e79b4036cb93aabd96df99b12967c8e322bee26707f89e2045c54",
        "0x196d84bdd92ee5068797926237ca5033cec2921671c85490a4117d9298e21171",
        "0x20e60c45f358882e7722aafbbe494ecd6d0c292b25717763d4af43aee13c9c1c",
        "0xe55e52b5070361e1d5ec224f421a3dbc2071b4c2900b19ea1c72b7b5fc9432e7",
        "0x32df88dd7e40636b587e17881a07c6b597db314de166bfc43568bc1848445105",
        "0xff60dca1ab0c683e8f80630535efd62a4f9e9dac307f441c1d823aaa6cd382fd",
        "0x5d692282381c75786e5f700c297def496e8e54f0a96d5a4447035f75085933cb",
        "0x0e2cdc2e8e987ea0c4b9053f832c813b60911f0667af3e200d7f67187d918afb",
        "0xf9fbf5711498335384e9516f27dccfe947fc10dd2a4c6222a93c7fa3fb3cd357",
        "0xa0bb3f1b5aae5a3c5f16a98d8c508c2db3aa5318fe68d9ddb014ca0593b4607c",
        "0xdcae4a84a5780f62f18a9afb07b3a7627b9a28aa128a76bfddec72de9a0c2606"
      ],
      "transactionsRoot": "0x366b2896dcebd63be94d9e47c8be84fba2187c9d1a780f1462df478ac1cec3ea",
      "uncles": [],
      "withdrawals": [
        {
          "address": "0x210b3cb99fa1de0a64085fa80e18c22fe4722a1b",
          "amount": "0xed41f0",
          "index": "0xf3c201",
          "validatorIndex": "0x71d99"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xee18d2",
          "index": "0xf3c202",
          "validatorIndex": "0x71d9a"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xeeafef",
          "index": "0xf3c203",
          "validatorIndex": "0x71d9b"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xee7197",
          "index": "0xf3c204",
          "validatorIndex": "0x71d9c"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xeebb12",
          "index": "0xf3c205",
          "validatorIndex": "0x71d9d"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xeee5d9",
          "index": "0xf3c206",
          "validatorIndex": "0x71d9e"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xeee7d2",
          "index": "0xf3c207",
          "validatorIndex": "0x71d9f"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xee52aa",
          "index": "0xf3c208",
          "validatorIndex": "0x71da0"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xeed07e",
          "index": "0xf3c209",
          "validatorIndex": "0x71da1"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xee5933",
          "index": "0xf3c20a",
          "validatorIndex": "0x71da3"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xee4e9c",
          "index": "0xf3c20b",
          "validatorIndex": "0x71da4"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xeea4f8",
          "index": "0xf3c20c",
          "validatorIndex": "0x71da5"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xeea4d9",
          "index": "0xf3c20d",
          "validatorIndex": "0x71da6"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xee4fd9",
          "index": "0xf3c20e",
          "validatorIndex": "0x71da7"
        },
        {
          "address": "0x4b5e9a6ab1b87d4df850178ad2807c1e3e3ba33e",
          "amount": "0xee452e",
          "index": "0xf3c20f",
          "validatorIndex": "0x71da8"
        },
        {
          "address": "0xb9d7934878b5fb9610b3fe8a5e441e8fad7e293f",
          "amount": "0xe0b164",
          "index": "0xf3c210",
          "validatorIndex": "0x71da9"
        }
      ],
      "withdrawalsRoot": "0x8e5ac4698f872ddf40a4b9aaccebcb6090d8e7ff64c510a4ecd5b5556c45bbce"
    }
  }
  ```
