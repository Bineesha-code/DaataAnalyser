# Data Analysis on CSV File
# Author  : Bineesha K P
# Date    : 30-06-2025

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')
grouped = df.groupby('Product')['Sales'].sum()
grouped.plot(kind='bar')

plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Sales by Product')
plt.tight_layout()
plt.show()
