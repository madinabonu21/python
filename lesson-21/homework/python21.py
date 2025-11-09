import pandas as pd
import matplotlib.pyplot as plt

# Данные
data1 = {
    'Student_ID': [1,2,3,4,5,6,7,8,9,10],
    'Math': [85,90,78,92,88,95,89,79,83,91],
    'English': [78,85,88,80,92,87,90,84,79,88],
    'Science': [90,92,85,88,94,79,83,91,87,89]
}
df1 = pd.DataFrame(data1)

# Exercise 1: Средний балл каждого студента
df1['Average'] = df1[['Math','English','Science']].mean(axis=1)
print("Average grade for each student:")
print(df1[['Student_ID','Average']])

# Exercise 2: Студент с самым высоким средним баллом
top_student = df1.loc[df1['Average'].idxmax()]
print("\nStudent with highest average grade:")
print(top_student[['Student_ID','Average']])

# Exercise 3: Создание колонки Total
df1['Total'] = df1[['Math','English','Science']].sum(axis=1)
print("\nDataFrame with Total marks:")
print(df1)

# Exercise 4: Барчарт по средним баллам предметов
subject_avg = df1[['Math','English','Science']].mean()
subject_avg.plot(kind='bar', title='Average Grades per Subject', ylabel='Average Grade')
plt.show()


# Данные
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120,150,130,110,140,160,135,125,145,155],
    'Product_B': [90,110,100,80,95,105,98,88,102,112],
    'Product_C': [75,80,85,70,88,92,78,82,87,90]
}
df2 = pd.DataFrame(data2)

# Exercise 1: Суммарные продажи каждого продукта
total_sales = df2[['Product_A','Product_B','Product_C']].sum()
print("Total sales for each product:")
print(total_sales)

# Exercise 2: Дата с наибольшими продажами
df2['Total_Sales'] = df2[['Product_A','Product_B','Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(),'Date']
print("\nDate with highest total sales:", max_sales_date)

# Exercise 3: Процентное изменение продаж для каждого продукта
pct_change = df2[['Product_A','Product_B','Product_C']].pct_change()*100
print("\nPercentage change in sales from previous day:")
print(pct_change)

# Exercise 4: Линейный график по продажам
df2.plot(x='Date', y=['Product_A','Product_B','Product_C'], kind='line', marker='o', title='Sales Trends')
plt.ylabel('Sales')
plt.show()



# Данные
data3 = {
    'Employee_ID': [101,102,103,104,105,106,107,108,109,110],
    'Name': ['Alice','Bob','Charlie','David','Emma','Frank','Grace','Hank','Ivy','Jack'],
    'Department': ['HR','IT','Marketing','IT','Finance','HR','Marketing','IT','Finance','Marketing'],
    'Salary': [60000,75000,65000,80000,70000,72000,68000,78000,69000,76000],
    'Experience (Years)': [3,5,2,8,4,6,3,7,2,5]
}
df3 = pd.DataFrame(data3)

# Exercise 1: Средняя зарплата по отделам
avg_salary = df3.groupby('Department')['Salary'].mean()
print("Average salary per department:")
print(avg_salary)

# Exercise 2: Сотрудник с наибольшим опытом
most_exp = df3.loc[df3['Experience (Years)'].idxmax()]
print("\nEmployee with most experience:")
print(most_exp[['Name','Experience (Years)']])

# Exercise 3: Процентное увеличение зарплаты относительно минимальной
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary)/min_salary)*100
print("\nDataFrame with Salary Increase:")
print(df3[['Name','Salary','Salary Increase (%)']])

# Exercise 4: Барчарт распределения сотрудников по отделам
dept_count = df3['Department'].value_counts()
dept_count.plot(kind='bar', title='Employees per Department', ylabel='Number of Employees')
plt.show()


# Данные
data4 = {
    'Order_ID': [101,102,103,104,105,106,107,108,109,110],
    'Customer_ID': [201,202,203,204,205,206,207,208,209,210],
    'Product': ['A','B','A','C','B','C','A','C','B','A'],
    'Quantity': [2,3,1,4,2,3,2,5,1,3],
    'Total_Price': [120,180,60,240,160,270,140,300,90,180]
}
df4 = pd.DataFrame(data4)

# Exercise 1: Общая выручка
total_revenue = df4['Total_Price'].sum()
print("Total revenue from all orders:", total_revenue)

# Exercise 2: Самый заказанный продукт
most_ordered = df4.groupby('Product')['Quantity'].sum().idxmax()
print("Most ordered product:", most_ordered)

# Exercise 3: Среднее количество товаров в заказе
avg_quantity = df4['Quantity'].mean()
print("Average quantity per order:", avg_quantity)

# Exercise 4: Круговая диаграмма по распределению продаж
sales_per_product = df4.groupby('Product')['Total_Price'].sum()
sales_per_product.plot(kind='pie', autopct='%1.1f%%', title='Sales Distribution by Product')
plt.ylabel('')
plt.show()
