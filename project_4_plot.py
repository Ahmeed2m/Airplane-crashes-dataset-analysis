
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





Data_frame2 = df.groupby(df.Date.dt.month)[['Date']].count()
Data_frame2 = Data_frame2.rename(columns={"Date": "month"})
print(Data_frame2)
Data_frame2=Data_frame2.reset_index(drop=True)
print(Data_frame2)
sns.barplot(Data_frame2.index,'month',data=Data_frame2,color='lightGreen')
plt.xticks(Data_frame2.index,['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec'])
plt.xlabel("Months of the Year")
plt.ylabel("Count")
plt.title("Count of Crashes by Month")
plt.show()