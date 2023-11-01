#!/usr/bin/env python
# coding: utf-8

# In[1]:


import io
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


# In[3]:


get_ipython().run_line_magic('cd', '"D:\\Imarticus\\stat\\MPG"')


# In[4]:


mp=pd.read_csv('Auto MPG Reg.csv')


# In[5]:


mp.head()


# In[6]:


mp.tail()


# In[7]:


mp.info()


# In[8]:


mp.isnull().sum()


# In[10]:


mp.horsepower=mp.horsepower.fillna(mp.horsepower.median())


# In[11]:


mp.isnull().sum()


# In[12]:


y=mp.mpg
x=mp[['cylinders','displacement','horsepower','weight','acceleration','modelyear','origin']]


# In[19]:


from sklearn.linear_model import LinearRegression


# In[20]:


reg=LinearRegression()


# In[26]:


reg.fit(x,y)


# In[27]:


reg.score(x,y)


# In[23]:


import joblib


# In[25]:


joblib.dump(reg,'reg_model.sav')


# In[ ]:




