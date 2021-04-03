from tabulate import tabulate
import requests
import json
from account import Account
from transaction import Transaction

# url = "https://api-ropsten.etherscan.io/api?module=account&action=tokentx&address=0x4e83362442b8d1bec281594cea3050c8eb01311c&startblock=0&endblock=999999999&sort=asc&apikey=KUSX5NPQHGKPT45Y6T5BBNPWPR3XZB6YIX"
# x = requests.get(url)
# print(x)


def track_account(address):
    Account.find_account(address).status = True
    url = f"https://api-ropsten.etherscan.io/api?module=account&action=tokentx&address={address}&startblock=0&endblock=999999999&sort=asc&apikey=KUSX5NPQHGKPT45Y6T5BBNPWPR3XZB6YIX"
    data = requests.get(url).json()

    # f = open('result.json')
    # data = json.load(f)

    for result in data['result']:
        if result['tokenSymbol'] == 'BKTC':
            if not Transaction.is_checked_account(result['hash']):
                Transaction(result['hash'], result['from'],
                            result['to'], result['value'])

                from_account = Account.find_account(result['from'])
                to_account = Account.find_account(result['to'])

                from_account.balance -= float(result['value'])/(10**18)
                to_account.balance += float(result['value'])/(10**18)
    
    for acount in Account.uncheck_account():
        track_account(acount.address)


def print_final():
    results = []
    count = 0
    for transaction in Transaction.show_all():
        count += 1
        results.append([
            count,
            transaction.hash,
            transaction.from_account,
            transaction.to_account,
            transaction.value,
        ])
    print(tabulate(results, headers=[
          'Tx hash', 'from (address)', ' to (address)', 'Amount transfer'], tablefmt='orgtbl'))

    accounts = []
    for account in Account.show_all():
        accounts.append([
            account.address,
            account.balance
        ])
    print(tabulate(accounts, headers=[
          'Address', 'Balance'], tablefmt='orgtbl'))


track_account('0xEcA19B1a87442b0c25801B809bf567A6ca87B1da')
print_final()
