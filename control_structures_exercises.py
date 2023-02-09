#!/usr/bin/env python
# coding: utf-8

# In[ ]:


''' 1. Conditional Basics

a. Prompt the user for a day of the week, print out whether the day is Monday or not

b. Prompt the user for a day of the week, print out whether the day is a weekday or a weekend

c. Create variables and make up values for

    The number of hours worked in one week
    The hourly rate
    How much the week's paycheck will be
    
Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours.'''


# In[2]:


# a.
day = input('day_of_the_week')
if day.startswith('Mon'):
    print(' It is monday')
else:
    print(' It is nor Monday')


# In[3]:


# b.
day = input('day_of_the_week')
if day.startswith('S'):
    print('Weekend')
else:
    print('Weekday')


# In[4]:


# c.
hw = input('hours_worked? ')
hw = int(hw)
hr = input('hourly_rate? ')
hr = int(hr)
weekly_pay = hw * hr
if hw > 40:
     print(((hw - 40) * (hr * 1.5)) + (40 * hr))
else:
    print(weekly_pay)


# In[ ]:


''' 2.Loop Basics '''


# In[6]:


### a
#i. Create an integer variable i with a value of 5. 
# Create a while loop that runs so long as i is less 
# than or equal to 15. Each loop iteration, output the 
# current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1


# In[7]:


#i. Create a while loop that will count by 2's starting with
#   0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(f"{i}")
    i += 2


# In[8]:


#ii. Alter your loop to count backwards by 5's from 100 to -10

i = 100
while i >= -10:
    print(f"{i}")
    i -= 5


# In[9]:


#iii. Create a while loop that starts at 2, and displays the number 
# squared on each line while the number is less than 1,000,000.
# Output should equal:

i = 2
while i <= 1000000:
    print(f"{i}")
    i **= 2


# In[10]:


# iv. Write a loop that uses print to create the output shown below.

i = 100
while i > 0:
    print(f"{i}")
    i -= 5


# In[11]:


### b. For Loops


# In[12]:


# i. Write some code that prompts the user for a number, then shows
#    a multiplication table up through 10 for that number.


# In[13]:


num = input("Number? ")
num = int(num)
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)


# In[14]:


#ii Create a for loop that uses print to create the 
#.  output shown below.

for i in range(1, 10):
    print(str(i)*i)


# In[15]:


### C. break and continue


# In[16]:


# i. Write a program that prompts the user for a positive integer.
#    Next write a loop that prints out the numbers from the number 
#    the user entered down to 1.


num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Invalid")
else:
    for i in range(num, 0, -1):
        print(i)


# In[29]:


# ii. The input function can be used to prompt for input and use 
#     that input in your python code. Prompt the user to enter a
#     positive number and write a loop that counts from 0 to that 
#     number. 


num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Invalid")
else:
    for i in range(0, num + 1, +1):
        print(i)


# In[23]:


# iii. Prompt the user for an odd number between 1 and 50. 
#      Use a loop and a break statement to continue prompting the user 
#      if they enter invalid input. (Hint: use the isdigit method on 
#      strings to determine this). Use a loop and the continue statement 
#      to output all the odd numbers between 1 and 50, except for the 
#      number the user entered.



while True:
    odd_input = input('please enter an odd number between 1 and 50. ')
    if odd_input.isdigit():
        odd_input = int(odd_input)
        if odd_input % 2 ==0:
            continue
        break
        
i = 1
while i <= 50:
    if i == odd_input:
        print(f'Yikes! Skipping number: {i}')
        i += 2
        continue
    print(f"Here is an odd number: {i}")
    i += 2


# In[ ]:


''' 3. Fizzbuzz

One of the most common interview questions for entry-level
programmers is the FizzBuzz test. Developed by Imran Ghory, 
the test is designed to test basic looping and conditional 
logic skills.

Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print 
"FizzBuzz".'''


# In[28]:


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# In[ ]:


''' 4. Display a table of powers.

Prompt the user to enter an integer
Display a table of squares and cubes from 1 to the value entered
Ask if the user wants to continue
Assume that the user will enter valid data
Only continue if the user agrees to

Bonus: Research python's format string specifiers to align the table'''


# In[46]:


n_integer = int(input('What number would you like to go up to? '))

print("number | squared | cubed")
print("-------|---------|------")
for i in range(1, n_integer + 1):
    print("%6i | %7i | %5i" % (i, i**2, i**3))
    
# %6i meaning. pad with 6 spaces. used to square the table 
# %.6 would pad with zeros instead of blank spaces
    


# In[ ]:


''' 5. Convert given number grades into letter grades.

Prompt the user for a numerical grade from 0 to 100
Display the corresponding letter grade
Prompt the user to continue
Assume that the user will enter valid integers for the grades
The application should only continue if the user agrees to
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0'''


# In[57]:


while True:
    

    num = int(input("Enter a in integer from 0 to 100: "))

    if num <= 59:
        print("F")
    elif num > 59 and num <= 66:
        print("D")
    elif num > 66 and num <= 79:
        print("C")
    elif num > 79 and num <=87:
        print("B")
    elif num > 87 and num <=100:
        print("A")
    
    user_response = input('Would you like to continue? (y/n) ')
    if user_response.lower() != 'y':
        break
        
    
# In[ ]:


''' 6. Create a list of dictionaries where each dictionary 
represents a book that you have read. Each dictionary in the list 
should have the keys title, author, and genre. Loop through the 
list and print out information about each book.

a. Prompt the user to enter a genre, then loop through your books
list and print out the titles of all the books in that genre.'''


# In[71]:


book = [ {'title': 'The Great Gatsby','author': 'Scorr Fitzgerald', 'genre': 'fiction'}, 
         {'title': 'Moby Dick','author': 'Scorr Fitzgerald', 'genre': 'fiction'}, 
         {'title': 'Weapons of Mass Destruction','author': 'Cathy O\'Neil', 'genre': 'non-fiction'}, 
         {'title': 'Alexander Hamilton','author': 'Ron Chernow', 'genre': 'biography'}, 
         {'title': 'The Hunger Games','Suzanne Collins': 'Scorr Fitzgerald', 'genre': 'fiction'} ]
for book in books:
    print("---")
    print("title: {}".format(book["title"]))
    print("author: {}".format(book["author"]))
    print("genre: {}".format(book["genre"]))


# In[80]:


# a. Prompt the user to enter a genre, then loop through your books
#    list and print out the titles of all the books in that genre.
book =  [ {'title': 'The Great Gatsby','author': 'Scorr Fitzgerald', 'genre': 'fiction'}, 
         {'title': 'Moby Dick','author': 'Scorr Fitzgerald', 'genre': 'fiction'}, 
         {'title': 'Weapons of Mass Destruction','author': 'Cathy O\'Neil', 'genre': 'non-fiction'}, 
         {'title': 'Alexander Hamilton','author': 'Ron Chernow', 'genre': 'biography'}, 
         {'title': 'The Hunger Games','Suzanne Collins': 'Scorr Fitzgerald', 'genre': 'fiction'} ]
    
genre = input("Enter a genre: ")

print("Books in the genre '%s':" % genre)
for book in books:
    if book["genre"] == genre:
        print("title: {}".format(book["title"]))

