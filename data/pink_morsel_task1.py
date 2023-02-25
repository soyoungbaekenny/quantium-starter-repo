import pandas as pd
import csv
# df = pd.concat(map(pd.read_csv, ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']),ignore_index=True)
# print(df)
# #df = pd.read_csv("daily_sales_data_0.csv")
# pink_morsel_only = df[(df['product'] == 'pink morsel')]
# print(pink_morsel_only)
# pink_morsel_only.to_csv('Pink_Morsel_Sales.csv')


# df = pd.read_csv("Pink_Morsel_Sales.csv")
# price = df['price'].replace('[\$,]', '', regex=True)
# df['price'] = price
# df['sales'] = df['price'].astype(float) * df['quantity'].astype(float)
# print(df)
# df.to_csv('sales_per_date.csv')

df = pd.read_csv("sales_per_date.csv")
new_frame = (df[['sales', 'date', 'region']])
print(new_frame.sort_values(['region', 'date'], ascending=[False,True]))
df.to_csv('final.csv')




