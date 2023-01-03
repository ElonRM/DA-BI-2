import pandas as pd

df = pd.read_parquet('Data_Science_Semester3/Data_Analytics_Business_Intelligence/DA-BI-2/shopping_carts.parquet')

print(df.describe())
