#!/usr/bin/env python
# coding: utf-8

# ## Problem 1:

# Using knowledge obtained from the experiment and demonstrations:
# 
# a. Load the corresponding .csv file into a data frame named cars using pandas
# 
# b. Display the first five and last five rows of the resulting cars

# In[62]:


# Start


# In[63]:


import pandas as pd # Import the pandas library


# In[64]:


# a. Load the corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('cars.csv') # Read the 'cars.csv' file and load it into a DataFrame called 'cars'
cars


# In[65]:


cars.head() # b. Display the first 5 rows of the Cars 


# In[66]:


cars.tail() # b. Display the last 5 rows of the Cars


# In[67]:


# End

