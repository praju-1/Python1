class Bank:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance= balance

    def info(self):
        print("Account holder name : ", self.name)
        print("Account number is  : ", self.acc_no)
        print("Balance is : ", self.__balance)

    def deposite(self, amt):
        self.__balance += amt

    def withdrawl(self, amt):
        self.__balance -= amt

    def update_balance(self):
        print("Update balance is : ", self.__balance)

b = Bank("John", 1234, 5000)
b.info()
b.deposite(2000)
b.update_balance()
b.withdrawl(1000)
b.update_balance()
# print(b.acc_no)
# b.__balance = 324
# print(b.acc_no)
# b.info()