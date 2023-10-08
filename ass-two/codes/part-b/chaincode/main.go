package main

import (
	"fmt"

	"github.com/hyperledger/fabric-contract-api-go/contractapi"
)

// SmartContract
type SmartContract struct {
	contractapi.Contract
}

// InitLedger
func (s *SmartContract) InitLedger(ctx contractapi.TransactionContextInterface) error {
	err := ctx.GetStub().PutState("testkey", []byte("testval"))
	if err != nil {
		return fmt.Errorf("failed to put to world state: %s", err.Error())
	}

	return nil
}

func main() {
	chaincode, err := contractapi.NewChaincode(new(SmartContract))
	if err != nil {
		fmt.Printf("error creating chaincode: %s", err.Error())
	}

	err = chaincode.Start()
	if err != nil {
		fmt.Printf("error starting chaincode: %s", err.Error())
	}
}
