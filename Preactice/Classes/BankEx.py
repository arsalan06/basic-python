class bank:
    accountsList=[{
        "no":1212,
        "balance":132323
    },
    {
        "no":2121,
        "balance":3434
    }]
    def __init__(self, amount, no):
        self.amount=amount
        self.no=no

    def CheckAmount(self):
        for el in self.accountsList:
            if(el["no"]==self.no):
             print("here is account", el)
    
    def CreditAmount(self):
        for el in self.accountsList:
            if(el["no"]==self.no):
             el["balance"]=el["balance"]-self.amount
             print("here is account", self.CureentAmount())
    
    def CureentAmount(self):
        for el in self.accountsList:
            if(el["no"]==self.no):
             return el

b1=bank(1212, 1212)
b1.CheckAmount()
b1.CreditAmount()