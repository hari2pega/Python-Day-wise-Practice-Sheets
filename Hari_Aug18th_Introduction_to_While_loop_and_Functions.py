#!/usr/bin/env python
# coding: utf-8

# In[2]:


#While Loop Introduction

current_number = 1
while current_number <=8:
    print(current_number)
    current_number = current_number + 1
#Entire logic depends up on the above code  


# In[3]:


# Printing Odd numbers
current_number = 1
while current_number <=8:
    print(current_number)
    current_number = current_number + 2


# In[5]:


#Printing Odd numbers
current_number = 1
while current_number <=20:
    print(current_number)
    current_number = current_number + 2


# In[6]:


#Printing Even numbers
current_number = 2
while current_number <=20:
    print(current_number)
    current_number = current_number + 2


# In[11]:


#Introduction to Functions:

#given two numbers ----> a,b --- add them a+b... this task i am doing in a day for 5 times...

a = 25
b = 76
c = a+b
print(c)


# In[ ]:


#a = 1
#b = 2

#f(x) = a+b


# In[15]:


def greet_users():
    """Display a simply greeting"""  # Doc String  -- Explain what the function is doing
    print("Hello")

greet_users()


# In[17]:


def greet_user(username):  # username is called as defining Parameter 
    """Display a simply greeting to user logged in"""  # Doc String  -- Explain what the function is doing
    print(f"Hello, {username.title()}!")

greet_user('james bond')


# In[20]:


def greet_user(username,age,hobbies):  # username is called as defining Parameter 
    """Display a simply greeting to user logged in"""  # Doc String  -- Explain what the function is doing
    print(f"Hello, {username.title()}!")
   
greet_user('harish kumar','28','playing') #Function calling  ---> arguments passing


# In[ ]:


#More information about passing arguments --- 

#1. positional arguments 
#2. keyword arguments


# In[21]:


def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print(f"\n I have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name.title()}")
    
describe_pet('husky','bruno')  # Positional arguments


# In[25]:


def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name.title()}")
    
#describe_pet('bruno','husky')  # Positional arguments
describe_pet(pet_name = 'bruno' , animal_type = 'husky' )  #---> Keyword arguments


# In[ ]:





# In[ ]:





# In[ ]:




