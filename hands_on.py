import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import os
from local_setting import dataFilePath

sales = pd.read_csv(dataFilePath, parse_dates=['Date'])

# columnes_names = sales.columns.values
# print(columnes_names)

# Columns of Customer_Age, exploring
# print(sales['Customer_Age'].__class__)
# print('number of customers : ', len(sales['Customer_Age']))

## maximum, minimum and mean and standard deviation of customers age
# max_customers_age = sales['Customer_Age'].max()
# min_customers_age = sales['Customer_Age'].min()
# mean_customers_age = sales['Customer_Age'].mean()
# std_customers_age = sales['Customer_Age'].std()
# print(f'(max, min, mean, std) = ({max_customers_age}, {min_customers_age}, {mean_customers_age}, {std_customers_age})')

## plot graphs on features of the data
# sales['Customer_Age'].plot(kind='box', vert=False, figsize=(14, 6))
# sales['Order_Quantity'].plot(kind='hist', bins=3, figsize=(14,6))
# plt.show() # This line is necessary to display all panda plots

## How many sales per year do we have
# number_of_sales_in_a_year = sales['Year'].value_counts()
# print(number_of_sales_in_a_year)
# sales['Year'].value_counts().plot(kind='pie', figsize=(6,6))
# plt.show()

## How many sales per month do we have
# number_of_sales_in_a_month = sales['Month'].value_counts()
# print(number_of_sales_in_a_month)
# sales['Month'].value_counts().plot(kind='bar', figsize=(6,6))
# plt.show()

## Which country has the most sales quantity of sales?
# country_with_most_sales = sales['Country'].value_counts().head(1)
# sales['Country'].value_counts().plot(kind='pie', figsize=(6,6))
# plt.show()

##  Create a list of every product sold
# ['Date' 'Day' 'Month' 'Year' 'Customer_Age' 'Age_Group' 'Customer_Gender'
#  'Country' 'State' 'Product_Category' 'Sub_Category' 'Product'
#  'Order_Quantity' 'Unit_Cost' 'Unit_Price' 'Profit' 'Cost' 'Revenue']
# list_of_products_sold = sales['Product'].unique()
# print(list_of_products_sold)

## A bar plot showing the 10 most sold products (best sellers)
# sales['Product'].value_counts().head(10).plot(kind='bar', figsize=(6,6))
# plt.show()

## Can you see any relationship between Unit_Cost and Unit_Price
# sales.plot(kind='scatter', x='Unit_Cost', y='Unit_Price', figsize=(6,6))
# plt.show()

## Can you see any relationship between Order_Quantity and Profit
# sales.plot(kind='scatter', x='Order_Quantity', y='Profit', figsize=(14, 7))
# plt.show()

## Can you see any relationship between Profit per Country
# sales[['Country', 'Profit']].boxplot(by='Country', figsize=(100,6))
# plt.show()

## Can you see any relationship between the Customer_Age per Country
# sales[['Customer_Age', 'Country']].boxplot(by='Country', figsize=(10, 6))
# sales.plot(kind='scatter', x='Country', y='Customer_Age', figsize=(10, 6))
# plt.show()

## Add and calculate a new Calculated_Date column

