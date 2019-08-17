#!/usr/bin/env python
# coding: utf-8

# In[23]:


#introduction to tuple - Data type
#1. It is an immutable data type.
#2. why tuple is needed....?
#3. if we want to create a list of items that cannot change, then we wuill be goig for tuple at that time
#4. how to declare tuple ..!!
#5. tuple can be created by using parenthesis...()
# Example are below: If we want to create a rectangle that should always be an fixed value

dimensions = (200,50)
#print(dimensions[0])
#print(dimensions[1])

print(dimensions[0])
print(dimensions[1])


# In[34]:


dimensions = (225,78)
print(dimensions[0])
print(dimensions[1])

dimensions[0] = 256


# In[38]:


dimensions1 = (20,50,60)
#looping through a Tuple by using for loop:
for dimension in dimensions:
    print(dimension)
for dimension in dimensions1:
    #print('\n')
    print(dimension)


# In[39]:


dimensions2 = (200,580,760)
print(dimensions2)


# In[41]:


message = 'harish'
print(message.title())


# In[42]:


message = 'harish'
print(message.upper())


# In[43]:


message = 'hArish'
print(message.lower())


# In[27]:


# ****** The styling guide:  -----> PEP8

#PEP --- Python Enhancement Praposols -8 ***

#1. line length -- should not exceed more than 80 words .... 
#2. Maintaining blank lines
#3. Indentation is ---- (4 blank lines)

triangle = (1,2,3)
print('original values')

#four spaces of lines ---- this is called as indentations:

for x in triangle:
    print(x)
triangle = (4,5,6)
print('\nmodified values:')
for x in triangle:
    print(x)
    


# In[ ]:


# Introduction to If conditions 
# Basic syntax of if conditions

#if condition_test:
        do_something


# In[1]:


#1. If my car is bmw then i want to be in upper acse
#2. If not bmw any other car then i want it to be in Tital case -- print 
cars = ['audi','toyota','benz','maruti','bmw']

for car in cars:
    if car== 'bmw':
        print(car.upper())
    else:
        print(car.title())
        


# In[2]:


#true or false of the statements
car = 'rangerover'

car == 'rangerover'   # It is a equality test !!


# In[3]:


car = 'Rangerover'

car == 'rangerover'   # It is a equality test !!


# In[4]:


car = 'Rangerover'

car.title() == 'rangerover'   # It is a equality test !!


# In[5]:


car = 'Rangerover'

car.upper() == 'rangerover'   # It is a equality test !!


# In[6]:


car = 'Rangerover'

car.lower() == 'rangerover'   # It is a equality test !!


# In[10]:


#checking whether a value is in list ?

requested_toppings = ['mushroom','corn','pineapple']

'mushroom' in requested_toppings


# In[9]:


requested_toppings = ['mushroom','corn','pineapple']

'pepperoni' in requested_toppings


# In[11]:


requested_toppings = ['mushroom','corn','pineapple']

'mushroom' not in requested_toppings  #? not in used to cheking whether a value is available in the list or not?


# In[15]:


#Boolean expressions : it declare true or falseness of the given conditions
age = 19
if age >= 18:
    print('you are old enough to vote!!')
else:
    print('sorry you are too young to vote!!')


# In[16]:


age = 17
if age >= 18:
    print('you are old enough to vote!!')
else:
    print('sorry you are too young to vote!!')


# In[17]:


# Most tested it in IQ ### Introduction to user Inputs... 

message = input("Tell me something and i will repeat it for you:")
print(message)


# In[18]:


message = input("Tell me something and i will repeat it for you:")
print(message)


# In[19]:


age = input("How old are you?")
print(age)


# In[44]:


email = input("What is your email ID?")
print(email)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




