# importing libaries to use
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10, 6]
plt.xlabel("Confidence(%)")
plt.ylabel("Rule count")
plt.title("Support level of 9%")
data = pd.read_csv("C:\BreadBasket_DMS.csv")

data = data.set_index(['Item'])
filtered = data.drop(['NONE'])
data = data.reset_index()
filtered = filtered.reset_index()
transaction_list = []

for i in filtered['Transaction'].unique():
    trans_list = list(set(filtered[filtered['Transaction'] == i]['Item']))
    if len(trans_list) > 0:
        transaction_list.append(trans_list)

t_encoder = TransactionEncoder()
te_ary = t_encoder.fit(transaction_list).transform(transaction_list)
df2 = pd.DataFrame(te_ary, columns=t_encoder.columns_)

print("SOLUTION-4 ")
frequent_itemsets = apriori(df2, min_support=0.05, use_colnames=True)
rule1 = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.0001)
rule1.sort_values('confidence', ascending=False)
rule1['support'] = rule1['support'] * 100
rule1['confidence'] = rule1['confidence'] * 100
rule2 = rule1[['antecedents', 'consequents', 'support', 'confidence']]
rule2.sort_values('confidence', ascending=False)
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print("Support Level of 5%: \n")
print("Confidence       count")
print(rule2['confidence'].value_counts(bins=bins, sort=False))
rule2['confidence'].value_counts(bins=bins, sort=False).plot(kind='bar')
plt.show()

print("SOLUTION-5 ")
frequent_itemsets = apriori(df2, min_support=0.01, use_colnames=True)
rule1 = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.0001)
rule1.sort_values('confidence', ascending=False)
rule1['support'] = rule1['support'] * 100
rule1['confidence'] = rule1['confidence'] * 100
rule2 = rule1[['antecedents', 'consequents', 'support', 'confidence']]
rule2.sort_values('confidence', ascending=False)
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print("Support Level of 1%: \n")
print("Confidence       count")
print(rule2['confidence'].value_counts(bins=bins, sort=False))
rule2['confidence'].value_counts(bins=bins, sort=False).plot(kind='bar')
plt.show()

print("SOLUTION 6 ")
frequent_itemsets = apriori(df2, min_support=0.005, use_colnames=True)
rule1 = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.0001)
rule1.sort_values('confidence', ascending=False)
rule1['support'] = rule1['support'] * 100
rule1['confidence'] = rule1['confidence'] * 100
rule2 = rule1[['antecedents', 'consequents', 'support', 'confidence']]
rule2.sort_values('confidence', ascending=False)
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print("Support Level of 0.5%: \n")
print("Confidence       count")
print(rule2['confidence'].value_counts(bins=bins, sort=False))
rule2['confidence'].value_counts(bins=bins, sort=False).plot(kind='bar')
plt.show()

print("solution-7")
frequent_itemsets = apriori(df2, min_support=0.01, use_colnames=True)
rule1 = association_rules(frequent_itemsets, metric='lift')
rule1.sort_values('confidence', ascending=False)
print("Rules:\n")
print(rule1.head(5))
print("\n")
rule1['support'] = rule1['support'] * 100
rule1['confidence'] = rule1['confidence'] * 100
rule1['lift'] = rule1['lift']
rule2 = rule1[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
rule2 = rule2.sort_values('confidence', ascending=False)
print("pairs with best confidence: \n")
print(rule2.head())
print("\n")
rule2 = rule2.sort_values('support', ascending=False)
print("pairs with best support: \n")
print(rule2.head())
print("\n")
print("As We can see from the above tables, The best possible pairs would be Cake & Coffee, Paestry & Cake\n")
rule2 = rule2.sort_values('confidence', ascending=False)
print("pairs with worst confidence: \n")
print(rule2.tail())
print("\n")
rule2 = rule2.sort_values('lift', ascending=False)
print("pairs with best lift: \n")
print(rule2.head())
print("\n")
rule2 = rule2.sort_values('lift', ascending=False)
print("pairs with worst lift: \n")
print(rule2.tail())
print("\n")
rule3 = rule2.set_index('confidence')
rule4 = rule3.sort_index()
finalrule = rule4.reset_index()
finalrule["antecedents"] = finalrule["antecedents"].apply(lambda x: list(x)[0]).astype("unicode")
finalrule["consequents"] = finalrule["consequents"].apply(lambda x: list(x)[0]).astype("unicode")
finalrule['combination'] = finalrule['antecedents'] + " And " + finalrule['consequents']
finalrule = finalrule.drop_duplicates()
print("All the pairs with minimum support their confidence: \n")
finalrule.plot(x='combination', y='confidence', kind='bar', color='blue')
plt.rcParams["figure.figsize"] = [10, 6]
plt.ylabel("Confidence(%)")
plt.title("Optimal Pairs wrt optimal support-confidence")
plt.show()
