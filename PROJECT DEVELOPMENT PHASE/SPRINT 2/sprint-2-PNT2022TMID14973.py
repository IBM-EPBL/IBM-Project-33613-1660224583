#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('C:/Users/NHTT/OneDrive/Desktop/airports.csv')
data.drop(["id"], axis=1, inplace=True)
data.head()


# In[3]:


data.describe()


# In[4]:


# Handling missing values


# In[5]:


data.info()


# In[6]:


data.isnull().sum()


# In[7]:


#Data Visulization


# In[8]:


plt.scatter(data['latitude_deg'],data['longitude_deg'])
plt.title('longitude_deg vs latitude_deg')
plt.xlabel('latitude_deg')
plt.ylabel('longitude_deg')
plt.show()


# In[12]:


plt.scatter(data['latitude_deg'],data['elevation_ft'])
plt.title('elevation_ft for latitude_deg')
plt.xlabel('latitude_deg')
plt.ylabel('elevation_ft')
plt.show()


# In[11]:


data[data.elevation_ft >= 2000].plot(kind='scatter', x='longitude_deg', y='elevation_ft',color="BLUE")
plt.xlabel("longitude_deg")
plt.ylabel("elevation_ft")
plt.title("elevation_ft>=2000")
plt.grid(True)
plt.show()


# In[13]:


data["longitude_deg"].plot(kind = 'hist',bins = 200,figsize = (6,6))
plt.title("longitude_deg")
plt.xlabel("longitude_deg")
plt.ylabel("scheduled_service")
plt.show()


# In[14]:


p = np.array([data["elevation_ft"].min(),data["elevation_ft"].mean(),data["elevation_ft"].max()])
r = ["Worst","Average","Best"]
plt.bar(p,r)
plt.title("elevation_ft")
plt.xlabel("Level")
plt.ylabel("elevation_ft")
plt.show()


# In[15]:


g = np.array([data["longitude_deg"].min(),data["longitude_deg"].mean(),data["longitude_deg"].max()])
h = ["Worst","Average","Best"]
plt.bar(g,h)
plt.title("longitude_deg")
plt.xlabel("Level")
plt.ylabel("longitude_deg")
plt.show()


# In[16]:


plt.figure(figsize=(10, 10))
sns.heatmap(data.corr(), annot=True, linewidths=0.05, fmt= '.2f',cmap="magma")
plt.show()


# In[ ]:





# In[ ]:




