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
temp = df.dropna(subset=['Fatalities', 'Aboard', 'Ground', 'Survived'])

print("Mean of Fatalities :", df["Fatalities"].mean())
print("Mean of Aboard :", df["Aboard"].mean())
print("Mean of Ground :", df["Ground"].mean())
print("Mean of Survived :", df["Survived"].mean())

print("Variance of Fatalities :", df["Fatalities"].var())
print("Variance of Aboard :", df["Aboard"].var())
print("Variance of Ground :", df["Ground"].var())
print("Variance of Survived :", df["Survived"].var())

mean1=0.0
df.dropna(subset=['Aboard'])
for i in range(0, len(df)):
    if df.iloc[i]['Aboard']>0:
        mean1 = mean1 + df.iloc[i]['Aboard']
    # print(mean1)
mean=mean1 /df['Aboard'].count()
# print("Mean of Aboard :",mean)


#
# plotting the sample
#

# plt.style.use('bmh')
dfmean=df.mean()
dfmean = dfmean.to_frame()
print(dfmean)

df.mean().plot(kind="bar",color="skyblue",rot =0,title="Original Means of each Feature")
plt.show()

mean_of_sample=[0,1,2,3]

samplesize = 50
no_of_samples = 50
# print("\n")
flag = False

sample_means =pd.DataFrame(columns=['Aboard','Fatalities','Ground','Survived'])

for i in range(0, no_of_samples):
    sample = df.sample(samplesize)
    sample_means.loc[i] = [sample["Aboard"].mean(),sample["Fatalities"].mean(),sample["Ground"].mean(),sample["Survived"].mean()]
    # print("Mean of Aboard of No.",i,"Sample of ",samplesize,":", sample["Aboard"].mean())
    # print("Mean of Fatalities of No.",i,"Sample of",samplesize,":", sample["Fatalities"].mean())
    # print("Mean of Ground of No.",i,"Sample of ",samplesize,":", sample["Ground"].mean())
    # print("Mean of Survived of No.",i,"Sample of ",samplesize,":", sample["Survived"].mean())
    if flag:
        mean_of_sample[0] += sample["Fatalities"].mean()
        mean_of_sample[1] += sample["Aboard"].mean()
        mean_of_sample[2] += sample["Ground"].mean()
        mean_of_sample[3] += sample["Survived"].mean()
    else:  # if this is the first iteration
        flag = True
        mean_of_sample[0] = sample["Fatalities"].mean()
        mean_of_sample[1] = sample["Aboard"].mean()
        mean_of_sample[2] = sample["Ground"].mean()
        mean_of_sample[3] = sample["Survived"].mean()

mean_of_sample[0] /= no_of_samples
mean_of_sample[1] /= no_of_samples
mean_of_sample[2] /= no_of_samples
mean_of_sample[3] /= no_of_samples


print(sample_means['Survived'].var())


ax = sample_means['Fatalities'].plot(kind='bar',color="skyblue",alpha=0.8,width=1,edgecolor="black",rot=0,title="Means of samples of Fatalities",x="Sample No.",y="Means")
ax.axhline(y=df["Fatalities"].mean(), xmin=-1, xmax=1, color='black', linestyle='-', lw=2)
ax.text(1.02, df["Fatalities"].mean(), "Dataset Mean", va='center', ha="left", bbox=dict(facecolor="w",alpha=0.5),
        transform=ax.get_yaxis_transform())
plt.show()

ax = sample_means['Aboard'].plot(kind='bar',color="skyblue",alpha=0.8,width=1,edgecolor="black",rot=0,title="Means of samples of Aboard",x="Sample No.",y="Means")
ax.axhline(y=df["Aboard"].mean(), xmin=-1, xmax=1, color='black', linestyle='-', lw=2)
ax.text(1.02, df["Aboard"].mean(), "Dataset Mean", va='center', ha="left", bbox=dict(facecolor="w",alpha=0.5),
        transform=ax.get_yaxis_transform())
plt.show()

ax = sample_means['Ground'].plot(kind='bar',color="skyblue",alpha=0.8,width=1,edgecolor="black",rot=0,title="Means of samples of Ground",x="Sample No.",y="Means")
ax.axhline(y=df["Ground"].mean(), xmin=-1, xmax=1, color='black', linestyle='-', lw=2)
ax.text(1.02, df["Ground"].mean(), "Dataset Mean", va='center', ha="left", bbox=dict(facecolor="w",alpha=0.5),
        transform=ax.get_yaxis_transform())
plt.show()

ax = sample_means['Survived'].plot(kind='bar',color="skyblue",alpha=0.8,width=1,edgecolor="black",rot=0,title="Means of samples of Survived",x="Sample No.",y="Means")
ax.axhline(y=df["Survived"].mean(), xmin=-1, xmax=1, color='black', linestyle='-', lw=2)
ax.text(1.02, df["Survived"].mean(), "Dataset Mean", va='center', ha="left", bbox=dict(facecolor="w",alpha=0.5),
        transform=ax.get_yaxis_transform())
plt.show()

# sample = df.sample(100)
# sample['Fatalities'].plot(kind='kde',stacked=True,legend = True,label='Fatalities of sample of 100 ')
plt.show()

# print("Mean of means Fatalities of five Samples of ",samplesize,":", mean_of_sample[0])
# print("Mean of means Aboard of five Samples of ",samplesize,":", mean_of_sample[1])
# print("Mean of means Ground of five Samples of ",samplesize,":", mean_of_sample[2])
# print("Mean of means Survived of five Samples of ",samplesize,":", mean_of_sample[3])
