# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df1 = pd.read_csv('Airplane_Crashes_and_Fatalities_Since_1908.csv',na_values=' ')
#
# df1['Date'] = pd.to_datetime(df1['Date'])
# df1['Date']=df1['Date'].dt.year
# ## Date Clean Section
# df1=df1.drop(labels=None,columns=['Time','Flight #'])
# df1=df1.dropna(subset=['Summary', 'Operator'])
#
# #df1=df1.dropna(how='all')
# #df1 = df1.dropna()
#
# print(df1[['Date','Summary']])
# print(df1.info())
# #number_of_craches = df1
# #df1['crashes_per_year'] =  df1.groupby(['Date','Operator'])
#
#
#
# ax = sns.countplot(x="Date", data=df1)
# plt.xticks(rotation=90)
# ax.axes.set_title("Plane Crashes Per Year",fontsize=20)
# ax.set_xlabel("Year",fontsize=15)
# ax.set_ylabel("Crashes",fontsize=15)
# ax.tick_params(labelsize=6)
# plt.show()
#
#
# cluster1 = df1.Summary.str.contains('fire' and 'fog' )
# print(list(cluster1).count(True))
#cluster2 = df1.Summary.str.contains('aircraft' and 'crashed' and 'plane'and 'shortly'and 'taking')
# cluster3 = df1.Summary.str.contains('fire' and 'fog' and 'cargo' and 'landing')
# cluster4 = df1.Summary.str.contains('fire' and 'fog' and '')
# cluster5 = df1.Summary.str.contains('fire' and 'fog' and '')
#
# cluster6 = df1.Summary.str.contains('fire' and 'fog' and '')
# cluster7 = df1.Summary.str.contains('fire' and 'fog' and '')
# print(list(cluster2).count(True))




#df1.plot(kind='hist')
#print(df1.info())


##print(df.describe())
##print(df.corr())
##df.corr().plot()
##plt.show()
##df.plot(subplots=True)

##plt.show()
#---------------------------------------------------------------------------------------------------------------#
import pandas as pd
import numpy as np
import seaborn as sns

# sns.set_color_codes("muted")  # to change color palette

import matplotlib.pyplot as plt

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)

df = pd.read_csv("Air.csv",na_values=' ')

# df1 = df[['Aboard','Fatalities']]
# print(df.describe())
# df.plot(kind='scatter',x='Aboard',y='Fatalities')

df['Survived'] = df['Aboard'] - df['Fatalities']
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.year

df = df.dropna(subset=['Summary', 'Date'])
df = df.drop(['Time', 'cn/In', 'Flight #', 'Registration'], axis=1)

df['Location'] = pd.Series([ var if var != 'NaN' else 'UnknownLocation'  for var in df['Location']  ])


"""Splitting location to Comma separated values   new is a dataframe"""
new = df['Location'].str.split(",", expand=True)
print(new)

"""Crashes Per Year"""

df['Date'].plot(kind='hist', bins=97, edgecolor='black', linewidth=0.8,color="skyblue")
plt.show()

#                                                               OLD WAY
# ax = sns.countplot(x="Date", data=df,color="blue")
# plt.xticks(rotation=90)
# ax.axes.set_title("Plane Crashes Per Year",fontsize=20)
# ax.set_xlabel("Year",fontsize=15)
# ax.set_ylabel("Crashes",fontsize=15)
# ax.tick_params(labelsize=6)
# plt.show()


df1 = df.groupby(['Date']).sum().reset_index()

"""Dead Per Year"""
# year = np.array(df['Date'])
# dead = np.array(df['Fatalities']).flatten()
# plt.bar(year, dead)
# plt.show()
bx = sns.barplot(x=df1['Date'], y=df1['Fatalities'], edgecolor='black', linewidth=0.8,color="skyblue", saturation=0.75)
bx.set(title="Dead per year")
bx.set_xlabel("Year", fontsize=15)
bx.set_ylabel("Dead", fontsize=15)
bx.tick_params(labelsize=6)
plt.xticks(rotation=70)
plt.show()
"""Survived Per Year"""
cx = sns.barplot(x=df1['Date'], y=df1['Survived'], edgecolor='black', linewidth=0.8,color="skyblue", saturation=0.75)
cx.set(title="Survived per year")
cx.set_xlabel("Year", fontsize=15)
cx.set_ylabel("Survived", fontsize=15)
cx.tick_params(labelsize=6)
plt.xticks(rotation=70)
plt.show()
"""Ground Per Year"""
cx = sns.barplot(x=df1['Date'], y=df1['Ground'], edgecolor='black', linewidth=0.8,color="skyblue", saturation=0.75)
cx.set(title="Ground per year")
cx.set_xlabel("Year", fontsize=15)
cx.set_ylabel("Survived", fontsize=15)
cx.tick_params(labelsize=6)
plt.xticks(rotation=70)
plt.show()

"""Aboard per year"""
# dx = sns.barplot(x=df1['Date'], y=df1['Aboard'], edgecolor='black', linewidth=0.8,color="skyblue", saturation=0.75)
# dx.set(title="Aboard per year")
# dx.set_xlabel("Year", fontsize=15)
# dx.set_ylabel("Aboard", fontsize=15)
# dx.tick_params(labelsize=6)
# plt.xticks(rotation=70)
# plt.show()

"""MY super plot"""
# Year = df1['Date']
# Aboard = df1['Aboard']
# Survived = df1['Survived']
# Fatalities = df1['Fatalities']
# legend = ['Aboard', 'Survived','Fatalities']
# plt.hist([Aboard, Survived,Fatalities], color=['orange', 'green','blue'])
# plt.xlabel("Year")
# plt.ylabel("No. of people")
# plt.legend(legend)
# plt.title('Aboard and Survived , Fatalities per year')
# plt.show()

# bx = sns.barplot(x=df1['Date'], y=df1['Aboard'],hue=['Ground','Survived'],color="b",saturation=0.75)
# bx.set(title="Aboard per year")
# bx.set_xlabel("Year",fontsize=15)
# bx.set_ylabel("",fontsize=15)
# bx.tick_params(labelsize=6)
# plt.xticks(rotation=70)

# df['Aboard'].plot(kind='bar')
# plt.show()
# """joint plot"""
# g = sns.jointplot("Fatalities", "Aboard", data=df, kind="reg")
# plt.show()
# """joint plot"""
# g = sns.jointplot("Survived", "Aboard", data=df, kind="reg")
# plt.show()
# """joint plot"""
# g = sns.jointplot("Ground", "Aboard", data=df, kind="reg")
# plt.show()
#
# """joint plot"""
# g = sns.jointplot("Fatalities", "Survived", data=df, kind="reg")
# plt.show()


"""Box plot"""
# sns.set(style="whitegrid")
# ax = sns.boxplot(x=df["Fatalities"])
# plt.show()
#
# """Box plot"""
# ax=df.plot(kind="box",stacked =True,y="Fatalities")
# """Box plot"""
# bx=df.plot(kind="box",stacked =True,y="Survived")
"""Box plot"""
cx=df.plot(kind="box",stacked =True,y="Ground")
"""Box plot"""
dx=df.plot(kind="box",stacked =True,y=["Aboard","Fatalities","Survived"])
plt.show()

# """Box plot"""
# ax = sns.boxplot(x=df["Ground"])
# plt.show()
# """Box plot"""
# sns.set(style="whitegrid")
# ax = sns.boxplot(x=df["Aboard"])
# plt.show()
# df1 = df.groupby(["Date","yr"])
# df.plot(kind="hist", x="Date", y="yr")


# ount = df.Summary.str.contains('fire' and 'plane' and '')
# print(list(count).count(True))
# plt.show()
# plt.plot(x,y2)