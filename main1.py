import pandas as pd

products = ['apples', 'bananas', 'oranges', 'grapes']
sales = [100,200,300,400]

sales_series = pd.Series(sales, index=products)
print(sales_series)

print(sales_series['grapes'])
total_sales = sales_series.sum()
print(total_sales)

best_selling_product = sales_series.idxmax()
print(f"Best selling product:{best_selling_product}")

# data = { 'Name':['Medina', 'Lisa', 'Une'],
#         'Age' : [10,12,13],
#         'City' : ['Prishtine', 'Peja', 'Gjakove']
        
# }

# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv('cs.csv')

# df.to_csv('output_database.csv', index = False)