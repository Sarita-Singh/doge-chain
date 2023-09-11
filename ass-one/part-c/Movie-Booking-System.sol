// SPDX-License-Identifier: GPL-3.0
// Roll Numbers: 20CS10020, 20CS10053, 20CS10031, 20CS10058

pragma solidity >=0.8.2 <0.9.0;

contract TicketBooking {
    struct Buyer {
        uint totalPrice;
        uint numTickets;
        string email;
    }

    address public seller;
    uint public numTicketsSold;
    uint public quota;
    uint public price;

    mapping(address => Buyer) BuyersPaid;

    constructor(uint _quota, uint _price) {
        seller = msg.sender;
        numTicketsSold = 0;
        quota = _quota;
        price = _price;
    }

    modifier soldOut() {
        require(numTicketsSold < quota, "All tickets have been sold");
        _;
    }

    modifier onlyOwner() {
        require(
            msg.sender == seller,
            "This function can only be run by the seller"
        );
        _;
    }

    function buyTicket(
        string memory email,
        uint numTickets
    ) public payable soldOut {}

    function withdrawFunds() public onlyOwner {}

    function refundTicket(address buyer) public onlyOwner {}

    function getBuyerAmountPaid(
        address buyer
    ) public view returns (uint totalPaid) {
        totalPaid = BuyersPaid[buyer].totalPrice;
    }

    function kill() public onlyOwner {}
}
