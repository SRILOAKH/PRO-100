from types import new_class


class atm:
    def __init__(self,atmcardnumber,pinnumber) :
        self.atmcardnumber=atmcardnumber
        self.pinnumber=pinnumber
    def cashwithdrawal(self,amount):
        new_amount=3000-amount
        print("cashwithdrawal.amount"+str(amount)+"your remaining balance"+str(new_amount))
    def balanceenquiry(self):
        print("balanceenquiry your balance is 3000")