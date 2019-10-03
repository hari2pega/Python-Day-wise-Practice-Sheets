#!/usr/bin/env python
# coding: utf-8

# In[22]:


#iterating...!!!

import numpy as np
#ID Arrays
a = np.arange(11)**2
a


# In[28]:


for i in a:
    print(i**(1/2))
          #i is a temporary variable
          
    


# In[8]:


#multi dimensional arrays
students = np.array([['amith','teja','veena','prasad'],[65,70,75,89,76],[54,76,87,65,45]])
students

for i in students:
    print('i=',i)


# In[12]:


for x in students:
    print('marks=',x)
    


# In[29]:


for element in students.flatten():
    print(element)
    
    #what is default flattering order --> row wise( C order)


# In[18]:


#colum order ---> known as Fortan order !!!
for element in students.flatten(order = 'F'):
    print(element)


# In[ ]:


#nditer 

#Efficient multi dimensional iterator object to over arrays


# In[20]:


x = np.arange(12).reshape(3,4)
x


# In[21]:


for i in np.nditer(x):
    print(i)
    


# In[24]:


for i in np.nditer(x, order = 'F'):
    print(i)


# In[25]:


#flag:
for i in np.nditer(x, order = 'F', flags = ['external_loop']):
    print(i)


# In[ ]:


#Real time datasets tomorrow -- 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




