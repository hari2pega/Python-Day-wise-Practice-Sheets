#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Introduction to Python Oops classes

#1.Class
#2.Method - 
#3.Constructor
#4.Object or Instance


# In[13]:


class Dog:
    """ A Simple attemt to model a dog"""  # Doc String 
    def __init__(self,name,age):   #def Inside declaration is called a Method  # self is a keyword
        #def __init__ -- #It is a constructor __
        #Special method called as constructor, 
        #it is used to initialize the variables automatically inside a class
        self.name = name 
        self.age = age
    def sit(self):  #methods inside a class............... #sit() and roll_over() are methods inside a class
        """Simulate a dog sitting and age attributes"""
        print(f"{self.name} is now sitting")
    def roll_over(self):   # methods inside a class.....
            """Simulate rolling over in response"""
            print(f"{self.name} rolled over")
    def sleep(self):
        """simulate sleeping response"""
        print(f"{self.name} is now sleeping!!")
            
my_dog = Dog('willie',6)   #By assigining the objects  #arguments passing....!
#print(f"my dog's name is {my_dog.name}")
#print(f"my dog is {my_dog.age} years old")

your_dog = Dog('bruno',8)   #Dynamic passing of arguements ...!
#print(f"my dog's name is {your_dog.name}")
#print(f"my dog is {your_dog.age} years old")

someones_dog = Dog('rambo',2)


my_dog.sit()
my_dog.roll_over()
my_dog.sleep()
print("*************************************")


your_dog.sit()
your_dog.roll_over() 
your_dog.sleep()
print("*************************************")

someones_dog.sit()
someones_dog.roll_over() 
someones_dog.sleep()


# In[15]:


class Dog:
    """ A Simple attemt to model a dog"""  # Doc String 
    def __init__(self,name,age):   #def Inside declaration is called a Method
        #def __init__ -- #It is a constructor __
        #Special method called as constructor, 
        #it is used to initialize the variables automatically inside a class
        self.name = name 
        self.age = age
    def sit(self):  #methods inside a class............... #sit() and roll_over() are methods inside a class
        """Simulate a dog sitting and age attributes"""
        print(f"{self.name} is now sitting")
    def roll_over(self):   # methods inside a class.....
            """Simulate rolling over in response"""
            print(f"{self.name} rolled over")
    def sleep(self):
        """simulate sleeping response"""
        print(f"{self.name} is now sleeping!!")
            
my_dog = Dog('willie',6)   #By assigining the objects  #arguments passing....!
print(f"my dog's name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old")
print("**************************")

your_dog = Dog('bruno',8)   #Dynamic passing of arguements ...!
print(f"my dog's name is {your_dog.name}")
print(f"my dog is {your_dog.age} years old")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




