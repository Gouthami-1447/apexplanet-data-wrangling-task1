import pandas as pd
df = pd.read_csv("customer_shopping_data.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
df['invoice_date'] = pd.to_datetime(df['invoice_date'], dayfirst=True)
print("\nAfter converting date:\n")
print(df.info())
df['total_amount'] = df['price'] * df['quantity']
print(df.head())
def age_group(age):
    if age < 25:
        return "Young"
    elif age < 50:
        return "Adult"
    else:
        return "Senior"

df['age_group'] = df['age'].apply(age_group)

print(df[['age', 'age_group']].head())
df['month'] = df['invoice_date'].dt.month

print(df[['invoice_date', 'month']].head())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nMissing values:\n", df.isnull().sum())