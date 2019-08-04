#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=98
y=87
print (x+y)
print (x*y)


# In[9]:


#introduction to for loops!!... ***
# -- Looping through an entire list. Creation of temporary variable inside a for loop
magicians = ['harry','dumbeldore','hormanie','anand']
#for magician in magicians:
        #print(magician)
        #print('hello how r u doing?')
for x in magicians:
    print(x)
    
# this space is called indentation... 4 lines of free space advised by the zen pf python.... 


# In[23]:


magicians = ['harry','dumbeldore','hormanie','anand']
for n in magicians:
    print(f"{n.title()} , that was a great trick!")
print(f"I cant wait to see your next trick, {n.title()}") # This print not in the for loop that's y it's printing only once


# In[25]:


magicians = ['harry','dumbeldore','hormanie','anand']
for n in magicians:
    print(f"{n.title()} , that was a great trick!")
    print(f"I cant wait to see your next trick, {n.title()}") # this print is in the for loop...


# In[27]:


#making numerical list!...
for x in range(1,21):
    print(x)
# how the range function works... 
# Non inclusive and exclusive values . it means between values it will print..


# In[28]:


#using range to make a list of numbers to store..
numbers = list(range(1,6))
print(numbers)


# In[30]:


#printing even numbers in the given range...
even_numbers = list(range(2,20,2))
print(even_numbers)


# In[36]:


#printing odd numbers in the given range...
odd_numbers = list(range(1,20,2))
print(odd_numbers)


# In[39]:


#how to p[erform a simple statistical operations on a list...
digits = [1,2,4,6,8,9,5,6,7]
print(min(digits))
print(max(digits))
print(sum(digits))


# In[35]:


# slicing of list ... ****** sub list of a list... 
players = ['yuvaraj','sachin','dhoni','dravid','kumble']
# I want to print out only the values from dhoni to kumble only... ?
print(players[2:5])


# In[40]:


# slicing of list ... ****** sub list of a list... 
players = ['yuvaraj','sachin','dhoni','dravid','kumble']
# I want to print out only the values from dhoni to kumble only... ?
print(players[2:4])


# In[ ]:




