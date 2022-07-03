# Budget_app
This budget app is writen in python and it is capable of handling multiple bank accounts, assign categories and description to different money transfers.
Code is written with respect to OOP principles.
Source file, where class bank_account is decribed, is called Account.py and in main.py is written an example of controling the code.
Records can be added in two ways - firstly through methods .payment, .income, .transfer.
With method .payment and .income you input amount as a positive number, with method .transfer you put account where money is sent to as an argument.
Secondly you can input recors from .csv file with data in format 'amount,category,description' with method .import_from_csv.
In .csv file there has to be considered positive/negative sign before amounts for incomes and payments.

There are also two ways how to get an overview over money records filtred through categories.
Method category_breakdown_single_account will bring an overview from one account.
Class method category_breakdown_all_accounts will bring an overview over all created accounts.
