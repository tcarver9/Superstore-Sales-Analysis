# Superstore-Sales-Analysis
In this project, I analyzed retail transaction data to understand what drives sales, profit, and profit margin across products, regions, and customer segments.

1) Results:
- The West region is the strongest profit center, while the South underperforms and likely needs pricing or cost attention.
- Certain products generate very high profit and should be protected/prioritized in inventory and marketing.
- High discounting is linked to negative profit in several categories, which means promotions are sometimes destroying margin instead of driving smart growth.
- Sales peak late in the year, which supports seasonal planning and inventory ramp-up toward Q4.
- Different customer segments do not deliver the same margin per dollar sold, which matters for targeting.


-The main workflow I followed includes:

Loading and cleaning data using pandas
Creating new features such as month, year, and profit margin
Performing exploratory data analysis and visualization
Explaining key business findings and recommendations
All of the work was done in Python using pandas, numpy, seaborn, and matplotlib.

-Business Questions Answered:

Which product categories generate the most revenue and which are actually the most profitable?
Which regions perform best and which ones underperform?
How do discounts affect total profit and margin?
What are the top 10 most profitable products?
Which customer segment has the highest profit margin?
Are there any seasonal trends that affect sales?

-Dataset:
The dataset is a Superstore-style retail dataset with historical order-level information: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download

-Key columns include:

Order Date, Ship Date
Region, State, Segment (Consumer, Corporate, Home Office)
Category, Sub-Category, Product Name
Sales, Quantity, Discount, Profit
Order Month (added)
Order Year (added)
Profit Margin (%) = Profit / Sales * 100 (added)

-Tech Stack:

Python: pandas, numpy
Visualization: matplotlib, seaborn
Next step: building a Power BI dashboard 

Steps I Performed:

1) Load data
df = pd.read_csv(r"C:\Users\diirt\Downloads\superstore_sales.csv", encoding='latin1')
print(df.info())
print(df.describe())

2) Clean the data:
Removed duplicates and missing values
Converted date columns into proper datetime format
Verified that numeric fields were in the right data type

3) Feature engineering
df['Order Month'] = df['Order Date'].dt.month_name()
df['Order Year'] = df['Order Date'].dt.year
df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100

4) Analysis:
Sales vs Profit by Category: helped me identify which categories sell the most vs which are actually profitable.
Profit by Region: showed which regions drive performance.
Discount vs Profit: revealed that heavy discounting often leads to negative profit.
Monthly Sales Trend: displayed seasonal peaks around holidays.
Top 10 Most Profitable Products: helped pinpoint which SKUs generate the most value.
Profit Margin by Customer Segment: compared how different customer types perform.

5) Business Recommendations:
- Limit discounts above 20 percent on low-margin categories, since margin drops sharply once discounts get too aggressive.
- Shift marketing and inventory priority toward top 10 most profitable SKUs instead of just top sellers, to protect contribution margin.
- Investigate why the South region underperforms in profit. Possible causes include shipping cost, discounting, or product mix.
- Treat higher-margin customer segments as priority for account-based outreach and retention efforts.
- Plan inventory and promotions aggressively around Q4 seasonal spikes, since sales consistently increase at year-end.


