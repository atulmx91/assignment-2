#!/usr/bin/env python
# coding: utf-8

# In[4]:


###1
the two Boolean data types are "True" and "False"
We write them in conditional scenarios. 


# In[2]:


###2
The three boolean operators are "and" , "or", "not"


# In[5]:


###3
"and" truth table
true and true = True
true and false = False
false and true = False
false and false = False


# In[6]:


"or" truth table
true or true = True
true or false = True
false or true = True
false or false = False


# In[9]:


#"not" truth table 
#not true = False
#not false = True


# In[10]:


###4
#(5 > 4) and (3 == 5) = False
#not (5 > 4) = False
#(5 > 4) or (3 == 5) = True
#not ((5 > 4) or (3 == 5)) = False
#(True and True) and (True == False) = False
#(not False) or (not True) = True


# In[11]:


###5
#The six comparission operators are <,>,<=,>=,=,!=


# In[15]:


###6
#The dfference between assignment operator and eqaul to is when we have to assign a value to 
#an object we use one "=" equal to sign, and when we have to compare we use two "==" equal to
#sign
#eg.assignment
a = 10
b = 20
#eg. comparission
if a == b :
    print("true")
else: 
    print("false")


# In[16]:


###7
#the three blocks in this code are

spam = 0
if spam == 10: #block one
    print('eggs')
if spam > 5: #block two
    print('bacon')
else: #block three
    print('ham')
    print('spam')
    print('spam')


# In[18]:


###8
spam = int(input("enter the number"))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("greetings")


# In[19]:


###9
#If the programme is stuck in an endless loop we press, ctrl + c


# In[21]:


###10
#The key difference between break and continue statements is that, the break statement breaks the loop
#immidieately and continue statement begins another operation after executed.


# In[22]:


###11
#In for loop range(10) means the loop will be executed 10 times considering the range from 0 to 9
#In range(0,10) the loop will again be executed 10 times considering 0 to 9
#In rnage(0,10,1) the loop will be executed by jumping 1 step from 0 to 10


# In[26]:


for i in range(10):
    print(i)


# In[27]:


for i in range(0,10):
    print(i)


# In[28]:


for i in range(0,10,1):
    print(i)


# In[30]:


###12
for i in range(1,11):
    print(i)


# In[35]:


i = 1
while range(i,11):
    print(i)
    i=i+1
    


# In[ ]:


###13
#to call becon() function after importing spam module we use (.) doperator along with the module name
#spam.bacon()

