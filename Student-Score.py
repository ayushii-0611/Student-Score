#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


df=pd.read_csv("Student_Score.csv")
print(df.head())


# In[8]:


df.describe()


# In[9]:


df.info()


# In[10]:


df.isnull().sum()


# # drop unnamed column

# In[11]:


df=df.drop("Unnamed: 0",axis=1)
print(df.head())


# # Change Weekly Study Hours

# In[13]:


df["WklyStudyHours"]=df["WklyStudyHours"].str.replace("05-Oct","5-10")
df.head()


# # Gender Distribution

# In[25]:


plt.figure(figsize=(4,4))
ax=sns.countplot(data=df,x="Gender")
plt.title("General Distribution")
ax.bar_label(ax.containers[0])
plt.show()


# In[ ]:


#from the above chart we have analysed that:
#the number of females in the data is more than the number of males


# In[18]:


gb=df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)


# In[26]:


plt.figure(figsize=(4,4))
sns.heatmap(gb,annot=True)
plt.title("Relationship between ParentsEdu and Student Scores")
plt.show()


# In[ ]:


#from the above chart we have concluded that the education of the parents have a good impact on their scores 


# In[22]:


gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb1)


# In[27]:


plt.figure(figsize=(4,4))
sns.heatmap(gb1,annot=True)
plt.title("Relationship between Parents Marital Status and Student Scores")
plt.show()


# In[ ]:


#from the above chart we have concluded that there is neglibigle impact on their scores due to there marital status


# In[29]:


sns.boxplot(data=df,x="MathScore")
plt.show()


# In[30]:


sns.boxplot(data=df,x="ReadingScore")
plt.show()


# In[31]:


sns.boxplot(data=df,x="WritingScore")
plt.show()


# In[33]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Groups

# In[45]:


groupA=df.loc[(df["EthnicGroup"]=="group A")].count()
groupB=df.loc[(df["EthnicGroup"]=="group B")].count()
groupC=df.loc[(df["EthnicGroup"]=="group C")].count()
groupD=df.loc[(df["EthnicGroup"]=="group D")].count()
groupE=df.loc[(df["EthnicGroup"]=="group E")].count()

l =["group A","group B","group C","group D","group E"]

print(mylist)
mylist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.pie(mylist,labels=l,autopct="%1.2f%%")
plt.title("Distribution of Groups")
plt.show()


# In[46]:


ax=sns.countplot(data=df,x="EthnicGroup")
ax.bar_label(ax.containers[0])


# In[ ]:





# In[ ]:





# In[ ]:




