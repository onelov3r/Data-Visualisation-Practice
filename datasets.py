import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('vgsales.csv')
print(sales_data.head())

plt.bar(sales_data['Publisher'], sales_data['Global_Sales'])
print(sorted_by_year.head())

