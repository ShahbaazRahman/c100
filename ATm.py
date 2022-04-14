class ATM:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def Checkbalance(self):
        print("Your Balance Is 5000")
    def Withdrawl(self,amount):
        newamount = 5000-amount
        print("You Have Withdrawn Amount"+str(amount)+"Avaiable Balance"+str(newamount))
    def main():
        CardNumber = input("Insert Your Card Number")
        PinNumber = input("Enter Your Pin Number")
        NewUser = ATM(CardNumber,PinNumber)
        print("Choose Your Activity")
        print("1.BalanceEnquiery 2.Withdrawl")
        Activity = int(input("Choose The Activity Number"))
        if(Activity==1):
            NewUser.Checkbalance()
        elif(Activity==2):
            amount = int(input("enter the amount:- "))
            NewUser.Withdrawl()
    if __name__ == "__main__": 
      main()