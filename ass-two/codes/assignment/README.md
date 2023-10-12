Required Directory Structure

```
.
├── assignment
│   ├── README.md
│   ├── part-a
│   │   ├── application
│   │   └── chaincode
│   └── part-b
│       ├── application
│       └── chaincode
└── fabric-samples
    ├── test-network
    │   ├── network.sh
    │   ...
    ...
```

<br/>

Setting Environment Variables (run this inside `fabric-samples/test-network` directory)

```bash
export PATH=${PWD}/../bin:$PATH
export FABRIC_CFG_PATH=$PWD/../config/

export CORE_PEER_TLS_ENABLED=true
export CORE_PEER_LOCALMSPID="Org1MSP"
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
export CORE_PEER_ADDRESS=localhost:7051
```

<br/>

Network up

```bash
./network.sh up -ca
```

<br/>

Create Channel

```bash
./network.sh createChannel -c doge-chain -ca
```

<br/>

Deploy Part A

```bash
./network.sh deployCC -c doge-chain -ccn part-a -ccp ../../assignment/part-a/chaincode/ -ccl javascript -cccg ../../assignment/part-a/chaincode/collections_config.json -ccep "OR('Org1MSP.peer','Org2MSP.peer')"
```

<br/>

Deploy Part B

```bash
./network.sh deployCC -c doge-chain -ccn part-b -ccp ../../assignment/part-b/chaincode/ -ccl javascript -cccg ../../assignment/part-b/chaincode/collections_config.json -ccep "OR('Org1MSP.peer','Org2MSP.peer')"
```
