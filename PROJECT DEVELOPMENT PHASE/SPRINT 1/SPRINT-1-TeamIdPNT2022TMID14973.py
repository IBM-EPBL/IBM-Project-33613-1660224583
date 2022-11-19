#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


df=pd.read_csv("C:/Users/NHTT/OneDrive/Desktop/airports.csv")


# In[7]:


df.continent.unique()


# In[8]:


df=df.replace("no",0)
df=df.replace("yes",1)
print(df.tail())


# In[10]:


sns.lineplot(df['latitude_deg'],df['longitude_deg'])
plt.show()


# In[11]:


print(df.shape)
n = len(pd.unique(df['name']))
d=len(pd.unique(df['type']))
print("name",n,"type",d)
df['scheduled_service'].value_counts()


# In[14]:


import plotly.express as px


# In[15]:


plt.scatter(x=df['latitude_deg'], y=df['longitude_deg'])
plt.show()


# In[16]:


df=df.replace('NaN',0)
df=df.replace('OC',1)
df=df.replace('AF',2)
df=df.replace('AN',3)
df=df.replace('EU',4)
df=df.replace('AS',5)
df=df.replace('SA',6)
print(df)


# In[19]:


plt.figure(figsize= (15,15))
sns.violinplot(x=df["continent"],y= df["type"],hue=df['scheduled_service'],split=True)


# In[21]:





# In[ ]:





# In[ ]:




