# Install these 2 libraries if not installed.
#1. Pandas 2. mlxtend
# pip install pandas
# pip install mlxtend
# Importing required libraries
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd

# Sample transaction data
data = {'Transaction_ID': [1, 2, 3, 4, 5],
        'Items': [['Milk', 'Bread', 'Butter'],
                  ['Milk', 'Bread', 'Butter', 'Eggs'],
                  ['Bread', 'Butter', 'Eggs'],
                  ['Milk', 'Eggs'],
                  ['Milk', 'Bread', 'Eggs']]}

# Creating DataFrame from transaction data
df = pd.DataFrame(data)

# Transforming the transaction data into a one-hot encoded DataFrame
df_encoded = df['Items'].str.join('|').str.get_dummies()

# Applying Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df_encoded, min_support=0.5, use_colnames=True)

# Generating association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Displaying frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# Displaying association rules
print("\nAssociation Rules:")
print(rules)
