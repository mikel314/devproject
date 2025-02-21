import pandas as pd
import matplotlib.pyplot as plt
import config as cf
from loguru import logger


df = pd.read_parquet(cf.path_data_processed + 'tracker_master_processed.parquet')

portfolio_type1 = df.groupby('Type1')['Value'].sum() / df['Value'].sum()
portfolio_type1 = portfolio_type1.reset_index()
portfolio_type1.columns = ['Type1', 'Value_pct']
portfolio_type1 = portfolio_type1[~portfolio_type1['Type1'].isin(['Curr', 'Index'])]

# Sort the dataframe by Value_pct
portfolio_type1 = portfolio_type1.sort_values(by='Value_pct', ascending=False)

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(portfolio_type1['Type1'], portfolio_type1['Value_pct'], color='skyblue')
plt.xlabel('Type1')
plt.ylabel('Value Percentage')
plt.title('Portfolio Distribution by Type1')
plt.xticks(rotation=45)
plt.savefig(cf.path_data_tmp + 'portfolio_distribution.png')