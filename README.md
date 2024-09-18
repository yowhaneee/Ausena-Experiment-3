## EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)

Instructions:
Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin.

For this programming assignment, download the following file and save to your default user folder:
http://bit.ly/Cars_file

### PROBLEM 1: 

Using knowledge obtained from the experiment and demonstrations:

a. Load the corresponding .csv file into a data frame named cars using pandas

b. Display the first five and last five rows of the resulting cars

### Code:

```python
    # Start
  
    import pandas as pd # Import the pandas library

    # a. Load the corresponding .csv file into a data frame named cars using pandas
    cars = pd.read_csv('cars.csv') # Read the 'cars.csv' file and load it into a DataFrame called 'cars'
    cars

    # b. Display the first 5 rows of the Cars 
    cars.head() # Display the first 5 rows of the Cars 

    # b. Display the first 5 rows of the Cars 
    cars.tail() # Display the last 5 rows of the Cars
    
    # End
```


### PROBLEM 2: 

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

### Code:
```python
    # Start
  
    import pandas as pd # Import the pandas library
    
    cars = pd.read_csv('cars.csv') # Read the 'cars.csv' file and load it into a DataFrame called 'cars'
    cars

    # a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
    cars.iloc[0:5, 1::2] # Display the first 5 rows (index 0 to 4) with odd-numbered columns (starting from column 1 and skipping every other column)

    df = cars # Declare the cars as df
    df

    # b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
    df.loc[df['Model']=='Mazda RX4'] # Display the row that contains 'Model' of 'Mazda      RX4'

    # c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
    df.loc[[23],['Model', 'cyl']] # Look for the 'Camaro Z28' model and its cyl

    # Another way to know the value of cyl in the car model 'Camaro Z28' 
    df.loc[df['Model'] == 'Camaro Z28']['cyl'].values[0] # Get the number of cylinders  for the 'Camaro Z28' model (this condition is more specific, giving the exact value of cyl)      

    # d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazd RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
    # Filter rows for specific models and display 'cyl' and 'gear' columns
    df.loc[df['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])][['Model', 'cyl', 'gear']]

    # End
```



