import Account

moneta = Account.bank_account(10000)
moneta.payment(25, 'food', 'bakery')
moneta.payment(100, 'food', 'fruit')
moneta.income(500, 'gift', 'birthday')
moneta.payment(800, 'clothes', 'jeans')
CSOB = Account.bank_account(12000)
CSOB.payment(300, 'food', 'cake')
moneta.transfer(100, CSOB)

CSOB.import_from_csv('CSOB_records.csv')
moneta.import_from_csv('moneta_records.csv')

print(Account.bank_account.category_breakdown_all_accounts())
print(moneta.category_breakdown_single_account())
print(CSOB.category_breakdown_single_account())