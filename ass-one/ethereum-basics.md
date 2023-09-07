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
