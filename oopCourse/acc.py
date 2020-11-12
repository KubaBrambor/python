class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        self.balance = self.connect(filepath)

    def connect(self, filepath):
        with open(filepath, 'r') as file:
            read_file = int(file.read())
        return read_file

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.commit()
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class CheckAccount(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount, reciver):
        self.balance = self.balance - amount - self.fee
        self.commit()
        inner_balance = self.connect(reciver)
        inner_balance = inner_balance + amount
        self.commit_to_reciver(inner_balance, reciver)

    def commit_to_reciver(self, inner_balance, reciver):
        with open(reciver, 'w') as file:
            file.write(str(inner_balance))

checkaccount = CheckAccount("balance.txt", 1)
checkaccount.transfer(100, "balance2.txt")
print(checkaccount.balance)