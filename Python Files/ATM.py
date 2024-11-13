#Inheritance
# creating Atm Machine
class ATM:                              
    def __init__(self,B_Name="BOI",Pin=1234,Balance=10000) :
        self.__BankNmae = B_Name
        self.__Pin = Pin
        self.__Balanace = Balance

    def verifivation(self):
        print("Wait for few Sec ...")
        print("Details are verifying ...")
        print("Verification Are Successfully Done !")
        Pin=int(input("Enter Your Pin :"))
        self.__userValidation(Pin)

    def __userValidation(self,__Pin):
        while(True):
            if self.__Pin==__Pin:
                print("1.Withdrawl Ammount :")
                print("2.Check Balanace :")
                print("3.Exit")
                chooice=int(input("Enter :"))
                match(chooice):
                    case 1:
                        atm=int(input("Enter your Amount :"))
                        self.__WithdrawlAmt(atm)
                    case 2:
                        self.__CheckBal()
                    case 3:
                        print("Thank You For using Our Bank ATM !!!")
                        break
                    case _:
                        print("Invalid choice")
            else:
                print("Invalid Pin !")
                break


    def __WithdrawlAmt(self,W_Amt):
        if self.__Balanace>=W_Amt:
            self.__Balanace-=W_Amt
            print("Withdrawl is Successufully Done !\n (Kindly Collect your Cash)")
        else:
            print("Insufficient balanace :")

    def __CheckBal(self):
        print("Your Current Balanace Is :",self.__Balanace)

                        
atm=ATM() 

atm.verifivation() 