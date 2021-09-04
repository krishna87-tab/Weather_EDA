#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[100]:


df = pd.read_csv('1. Weather Data.csv')


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.index


# In[6]:


df.columns


# In[7]:


df.dtypes


# In[8]:


df['Weather'].unique() #shows unique values in a single column


# In[9]:


df['Weather'].nunique() #shows unique values in a single column


# In[10]:


df.nunique() #shows unique values in a dataframe


# In[11]:


df.count() #shows total number of non-null values in each column


# In[12]:


df['Weather'].value_counts() #return a Series containing counts of unique values


# In[13]:


df.info()


# In[14]:


#To find the unique 'Wind Speed'

df['Wind Speed_km/h'].nunique()


# In[15]:


df['Wind Speed_km/h'].unique() #Answer


# In[16]:


#Find the number of times when the 'Weather is exactly Clear'

df['Weather'].value_counts()


# In[17]:


#filtering method
df.head(2)


# In[18]:


df[df.Weather == 'Clear']


# In[19]:


df.groupby('Weather').get_group('Clear')


# In[20]:


#To find the number of times when 'Wind Speed was exactly 4 km/h'

df.head(2)


# In[21]:


df[df['Wind Speed_km/h'] == 4]


# In[22]:


#Find the null values in the data
df.isnull().sum()


# In[23]:


df.notnull().sum()


# In[24]:


#Rename the column name 'Weather' to 'Weather Condition'

df.head(2)


# In[25]:


df.rename(columns = {'Weather':'Weather Condition'}).head(2)


# In[26]:


df.rename(columns = {'Weather':'Weather Condition'},inplace = True)


# In[27]:


# What is the mean 'Visibility'?

df['Visibility_km'].mean()


# In[28]:


#What is the Standard Deviation of 'Pressure'?
df['Press_kPa'].std()


# In[30]:


# what is the variance of 'Relative Humidity'?
df['Rel Hum_%'].var()


# In[31]:


#Find all instance when "Snow" was recorded.
df['Weather Condition'].value_counts()


# In[32]:


#filtering
df[df['Weather Condition'] == 'Snow']


# In[33]:


#str.contains

df[df['Weather Condition'].str.contains('Snow')]


# In[34]:


#Find all instance when 'Wind Speed is above 24' and 'Visibility is 25'

df.head(2)


# In[35]:


df[(df['Wind Speed_km/h']>24)&(df['Visibility_km'] == 25)]


# In[36]:


#What is the Mean value of each column against each 'Weather Condition'?

df.columns


# In[37]:


df.groupby('Weather Condition').mean()


# In[38]:


#What is the Min and Max value of each column in 'Weather Condition'?

df.groupby('Weather Condition').max()


# In[39]:


df.groupby('Weather Condition').min()


# In[40]:


#Show all records where Weather Condition is Fog'

df[df['Weather Condition'] == 'Fog']


# In[41]:


#Find instance when 'Weather is clear' or 'Visibility is above 40'

df[(df['Weather Condition'] == 'Clear') | (df['Visibility_km'] > 40)]


# In[42]:


#Find all instance when
#Weather is Clear and Relative Humidity if greater than 50
#or
#Visibility is above 40


df[(df['Weather Condition'] == 'Clear') & (df['Rel Hum_%'] > 50) | (df['Visibility_km'] > 40)]


# In[45]:


df[(df['Wind Speed_km/h']>24)&(df['Visibility_km'] == 25)].head(3)


# In[56]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
sns.set_style("darkgrid")


# In[86]:


windspeed = df['Wind Speed_km/h']
visibility = df['Visibility_km']
Temperature = df['Temp_C']
Humidity = df['Rel Hum_%']


# In[60]:


plt.figure(figsize=(12, 6))
sns.scatterplot(x=windspeed, y = visibility,hue=Temperature);


# In[80]:


df['year']   =  pd.DatetimeIndex(df['Date/Time']).year
df['month']  =  pd.DatetimeIndex(df['Date/Time']).month
df['day']    =  pd.DatetimeIndex(df['Date/Time']).day
df['Weather Condition'] = df['Weather Condition'].astype('str') 


# In[81]:


year_weather = df['year']
weather_conditions = df['Weather Condition']


# In[92]:


plt.figure(figsize=(12, 10))
plt.bar(windspeed, Temperature);
plt.xlabel('Wind-speed')
plt.ylabel('Temperature')
plt.title('Weather Change');


# In[112]:


sns.set_theme(style="ticks")
sns.pairplot(df,hue = 'Visibility_km');


# In[116]:


df.head(2)


# In[119]:


plt.figure(figsize=(16, 14))
sns.set_theme(style="whitegrid")

cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(data=df, x="Temp_C", y="Press_kPa",hue="Visibility_km", size="Wind Speed_km/h",
    palette=cmap, sizes=(10, 200),
)
g.set(xscale="log", yscale="log")
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)

