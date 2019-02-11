import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime

desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 100)

df = pd.read_csv("Air.csv",na_values=' ')


df['Survived'] = df['Aboard'] - df['Fatalities']


df['Date'] = pd.to_datetime(df['Date'])

print(df.head(10))

temp = df.dropna(subset=['Summary', 'Date'])


plt.style.use('seaborn-muted')

Data_frame1 = df.groupby(df.Date.dt.weekday)[['Date']].count()
Data_frame1 = Data_frame1.rename(columns={"Date": "day"})
print(Data_frame1)
sns.barplot(Data_frame1.index,'day',data=Data_frame1,color='lightGreen')
plt.xticks(Data_frame1.index,['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.xlabel("Days of The Week")
plt.ylabel("Count")
plt.title("Count of Crashes by Day")
plt.show()

