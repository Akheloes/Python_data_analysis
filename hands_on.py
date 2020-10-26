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
number_of_sales_in_a_month = sales['Month'].value_counts()
# print(number_of_sales_in_a_month)
sales['Month'].value_counts().plot(kind='bar', figsize=(6,6))
plt.show()

## Which country has the most sales quantity of sales?