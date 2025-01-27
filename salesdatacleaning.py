import pandas as pd

data = {

    'sales': [350, 450, 500, 600, 700],
    'region': ['North', 'South', 'East', 'West', 'Central'],
    'product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']

}

df = pd.DataFrame(data)

cleaned_df = df.dropna()

print("Cleaned DataFrame : \n", cleaned_df)

renamed_df = cleaned_df.rename(columns={'sales': 'total_sales'})
print("Renamed DataFrame : \n", renamed_df)

total_sales = renamed_df.groupby('region')['total_sales'].sum()
print("Total Sales : \n", total_sales)