//SPDX-License-Identifier:MIT 
pragma solidity >=0.5.0 <0.9.0; 
 
contract EtherWallet{ 
    address payable public owner; 
     
    constructor()Payable{ 
        owner = payable(msg.sender); // by default msg.sender is not payable so we cast it    
    } 
 
    function Withdraw(uint _amount) public { 
        require(msg.sender == owner,"Only the owner can invoke this function"); 
        payable(msg.sender).transfer(_amount); 
    } 
 
    function getBalance() external view returns(uint){ 
        return address(this).balance;// return balance in this contract 
    } 
 
    receive() external payable {} // default function came after sol version 0.6.0 that allows 
contract to receive funds 
} 
