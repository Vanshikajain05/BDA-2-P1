import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import calendar
from datetime import datetime
import seaborn as sns

print('SECTION-A SOLUTIONS 1-9')
bakery_dataset = pd.read_csv(r"C:\BreadBasket_DMS.csv")
bakery_dataset.dropna()
bakery_dataset = bakery_dataset[bakery_dataset['Item'] != 'NONE']

bakery_dataset['Date'] = pd.to_datetime(bakery_dataset['Date'])
bakery_dataset['Time'] = pd.to_datetime(bakery_dataset['Time'])
bakery_dataset['Year'] = bakery_dataset['Date'].dt.year
bakery_dataset['Month'] = bakery_dataset['Date'].dt.month
bakery_dataset['Day'] = bakery_dataset['Date'].dt.day
bakery_dataset['Weekday'] = bakery_dataset['Date'].dt.weekday
bakery_dataset['Hour'] = bakery_dataset['Time'].dt.hour

bakery_dataset.head(10)

bakery_dataset.tail(10)


def index_and_values(ds, c):
    ds_c = ds[c].value_counts()
    a = ds_c.index.tolist()
    b = ds_c.values.tolist()
    return a, b


popular_items, popular_items_count = index_and_values(bakery_dataset, 'Item')
plt.bar(popular_items[:10], popular_items_count[:10])

print("SOLUTION-1")

plt.xlabel('Top 10 most popular Items')
plt.ylabel('Number of Transactions')
plt.show()

print("Top 10 most popular items are:", "\n", popular_items[:10])

# top items in 2016

print("SOLUTION-2")

I_year_data = bakery_dataset[bakery_dataset['Year'] == 2016]
x, y = index_and_values(I_year_data, 'Item')
plt.bar(x[:5], y[:5], label='2016')
plt.xlabel('Most popular Items')
plt.ylabel('Number of Transactions')
plt.legend()
plt.show()

print("5 most popular items in 2016 are:", "\n", I_year_data[:5])

# top items in 2017
print("SOLUTION-3")

II_year_data = bakery_dataset[bakery_dataset['Year'] == 2017]
x, y = index_and_values(II_year_data, 'Item')
plt.bar(x[:5], y[:5], label='2017')
plt.xlabel('Most popular Items')
plt.ylabel('Number of Transactions')
plt.legend()
plt.show()

print("5 most popular items in 2017 are:", "\n", II_year_data[:5])

print("SOLUTION-4")

monday = bakery_dataset[bakery_dataset['Weekday'] == 0]
item, item_count = index_and_values(monday, 'Item')

plt.bar(item[:5], item_count[:5], label='Monday')
plt.xlabel('Popular items on Monday')
plt.ylabel('Number of Transactions')
plt.show()

print("5 most popular items sold on monday are:", "\n", monday[:5])

print("SOLUTION-5")

bakery_dataset.groupby('Month')['Transaction'].nunique().plot(kind='bar', title='Number of items sold per month. ')
plt.xlabel('Months')
plt.ylabel('Number of Transactions')
plt.show()

print("SOLUTION-6")

bakery_dataset.groupby('Weekday')['Transaction'].nunique().plot(kind='bar', title='Number of items sold per weekday.')
plt.xlabel('Days')
plt.ylabel('Number of Transactions')
plt.show()

print("SOLUTION-7 ")

bakery_dataset.groupby('Hour')['Transaction'].nunique().plot(kind='bar', title='Number of items sold per hour.')
plt.xlabel('Hour')
plt.ylabel('Number of Transactions')
plt.show()

coffee = bakery_dataset[bakery_dataset['Item'].str.contains('Coffee')]['Transaction'].unique()

coffee = pd.DataFrame(coffee, columns=['Transaction'])
coff = coffee.merge(bakery_dataset, left_on='Transaction', right_on='Transaction', how='right')
coff = coff[~coff.Item.str.contains('Coffee')]['Item'].value_counts()

print("SOLUTION-8 ")

plt.figure(figsize=(10, 6))
coff[:5].plot(kind='bar')
plt.show()

print("SOLUTION-9")

bakery_dataset['Date'] = pd.to_datetime(bakery_dataset['Date'], format='%d-%m-%Y', errors='coerce')
bakery_dataset['year'] = bakery_dataset['Date'].dt.year

yeardataset = bakery_dataset.loc[bakery_dataset['year'] == 2017]

coffee = yeardataset.set_index(['Item'])
only_coffee = coffee.loc['Coffee']
only_coffee.reset_index(inplace=True)

pop = only_coffee['Date'].value_counts()
print(pop.head())
pop.head().plot(kind='line', color='orange', marker='o')
plt.xlabel('Dates')
plt.ylabel('Number of Transactions')
plt.title('Five most Coffee Sales day in 2017')
plt.show()
