#!/usr/bin/env python
# coding: utf-8

# In[ ]:


''' 1. Define a function named is_two. It should accept one input 
and return True if the passed input is either the number or the 
string 2, False otherwise.'''


# In[18]:


def is_two(arg):
    if arg == 2:
        return True
    else:
        return False
is_two(2)


# In[1]:


''' 2. Define a function named is_vowel.
It should return True if the passed string is a vowel, 
False otherwise.'''


# In[16]:


def is_vowel(arg):
    vowels = ["a","e","i","o","u"]
    return arg.lower() in vowels

is_vowel("u")


# In[ ]:


'''Define a function named is_consonant. It should return
True if the passed string is a consonant, False otherwise.
Use your is_vowel function to accomplish this.'''


# In[24]:


def is_consonant(arg):
    vowels = ["a","e","i","o","u"]
    if arg.lower() not in vowels:
        return True
    else:
        return False
is_consonant("n")


# In[ ]:


''' 4. Define a function that accepts a string that is a word. 
The function should capitalize the first letter of the word if 
the word starts with a consonant.'''


# In[36]:


def cap_word(arg):
    for n in arg[0]:
        if is_consonant(n):
            return (f"{arg}".capitalize())
        else:
            return arg
cap_word("codeUp")


# In[ ]:


''' 5. Define a function named calculate_tip. It should accept a 
tip percentage (a number between 0 and 1) and the bill total, and
return the amount to tip.'''


# In[67]:


def calculate_tip(percent, bill):
    tip_amount = percent*bill
    return (tip_amount)
calculate_tip(.25, 100)


# In[ ]:


''' 6. Define a function named apply_discount. It should accept 
a original price, and a discount percentage, and return the 
price after the discount is applied.'''


# In[74]:


def apply_discount(discount, price):
# discount formatted as 20% = 20
    total_discount = price - (price * (discount / 100))
    return (total_discount)
apply_discount(30, 10)


# In[ ]:


''' 7. Define a function named handle_commas. It should 
accept a string that is a number that contains commas in 
it as input, and return a number as output.'''


# In[75]:


def handle_commas(arg):
    return float(arg.replace(',',''))
handle_commas("1,000,2")


# In[ ]:


''' 8. Define a function named get_letter_grade.
It should accept a number and return the letter grade associated
with that number (A-F).'''


# In[83]:


def get_letter_grade(num):
    

    if num <= 59:
        return ("F")
    elif num > 59 and num <= 69:
        return ("D")
    elif num > 69 and num <= 79:
        return ("C")
    elif num > 79 and num <=89:
        return ("B")
    elif num > 89 and num <=100:
        return ("A")
get_letter_grade(80)


# In[ ]:


''' 9. Define a function named remove_vowels that accepts a 
string and returns a string with all the vowels removed.'''


# In[137]:


def remove_vowels(arg):
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        arg = arg.replace(vowel, '')
    return arg
remove_vowels('methylchloroisothiazolinone')
# ^ normally the longest work on a shampoo bottle


# In[ ]:


''' 10. Define a function named normalize_name. It should accept a 
string and return a valid python identifier, that is:
anything that is not a valid python identifier should be removed
leading and trailing whitespace should be removed
everything should be lowercase
spaces should be replaced with underscores
for example:
Name will become name
First Name will become first_name
% Completed will become completed'''


# In[159]:


def normalize_name(arg):
    arg = "".join(c for c in arg if c.isalnum() or c == " ") 
    for c in arg:
            return arg.strip().lower().replace(" ", "_")
normalize_name("   %First name  %   ")
# isalnum is a function that only keeps alphabetical or numerical characters


# In[ ]:


''' 11. Write a function named cumulative_sum that accepts a list 
of numbers and returns a list that is the cumulative sum of the 
numbers in the list.
cumulative_sum([1, 1, 1]) returns [1, 2, 3]
cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]'''


# In[145]:


def cumulative_sum(arg):
    total = 0
    for number in arg:
        total += number
        yield total
list(cumulative_sum([1,2,3,4,5,6,7,8,9,10]))


# # BONUS

# In[ ]:


''' 1. Create a function named twelveto24. 
It should accept a string in the format 10:45am or 4:30pm and 
return a string that is the representation of the time in a 24-hour 
format. Bonus write a function that does the opposite.'''


# In[ ]:


def twelveto24(arg)


# In[ ]:


''' 2. Create a function named col_index. It should accept a
spreadsheet column name, and return the index number of the column.
col_index('A') returns 1
col_index('B') returns 2
col_index('AA') returns 27'''


# In[ ]:


def col_index

