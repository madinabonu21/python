# Homework Assignment 1: Analyzing Sales Data


# 1 Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction.
import pandas as pd

df = pd.read_csv("sales_data.csv")

category_group = df.groupby('Category')

# Считаем суммарное количество, среднюю цену и максимальное количество
total_quantity = category_group['Quantity'].sum()           # суммарное количество проданных единиц
average_price = category_group['Price'].mean()             # средняя цена за единицу
max_quantity = category_group['Quantity'].max()            # максимальное количество в одной транзакции

# Объединяем в один DataFrame
category_summary = pd.DataFrame({
    'Total Quantity Sold': total_quantity,
    'Average Price': average_price,
    'Max Quantity in Single Transaction': max_quantity
})



# 2 Identify the top-selling product in each category based on the total quantity sold.

product_group = df.groupby(['Category', 'Product'])['Quantity'].sum()

# Для каждой категории выбираем продукт с наибольшим количеством
top_products = product_group.groupby('Category').idxmax()

# 3 Find the date on which the highest total sales (quantity * price) occurred.

df['Total_Sales'] = df['Quantity'] * df['Price']

# Суммируем выручку по датам
sales_by_date = df.groupby('Date')['Total_Sales'].sum()

# Находим дату с максимальной выручкой
max_sales_date = sales_by_date.idxmax()
max_sales_value = sales_by_date.max()





# Homework Assignment 2: Examining Customer Orders
import pandas as pd 

df = pd.read_csv('customer_orders.csv')

# 1)Group the data by CustomerID and filter out customers who have made less than 20 orders.

cnt = df.groupby('CustomerID').size().reset_index(name= 'order_cnt')
customer_20 = cnt[cnt['order_cnt'] >= 20 ]
print(customer_20)

# 2)Identify customers who have ordered products with an average price per unit greater than $120.   

avg = df.groupby('CustomerID')['Price'].mean().reset_index(name= 'avg_price')
customer_avg = avg[avg['avg_price'] > 120]

print(customer_avg)


# 3 Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

product_summary = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Price', lambda x: (x * df.loc[x.index, 'Quantity']).sum())
).reset_index()

# Фильтруем продукты с количеством >= 5
product_filtered = product_summary[product_summary['Total_Quantity'] >= 5]

print(product_filtered)
