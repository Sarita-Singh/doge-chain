// SPDX-License-Identifier: GPL-3.0
// Contract Address: 0x67dE01266bC186Bf8EF48209265d90676d0e73f9
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
        require(msg.sender == seller, "You are not the seller");
        _;
    }

    function buyTicket(
        string memory email,
        uint numTickets
    ) public payable soldOut {
        require(
            msg.value >= numTickets * price,
            "Transaction value should not be less than total price of the tickets."
        );
        require(
            numTickets <= quota - numTicketsSold,
            "Requested number of tickets not available. Please try a smaller amount."
        );

        Buyer storage buyer = BuyersPaid[msg.sender];

        if (buyer.numTickets > 0) {
            buyer.numTickets += numTickets;
            buyer.totalPrice += numTickets * price;
        } else {
            buyer.email = email;
            buyer.numTickets = numTickets;
            buyer.totalPrice = numTickets * price;
        }

        numTicketsSold += numTickets;

        uint extra = msg.value - numTickets * price;
        if (extra > 0) {
            payable(msg.sender).transfer(extra);
        }
    }

    function withdrawFunds() public onlyOwner {
        uint256 totalFunds = address(this).balance;
        payable(msg.sender).transfer(totalFunds);
    }

    function refundTicket(address buyer) public onlyOwner {
        Buyer storage refundBuyer = BuyersPaid[buyer];
        require(refundBuyer.numTickets > 0, "Buyer has no ticket booked");
        require(
            address(this).balance >= refundBuyer.totalPrice,
            "Contract has no funds left. Cannot refund"
        );

        payable(buyer).transfer(refundBuyer.totalPrice);
        numTicketsSold -= refundBuyer.numTickets;
        refundBuyer.numTickets = 0;
        refundBuyer.totalPrice = 0;
    }

    function getBuyerAmountPaid(
        address buyer
    ) public view returns (uint totalPaid) {
        totalPaid = BuyersPaid[buyer].totalPrice;
    }

    function kill() public onlyOwner {
        selfdestruct(payable(msg.sender));
    }
}
