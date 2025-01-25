class Bank:
 def __init__(self, number, passwor):
      self.account_no=number
      # to make account_passwork private i will add __ (double underscore) at start of variable 
      self.__account_password=passwor
      #in this functon we can access password because it is inside class not outside
 def resetPasswor(self):
    print(self.__account_password)
    

b1=Bank("21212","23222")
print(b1.account_no)
print(b1.resetPasswor())
print(b1.__account_password)
   