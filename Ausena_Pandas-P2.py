#!/usr/bin/env python
# coding: utf-8

# ## Problem 2:

# Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
# 
# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
# 
# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
# 
# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# 
# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazd RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[ ]:


# Start


# In[4]:


import pandas as pd # Import the pandas library


# In[11]:


cars = pd.read_csv('cars.csv') # Read the 'cars.csv' file and load it into a DataFrame called 'cars'
cars


# In[15]:


# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
cars.iloc[0:5, 1::2] # Display the first 5 rows (index 0 to 4) with odd-numbered columns (starting from column 1 and skipping every other column)


# In[17]:


df = cars # Declare the cars as df
df


# In[19]:


# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
df.loc[df['Model']=='Mazda RX4'] # Display the row that contains 'Model' of 'Mazda RX4'


# In[23]:


# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
df.loc[[23],['Model', 'cyl']] # Look for the 'Camaro Z28' model and its cyl


# In[27]:


# Another way to know the value of cyl in the car model 'Camaro Z28' 
df.loc[df['Model'] == 'Camaro Z28']['cyl'].values[0] # Get the number of cylinders for the 'Camaro Z28' model  (this condition is more specific, giving the exact value of cyl)


# In[29]:


# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazd RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
# Filter rows for specific models and display 'cyl' and 'gear' columns
df.loc[df['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])][['Model', 'cyl', 'gear']] 


# In[ ]:


# End

