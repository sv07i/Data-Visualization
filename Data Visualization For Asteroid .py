#!/usr/bin/env python
# coding: utf-8

# Name : Patel Yash Shaileshkumar
# 
# 
#     

# Enrollment Number : 20MSCPHY22034

# Course : MSC PHYSICS

# Sem : 2

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


# In[5]:


data = pd.read_csv("impacts.csv")
data


# In[6]:


data.info()


# In[7]:


data.describe()


# In[8]:


data.head()


# In[41]:


data['.s'].sort_values(ascending=False).head().plot(kind="barh")


# In[10]:


data["Asteroid Diameter (km)"].value_counts().head().plot(kind="pie")


# In[11]:


data['Asteroid Velocity'].plot(kind="hist")


# In[12]:


data['Asteroid Magnitude'].plot(kind="hist")


# In[13]:


data[["Object Name" ,"Period Start", "Period End"]]


# In[14]:


data.iloc[0]


# In[15]:


data.iloc[:,[0,1,2]]


# In[16]:


runs=data.groupby("Object Name")


# In[17]:


v1= runs["Possible Impacts"].sum().sort_values(ascending=False).head().plot(kind="pie")
v1


# In[18]:


runs["Possible Impacts"].sum().sort_values(ascending=False).shape






















# In[ ]:





# In[44]:


vk = data.groupby("Object Name")
v2 = vk["Asteroid Velocity"].sum().sort_values(ascending=False).head().plot(kind="pie")
v2


# In[45]:


vk = data.groupby("Object Name")
v2 = vk["Asteroid Magnitude"].sum().sort_values(ascending=False).head().plot(kind="pie")
v2


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


sns.displot(data["Possible Impacts"])
plt.show()


# In[46]:


sns.heatmap(data.corr(), annot = True)


# In[47]:


x = data["Asteroid Velocity"]
y = data["Asteroid Magnitude"]
sns.regplot(x,y)


# In[ ]:




