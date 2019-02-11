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

temp = df.dropna(subset=['Summary', 'Date'])

df1 = df[['Aboard','Fatalities']]
print(df.describe())
plt.figure(figsize=(15,5))
plt.scatter(df.Aboard,df.Survived,alpha=0.7,s = 50)
plt.ylabel('Aboard')
plt.xlabel('Survived')
plt._show()

plt.scatter(df.Aboard,df.Fatalities,alpha=0.7,s = 50)
plt.ylabel('Aboard')
plt.xlabel('Fatalities')
plt._show()


plt.scatter(df.Fatalities,df.Survived,alpha=0.7,s = 50)

plt.ylabel('Survived')
plt.xlabel('Fatalities')
plt._show()

