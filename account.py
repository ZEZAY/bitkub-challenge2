class Account:

    __account_database = []
    class_name = "Account"

    def __init__(self, address):
        self.address = address
        self.balance = 0
        self.status = False
        self.__account_database.append(self)

    @classmethod
    def show_all(cls):
       return cls.__account_database
    
    @classmethod 
    def find_account(cls, address):
        for acc in cls.__account_database:
            if address == acc.address:
                return acc
        return Account(address)
    
    @classmethod 
    def uncheck_account(cls):
        accounts = []
        for acc in cls.__account_database:
            if not acc.status:
                accounts.append(acc)
        return accounts
