

'''Command Line Checkbook Application
You will create a command line checkbook application that allows 
users to track their finances with a command line interface.

Project Requirements
Build a .py file that will be run from the command line.

When run, the application should welcome the user, and prompt them
for an action to take:

view current balance
add a debit (withdrawal)
add a credit (deposit)
exit

The application should notify the user if the input is invalid and
prompt for another choice.

The application should persist between times that it is run.

Example, if you run the application, add some credits, exit the 
application and run it again, you should still see the balance that 
you previously created. In order to do this, your application will 
need to store its data in a text file. Consider creating a file where 
each line in the file represents a single transaction.

Utilize functions to call the balance, debit, credit, and exit

Example Ouput
Here is an example of what using the program might look like:


    $ python checkbook.py

    ~~~ Welcome to your terminal checkbook! ~~~

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 5
    Invalid choice: 5

    Your choice? 1

    Your current balance is $100.00.

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 2

    How much is the debit? $50

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 1

    Your current balance is $50.00.

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 4

    Thanks, have a great day! '''

import os
transactions_file = "transactions.txt"
def check_file():
    if not os.path.exists(transactions_file):
        open(transactions_file, "w").close()
def view_balance():
    check_file()
    with open(transactions_file, "r") as f:
        lines = f.readlines()
        balance = 0
        for line in lines:
            balance += int(line)
        return print('Your current balance is ', '${}'.format(balance))
def withdraw(amount):
    check_file()
    with open(transactions_file, "a") as f:
        f.write(str(-amount) + "\n")
def deposit(amount):
    check_file()
    with open(transactions_file, "a") as f:
        f.write(str(amount) + "\n")
while True:
    print('What would you like to do?\n\n1) view current balance\n2) record a debit (withdraw)\n3) record a credit (deposit)\n4) exit')
    num = int(input('Your Choice? '))
    
    if num == 1:
        view_balance()
        continue 
    elif num == 2:
        amount = int(input('Enter the amount of the debit: '))
        withdraw(amount)
        print(('Debit of', '${}'.format(amount), 'is successful!'))
        continue
    elif num == 3:
        amount = int(input('Enter the amount of the withdraw: '))
        deposit(amount)
        print('Credit of', '${}'.format(amount),' is successful!')
        continue
    elif num == 4:
        print('Thank you, goodbye!')
        break
    elif num != (1, 2, 3, 4):
        print('Invalid Choice')
