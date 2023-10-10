# Part-A Execution Steps

1. Install Hyper Ledger Fabric\
\
2. Start the network\
`cd <Directory where fabric is installed>/fabric-samples/test-network`\
`./network.sh up createChannel -ca -s couchdb`\
`docker ps`\
\
3. Deploy chaincode\
`./network.sh deployCC -ccn shra -ccp <Directory path of source code>/part-a/chaincode/ -ccl javascript -cccg <Directory path of source code>part-a/chaincode/collections_config.json`
