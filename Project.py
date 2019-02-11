import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime

desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 100)

df = pd.read_csv("Air.csv", na_values=' ')

df['Survived'] = df['Aboard'] - df['Fatalities']

df['Date'] = pd.to_datetime(df['Date'])

print(df.head(10))

temp = df.dropna(subset=['Summary', 'Date'])

Date_frame = df.groupby(df.Date.dt.year)[['Date']].count()
Date_frame = Date_frame.rename(columns={"Date": "Count"})
Date_frame['Years'] = Date_frame.index
print(Date_frame.head())
print(plt.style.available)
plt.style.use('seaborn-muted')
Date_frame.plot(kind='bar', x='Years', y='Count', color='blue', width=1, figsize=(15, 10), rot=90, edgecolor='black')

Fatalities = df.groupby(df.Date.dt.year).sum()
print(Fatalities)
plt.xlabel("Count Crashes")
plt.ylabel("Year")
plt.title("Number of Crashes Per Year")
plt.show()
