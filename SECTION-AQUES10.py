import pandas as pd
import matplotlib.pyplot as plt

print('SECTION-A QUESTION 10')

plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Week Days")
plt.ylabel("Sales")

data = pd.read_csv(r"C:\BreadBasket_DMS.csv")

data = data.set_index(['Item'])
data = data.drop(['NONE'])
data.reset_index(inplace=True)

bread = data['Item'] == 'Bread'
breadbasket_data = data[bread]

assert isinstance(breadbasket_data, object)
breadbasket_data['Date'] = pd.to_datetime(breadbasket_data['Date'], format='%d-%m-%Y', errors='coerce')
breadbasket_data['weekday'] = breadbasket_data['Date'].dt.weekday
sales = breadbasket_data['weekday'].value_counts()
new_sales = sales.sort_index()
rename_data = new_sales.rename(
    index={0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'})

print("\nBreads sold per weekday: \n")

print(rename_data)

average = rename_data.sum() / 7
print("\nThe number of average transactions of bread per weekday: " + str(average) + "\n")

rename_data.plot(kind='line', marker='o')

plt.show()
