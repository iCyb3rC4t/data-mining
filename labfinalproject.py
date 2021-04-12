#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


df = pd.read_csv(r'C:\Users\GAMING PC\Documents\Collage Docs\heart.csv')


# In[9]:


df.head()


# In[10]:


df.describe()


# In[11]:


df.isnull().sum()


# In[12]:


print(df.info())


# In[15]:


plt.figure(figsize=(20,10))
sns.heatmap(df.corr(),annot=True,cmap='terrain')


# In[16]:


sns.pairplot(data=df)


# In[17]:


df.hist(figsize=(12,12),layout=(5,3));


# In[18]:


df.plot(kind='box',subplots=True ,layout=(5,3),figsize=(12,12))
plt.show()


# In[19]:


sns.catplot(data=df , x='sex',y='age',hue='target',palette='husl')


# In[20]:


sns.barplot(data=df,x='sex',y='chol',hue='target',palette='spring')


# In[21]:


df['sex'].value_counts()


# In[22]:


df['target'].value_counts()


# In[23]:


df['thal'].value_counts()


# In[24]:


df.plot(kind='box', subplots=True, layout=(5,3), figsize=(12,12))
plt.show()
sns.catplot(data=df, x='sex', y='age', hue='target', palette='husl')


# In[25]:


sns.countplot(x='sex', data=df, palette='husl', hue='target')


# In[26]:


sns.countplot(x='target', palette='BuGn', data=df)


# In[27]:


df = pd.read_csv(r'C:\Users\GAMING PC\Documents\Collage Docs\heart.csv')


# In[28]:


sns.countplot(x='ca', hue='target', data=df)


# In[29]:


sns.countplot(x='thal', data=df, hue='target', palette='BuPu')


# In[30]:


sns.countplot(x='thal', hue='sex', data=df, palette='terrain')


# In[31]:


df['cp'].value_counts()


# In[32]:


sns.countplot(x='cp', hue='target', data=df, palette='rocket')


# In[33]:


sns.countplot(x='cp', hue='sex', data=df, palette='BrBG')


# In[34]:


sns.boxplot(x='sex', y='chol', hue='target', palette='seismic', data=df)


# In[35]:


sns.boxplot(x='sex', y='thal', hue='target', palette='seismic', data=df)


# In[36]:


sns.boxplot(x='target', y='ca', hue='sex', palette='seismic', data=df)


# In[37]:


sns.barplot(x='sex', y='cp', hue='target', data =df, palette='seismic')


# In[38]:


temp=pd.crosstab(index=df['sex'],
                 columns=[df['thal']],
                 margins=True)
                 
temp


# In[ ]:




