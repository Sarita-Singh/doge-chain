# Part-A Execution Steps

1. Install Hyper Ledger Fabric\

2. Start the network\
`cd <Directory where fabric is installed>/fabric-samples/test-network`\
`./network.sh up createChannel -ca -s couchdb`\
`docker ps`\

3. Deploy chaincode\
`./network.sh deployCC -ccn shra -ccp <Directory path of source code>/part-a/chaincode/ -ccl javascript -cccg <Directory path of source code>part-a/chaincode/collections_config.json`

4. Export Environment variables\
`export PATH=${PWD}/../bin:$PATH`\
`export FABRIC_CFG_PATH=$PWD/../config/`\
`export CORE_PEER_TLS_ENABLED=true`\
`export CORE_PEER_LOCALMSPID="Org1MSP"`\
`export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt`\
`export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp`\
`export CORE_PEER_ADDRESS=localhost:7051`

