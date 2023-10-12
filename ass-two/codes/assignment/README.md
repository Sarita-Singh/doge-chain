# Required Directory Structure

```graphql
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

# Setting Environment Variables

Run this inside `fabric-samples/test-network` directory

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

# Test-Network and Chaincode Deployment

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

<br/>

# Running Application

- part-a directory: `assignment/part-a/application`
- part-b directory: `assignment/part-b/application`

<br/>

Installing Dependencies

```bash
yarn
```

OR

```bash
npm install
```

<br/>

Generic run command

```bash
node index.js 1/2 <action-command> ...args
```

1 runs the application as client for Org1 and respectively for 2.

<br/>

Examples of commands common to both parts

```bash
node index.js 1 ADD_MONEY 50

node index.js 1 QUERY_BALANCE Org1MSP

node index.js 2 ADD_MONEY 2000

node index.js 2 QUERY_BALANCE Org2MSP

node index.js 1 QUERY_BALANCE Org2MSP

node index.js 1 ADD_ITEM apple 3 60

node index.js 2 ADD_ITEM maaza 1 20

node index.js 1 GET_ITEM

node index.js 2 GET_ITEM
```

<br/>

Examples of commands exculsively for part B

```bash
node index.js 1 ENLIST_ITEM apple 80

node index.js 1 ENLIST_ITEM orange 70

node index.js 1 ALL_ITEMS

node index.js 2 BUY_ITEM orange (this command is meant for debug purposes)
```

<br/>

Verbose Logging On

```bash
export DEBUG=True
```

Verbose Logging Off

```bash
unset DEBUG
```
