# Superstore-Sales-Analysis
In this project, I analyzed retail transaction data to understand what drives sales, profit, and profit margin across products, regions, and customer segments.

The main workflow I followed includes:

Loading and cleaning data using pandas
Creating new features such as month, year, and profit margin
Performing exploratory data analysis and visualization
Explaining key business findings and recommendations
All of the work was done in Python using pandas, numpy, seaborn, and matplotlib.

Business Questions Answered:

Which product categories generate the most revenue and which are actually the most profitable?
Which regions perform best and which ones underperform?
How do discounts affect total profit and margin?
What are the top 10 most profitable products?
Which customer segment has the highest profit margin?
Are there any seasonal trends that affect sales?

Dataset:
The dataset is a Superstore-style retail dataset with historical order-level information: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download

Key columns include:

Order Date, Ship Date
Region, State, Segment (Consumer, Corporate, Home Office)
Category, Sub-Category, Product Name
Sales, Quantity, Discount, Profit
Order Month (added)
Order Year (added)
Profit Margin (%) = Profit / Sales * 100 (added)
