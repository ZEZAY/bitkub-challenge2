class Transaction:

    __transaction_database = []
    class_name = "Transaction"

    def __init__(self, hash, from_account, to_account, value):
        self.hash = hash
        self.from_account = from_account
        self.to_account = to_account
        self.value = value
        self.__transaction_database.append(self)

    @classmethod
    def show_all(cls):
        return cls.__transaction_database

    @classmethod
    def is_checked_account(cls, hash):
        for transaction in cls.__transaction_database:
            if transaction.hash == hash:
                return True
        return False
