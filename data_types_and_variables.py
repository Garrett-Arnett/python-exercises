''' Inside the script, write Python code to describe 
the following scenarios. You will need to create and
 assign variables and use operators.'''


''' 5. You have rented some movies for your kids:

The Little Mermaid for 3 days
Brother Bear for 5 days
Hercules for 1 day 

If the daily fee to rent a movie is 3 dollars,
 how much will you have to pay?'''


fee = 3 #dollars
days_rented = (3 + 5 + 1)

payment = fee * days_rented
print(payment)


''' 6. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.

They pay you the following hourly rates:

Google: 400 dollars
Amazon: 380 dollars
Facebook: 350 dollars
This week you worked: 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

How much will you receive in payment for this week? '''

google_pay = 400 * 6
amazon_pay = 380 * 4
facebook_pay = 350 * 10

total_pay = google_pay + amazon_pay + facebook_pay

print(total_pay)





''' 7. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule. '''




class_not_full = True

class_conflict = False

can_enroll = class_not_full and not class_conflict

print(can_enroll)



''' 8. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.'''


number_of_items = 3
offer_expired = False
premium_member = False

if (number_of_items > 2 or premium_member) and not offer_expired:
    offer_applied = True
else:
    offer_aplied = False
    
print(offer_applied)


''' 9. Continue working in the data_types_and_variables.py file. Use the following code to follow the instructions below:


username = 'codeup'
password = 'notastrongpassword'
Create a variable that holds a boolean value for each of the following conditions:

The password must be at least 5 characters
The username must be no more than 20 characters
The password must not be the same as the username
Bonus Neither the username or password can start or end with whitespace'''


username = 'codeup'
password = 'notastrongpassword'

password_legnth = len(password) >=5
username_legnth = len(username) <= 20
password_different_from_username = password != username
no_whitespace_username = username.strip() == username
no_whitespace_password = password.strip() == password

conditions_met = password_legnth and username_legnth and password_different_from_username and no_whitespace_username and no_whitespace_password

print(conditions_met)











