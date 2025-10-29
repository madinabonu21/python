import pandas as pd 

# Homework 1:
# 1. Rename column names using function. "First Name" --> "first_name", "Age" --> "age

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df.rename(columns={'First Name' : 'first_name', 'Age' : 'age'}))


# 2. Print the first 3 rows of the DataFrame

print(df.head(3))


# 3.Find the mean age of the individuals

print(df['Age'].mean())


# 4.Select and print only the 'Name' and 'City' columns

print(df[['First Name','City']])


# 5.Add a new column 'Salary' with random salary values

df['Salary'] = [19000,40000,3700,60000]
print(df)

# 6.Display summary statistics of the DataFrame

print(df.describe())

# Homework 2:

# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. 

my_dict = {'Month': ['Jan','Feb','Mar','Apr'], 'Sales': [5000,6000,7500,8000], 'Expenses': [3000,3500,4000,4500]}

sales_and_expenses = pd.DataFrame(my_dict)


# # 1.Calculate and display the maximum sales and expenses.

max_salexp = sales_and_expenses[['Sales', 'Expenses']].max()
print(max_salexp)

# # 2.Calculate and display the minimum sales and expenses.

min_salexp = sales_and_expenses[['Sales','Expenses']].min()
print(min_salexp)

# # 3.Calculate and display the average sales and expenses.

avg_salexp = sales_and_expenses[['Sales','Expenses']].mean()
print(avg_salexp)



# Homework 3:

# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories.

my_df = {'Category': ['January' , 'February' , 'March', 'April'], 'Rent': [1200	,1300,1400,1500], 'Utilities':	[200 ,220,240,250] , 'Groceries':	[300,320,330,350],  'Entertainment':	[150, 160 , 170	,180]}

expenses = pd.DataFrame(my_df)
expenses.set_index('Category')


# Calculate and display the maximum expense for each category.

max_exp = expenses[['Rent','Utilities','Groceries','Entertainment']].max()
print(max_exp)

# Calculate and display the minimum expense for each category.

min_exp = expenses[['Rent','Utilities','Groceries','Entertainment']].max()
print(min_exp)

# Calculate and display the average expense for each category.

avg_exp = expenses[['Rent','Utilities','Groceries','Entertainment']].mean()
print(avg_exp)
