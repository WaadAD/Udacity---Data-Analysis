#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: Investigate a Dataset - TMDb Movie Data
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# In this project I will be analyzin dataset the's associated with "TMDB Movies" , This dataset contains huge information about movies that are collected from the Movie Database (TMDb).
# 
# I'm very interested to find more about the movie ratings and revenue.
# 

# In[5]:


# set up import statements for all of the packages 
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# to start, i will import all the packes that i will need in this project.

# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# ### General Properties
# First of all I'm starting with loading the dataset and then reading the 5 first rows to undrstand data more.

# In[6]:


# Load data and print out a few lines. 
df = pd.read_csv('tmdb-movies.csv')
df.head()


# then, will look for more information about the data. 

# In[7]:


df.shape


# It shows that the data continue 10866 rows and 21 columns

# In[8]:


df.info()


# the shown data above shows there is some mising values as well as wrong data type for the (relase data).

# In[9]:


df.describe()


# In[10]:


#check null value
df.isnull().sum()


# as shown there is a lot of mising values.

# In[11]:


#check duplicate value
df.duplicated().sum()


# there is one duplication in the rows 

# after assessing, it shows that there is some wrong data type and missing valus also some duplicated data.

# 
# ### Data Cleaning
# First:I will be removing the duplicated row.

# In[12]:


df.drop_duplicates(inplace=True)


# In[13]:


#checking after removing duplicated data.

sum(df.duplicated())


# Second:I will fill the missing values

# In[14]:


df = df.fillna(0)


# In[15]:


#checking after filling the missing values.
df.info()


# Third: I will change the data type of the release_date from object to datetime
# 

# In[16]:


df['release_date'] = pd.to_datetime(df['release_date'])


# In[17]:


#checking after changing the data type.
df['release_date'].head()


# Fouth: I will remove the column that i dont need.

# In[18]:


df.drop(['imdb_id', 'homepage', 'overview', 'budget_adj','revenue_adj'], axis = 1, inplace = True)


# In[19]:


#checking after drop column
df.head()


# Fifth: I will be using the first movie category intsed of having multible category by grouping them it will help me to classfiy the movie much easier.

# In[20]:


df['genres'] =df['genres'].str.split('|', expand=True)


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# 
# ### General look

# In[21]:


df.hist(figsize=(10,10));


# ### Research Question 1 (what year has most movie releasing ?)

# In[22]:



df['release_year'].value_counts().plot(title='Number Of relased Movies per Year',kind='bar',fontsize = 12 ,figsize=(12,12));

plt.ylabel('Number Of Movies',fontsize = 13)
plt.xlabel('year',fontsize = 13 )


# the above chart shows that 2014 has the most movie releasing.

# In[23]:


df['release_year'].value_counts().head(3)


# ### Research Question 2 (what the highest prdouced movie genres ?)

# In[24]:


#will shows the count of each movie category
df['genres'].value_counts()


# In[25]:


df['genres'].value_counts().plot(title='Number of produced Movie Category',kind='bar',fontsize = 12 ,figsize=(12,12),color="b");

plt.ylabel('Count',fontsize = 13)
plt.xlabel('Category',fontsize = 13 )


# it show that hightest movie catgory production is drama with 2453.

# ### Research Question 3 (Does the highest prdouced movie have the highest popularity ?)

# In[26]:


df.groupby('genres')['popularity'].mean().sort_values(ascending=False)


# the highest produced movie catgory was "drama" but it shows that the highest pupolority end to be "Adventure".

# ### Research Question 4 (Does the highest prdouced movie have the highest vote ?)

# In[27]:


a = df.groupby('genres')['vote_count'].mean().sort_values(ascending=False)
print(a)


# In[28]:


plt.subplots(figsize=(25, 10))
plt.bar(a.index, a ,color="b")
plt.title('Vote Count by Genres',fontsize = 30)
plt.xlabel('genres',fontsize = 30)
plt.ylabel('votes',fontsize = 30)


# As shown above the highest vote was for both Adventure,Science Fiction.

# ### Creating functions 

# In[29]:


#creating a function that will help us to find the average of selected column
def avg_find(x):
    return df[x].mean()


# In[30]:


avg_find('revenue')


# In[33]:


avg_find('budget')


# <a id='conclusions'></a>
# ## Conclusions
# 
# 1- the most movie production was in 2014 with 700 movie. <br>
# 2- there was high continous movie production between the years 2012~2015.<br>
# 3- the charts shows that the movie production is continously increasing by the years.<br>
# 4- the highest produced movie end to be drama genres.<br> 
# 5- the highest vote were Adventure and the lowest is foreign.<br>
# 6- the most popular is Adventure and the last is also foreign.<br>
# 7- in term of publishing the drama take the firt place however it doent take place in both popularity and voting.<br>
# 
# ## Limitaions
# 1-there was huge amount of missing vlaues <br>
# 2-some wrong data type<br>
# 3-few duplications <br>
# 
# 
# 
# 
# 

# In[31]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

