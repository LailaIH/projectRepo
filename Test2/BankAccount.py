class BankAccount:
    def __init__(self,name,password):
        self.name=name
        self.password=password


    def getName(self):
        return self.name

    def getPassword(self):
        return self.password

    def setName(self,name):
        self.name = name

    def setPassword(self, password):
        self.password = password

    def setBalance(self,balance):
        self.balance = balance


    def getBalance(self):
         return self.balance

    def check(self):
        if self.getName()=="Laila" and self.getPassword()==123:
            return True
        else:
            return False

    def start(self):

        trials=0
        while trials < 3 :
            customerName = input('Enter your name')
            customerPass = int(input('Enter Password'))
            self.setName(customerName)
            self.setPassword(customerPass)
            if(not self.check()):

                print("try again!")
                trials+=1
                if(trials == 3) :
                    print('exit')

            else:
                choice=0
                while choice!= 3 :
                  print("Welcome to your Bank Account , please pick a servic\n 1.Draw \n 2.Deposit\n3.Exit")
                  choice = int(input(" "))
                  if(choice == 1):
                    amount = float(input('Please enter the amount you want to draw: '))
                    self.draw(amount)
                  elif choice==2:
                    amount = float(input('Please enter the amount you want to deposit: '))
                    self.deposit(amount)

                  elif choice == 3:
                    print("exiting...")

                  else:
                    print("unsupported choice")

                break


    def draw(self,amount):
        if amount <= self.getBalance():
            self.balance -= amount
            print('drawn successfully , your current balance is ' , self.getBalance())
        else:
            print("sorry , cannot draw")

    def deposit(self,amount):
        self.balance += amount
        print('Deposite process was successful , your current balance is', self.getBalance())