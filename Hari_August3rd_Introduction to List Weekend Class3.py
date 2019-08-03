#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=19
y=10
print(x+y)
print(x-y)


# In[28]:


#Introduction to List data type - List is a Mutable data type
'''1. List is an Mutable Data type.. it is nothing but we can be changed once assigned!
A list is a collection of items in a particuler order'''
bicycles =['Hero','Atlas','Ranger','BMX','redline']
print(bicycles)
#How to print a particuler item from the list - Output required as ranger
print(bicycles[2])
print(bicycles[3])
#Deleting one of the item from the list
del bicycles[4]
print(bicycles)
# *** what if i want to give the index which is not there in the list...
print(bicycles[1]) #Index error -- List index out of range


# In[15]:


bicycles = ['heRo','Atlas','Ranger','BMX','redline']
print(bicycles[0].title())
print(bicycles[0].upper())
print(bicycles[0].lower())


# In[19]:


bicycles = ['heRo','Atlas','ranGer','BMX','redline']
message = f"My first bicycle was {bicycles[2].title()}. "
print(message)


# In[25]:


#Delete the particuler name from the given list -- I want to exclude BMX from the given list
bicycles =['Hero','Atlas','Ranger','BMX','redline']
del bicycles[3]
print(bicycles)


# In[30]:


# How to change, add and modify elements in a list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#1.how to change the element in the list .. Ans is .. by using Index positions..,
motorcycles[0]='ducati'
print(motorcycles)
#2. How to add or append/include the element in the list


# In[35]:


#2. How to add or append/include the elements in the list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('bullet')
print(motorcycles)
#*** IQ***One point to remember ... If i wanted to include ducati in the 1st index position of the above given list... 
# How do you achieve this?
motorcycles.insert(1,'ducati')
print(motorcycles)


# In[36]:


car = []
#creating an empty list ... *** Dynamic creation of list ***
car.append('audi')
car.append('bmw')
car.append('volvo')
car.append('swift')
car.append('Hyundai')
print(car)


# In[40]:


#how to delete the items/elements from the list 
motorcycles = ['honda','yamaha','suzuki','r15','pulsar']
print(motorcycles)
del motorcycles[2]
print(motorcycles)
# *** pop delete the last item from the list.. pop() will not delete the items permanently... 
# the deleted items will be stored separately in another variable .. declared ...
motorcycles.pop()
print(motorcycles)


# In[50]:


motorcycles = ['honda','hayabusa','yamaha','suzuki','r15','pulsar']
print(motorcycles)
#how to sort the list...? arranging in assending or descending...?
#for arranging in a particular order ...!!
# it sorts based upon the alphabets
motorcycles.sort()
print(motorcycles)
#how to print the elements in a list in reverse/descending order.....?
#Printing/displaying the elements in reverse/descending order
motorcycles.reverse()
print(motorcycles)
#Finding the number of elements in the list
print(len(motorcycles))


# In[ ]:




