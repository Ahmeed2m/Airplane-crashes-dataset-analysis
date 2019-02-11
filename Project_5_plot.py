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


temp = df.dropna(subset=['Operator'])
# print(temp.info())
temp['military'] = temp.Operator.str.contains("Military")
temp['civil']= temp['military']==False
temp['Date'] = temp.Date.dt.year


temp = temp.loc[:,['Date','military','civil']]
# print(temp.info())
temp = temp.groupby('Date')[['military','civil']].aggregate(np.count_nonzero)
plt.figure(figsize=(15,5))
plt.style.use('bmh')
print("\n\n",temp,"\n\n",type(temp.index))
plt.plot(temp.index,'military',data=temp,color='blue',marker=".",linewidth=1)
plt.plot(temp.index,'civil', data=temp,color='green',marker=".",linewidth=1)
#plt.xticks(temp.index,rotation=45)

plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Count of Crashes Per")
plt.legend(fontsize=10)
plt.show()