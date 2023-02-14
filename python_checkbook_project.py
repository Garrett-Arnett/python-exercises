#                          ~~~  Notes ~~~

# This code is able to run numerical arguments up to and no more than 2 decimal places, 
# for example you can deposit $20.24 and a credit of $20.24 will be added to your account.

# The user cannnot debit or credit a negative number into the system. If the user tries to, the 
# transation will be cancelled and the interaction will reset.


# The user cannot have a balance that will fall under 0. If the user withdraws an amount exceeding 
# the users current balance, the transaction will be canceled and the interaction will reset.



import os

transactions_file = "transactions.txt"

def check_file():
    if not os.path.exists(transactions_file):
        open(transactions_file, "w").close()

def view_balance():
    check_file()
    with open(transactions_file, "r") as f:
        lines = f.readlines()
        balance = 0.0
        for line in lines:
            balance += float(line)
        return print('Your current balance is ', '${:.2f}'.format(balance))

def get_valid_float(amount):
    while True:
        try:
            value = float(input(amount))
            if value != round(value, 2):
                print("Please enter a value with no more than two decimal places.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")
    
def withdraw(amount):
    if amount < 0:
        print("Error: withdraw amount must be a positive number. Transaction cancelled.")
        return
    check_file()
    with open(transactions_file, "r") as f:
        lines = f.readlines()
        balance = 0.0
        for line in lines:
            balance += float(line)
        if balance - amount < 0:
            print("Withdrawal amount is greater than current balance. Transaction cancelled.")
        elif balance - amount >= 0:
            with open(transactions_file, "a") as f:
                f.write(str(-amount) + "\n")
                print('Debit of', '${:.2f}'.format(amount), 'is successful!')
def deposit(amount):
    if amount < 0:
        print("Error: deposit amount must be a positive number. Transaction cancelled.")
        return
    check_file()
    with open(transactions_file, "a") as f:
        f.write(str(amount) + "\n")
    print('Credit of ' '${:.2f}'.format(amount) ,'is successful!')
print('~~~ Welcome to your terminal checkbook! ~~~')
while True:
    print('What would you like to do?\n\n1) View current balance\n2) Record a debit (Withdraw)\n3) Record a credit (Deposit)\n4) Exit')
    num = input('Your Choice? ')

    if num == '1':
        view_balance()
        continue
    elif num == '2':
        amount = get_valid_float('Enter the amount of the debit: ')
        withdraw(amount)
        continue
    elif num == '3':
        amount = get_valid_float('Enter the amount of the credit: ')
        deposit(amount)
        continue
    elif num == '4':
        print('Thank you, goodbye!')
        break
    else:
        print('Invalid Choice')
