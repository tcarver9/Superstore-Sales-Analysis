import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\diirt\Downloads\superstore_sales.csv", encoding = 'latin1')
print(df.info())
print(df.describe())
df.drop_duplicates(inplace=True)
df = df.dropna()

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Order Month'] = df['Order Date'].dt.month_name()
df['Order Year'] = df['Order Date'].dt.year
df['Profit Margin (%)'] = np.round((df['Profit'] / df['Sales']) * 100, 2)

plt.figure(figsize=(8,6))
sns.barplot(x='Category', y='Sales', data=df, estimator=sum)
plt.title('Total Sales by Category', fontsize=14)
plt.show()

plt.figure(figsize=(8,6))
sns.barplot(x='Category', y='Profit', data=df, estimator=sum)
plt.title('Total Profit by Category', fontsize=14)
plt.show()

region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
region_profit.plot(kind='bar', color='teal', figsize=(8,5), title='Profit by Region')
plt.ylabel("Total Profit ($)")
plt.show()
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title('Discount Impact on Profit', fontsize=14)
plt.xticks(rotation=45)
plt.show()

month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

df['Order Month'] = pd.Categorical(df['Order Month'], categories=month_order, ordered=True)
monthly_sales = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().reset_index()
sns.lineplot(data=monthly_sales, x='Order Month', y='Sales', hue='Order Year')
plt.title('Monthly Sales Trends Over Time', fontsize=14)
plt.show()

top_products = (
    df.groupby('Product Name')[['Sales', 'Profit']]
      .sum()
      .sort_values(by='Profit', ascending=False)
      .head(10)
      .reset_index()
)

plt.figure(figsize=(10,6))
sns.barplot(
    data=top_products,
    x='Profit',
    y='Product Name'
)
plt.title('Top 10 Most Profitable Products')
plt.xlabel('Total Profit ($)')
plt.ylabel('Product')
plt.tight_layout()
plt.show()

segment_margin = (
    df.groupby('Segment')
      .agg(
          Total_Sales=('Sales', 'sum'),
          Total_Profit=('Profit', 'sum')
      )
      .reset_index()
)

segment_margin['Profit Margin (%)'] = (
    segment_margin['Total_Profit'] / segment_margin['Total_Sales']
) * 100

plt.figure(figsize=(8,5))
sns.barplot(
    data=segment_margin,
    x='Segment',
    y='Profit Margin (%)'
)
plt.title('Profit Margin by Customer Segment')
plt.ylabel('Profit Margin (%)')
plt.xlabel('Customer Segment')
plt.show()

