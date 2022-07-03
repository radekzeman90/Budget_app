import csv
import pandas as pd
import gc

class bank_account:
    def __init__(self, starting_amount: float):
        # defines a bank account with ammount of money in time of its creation
        #self.list is a list where all money transfer will be stored
        assert starting_amount > 0, f"Amount {starting_amount} has to be positive number"
        self.starting_amount = starting_amount
        self.list = []
        self.account_level = starting_amount

    def payment(self, amount: float, category: str, description=''):
        # creates a record of payment from given account
        self.amount = amount
        self.category = category
        self.description = description
        self.list.append(({'amount': -amount}, {'category': category}, {'description': description}))

    def account_balance(self):
        # returns current balance of given account
        balance = self.starting_amount
        for item in self.list:
            balance += item[0]['amount']
        return(balance)

    def income(self, amount: float, category: str, description=''):
        # creates a record of income payment to given account
        self.amount = amount
        self.category = category
        self.description = description
        self.list.append(({'amount': amount}, {'category': category}, {'description': description}))

    def check_account(self, amount):
        # checks if payment from an account is greater than account balance
        if self.account_balance() >= amount:
            return True
        else:
            print (f"Payment is greater than account balance.")
            return False

    def transfer(self, amount, account):
        # creates a record of money transfer from given account to another account stated as an parametr
        self.payment(amount, 'transfer')
        account.income(amount, 'transfer')

    def import_from_csv(self, file_name):
        # imports data of money transfers in given bank accounf from .csv file
        with open(file_name, 'r') as br:
            reader = csv.DictReader(br)
            items = list(reader)
        for record in items:
            amount = float(record.get('amount'))
            category = record.get('category')
            description = record.get('description')
            self.list.append(({'amount': amount}, {'category': category}, {'description': description}))

    def data_to_df(self):
        #creates dataframe from all money transfers in given account
        df = pd.DataFrame({
            'amount': [record[0].get('amount') for record in self.list],
            'category': [record[1].get('category') for record in self.list],
            'description': [record[2].get('description') for record in self.list],
        })
        return df

    def category_breakdown_single_account(self):
        #will sumarize money flows within single account by categories
        breakdown = self.data_to_df()[['amount', 'category']].groupby('category').sum().sort_values(['amount'])
        return(breakdown)

    @classmethod
    def category_breakdown_all_accounts(cls):
        # will sumarize money flows within all created accounts by categories
        df = pd.DataFrame()
        for obj in gc.get_objects():
            if isinstance(obj, bank_account):
                asd = obj.data_to_df()[['amount', 'category']]
                df = pd.concat([df,asd])
        df = df.groupby('category').sum().sort_values(['amount'])
        return(df)









