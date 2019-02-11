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
#
# print("Variance of Fatalities :", df["Fatalities"].var())
# print("Variance of Aboard :", df["Aboard"].var())
# print("Variance of Ground :", df["Ground"].var())
# print("Variance of Survived :", df["Survived"].var())

#
#
#plotting the sample
#
#


mean_of_sample=[0,1,2,3]

samplesize = 50
no_of_samples = 50
flag = False

sample_means =pd.DataFrame(columns=['Aboard','Fatalities','Ground','Survived'])

for samplesize in [100,500,1000]:

    for i in range(0, no_of_samples):
        sample = df.sample(samplesize)
        sample_means.loc[i] = [sample["Aboard"].mean(),sample["Fatalities"].mean(),sample["Ground"].mean(),sample["Survived"].mean()]
    ax = sample_means['Aboard'].plot(kind='kde', stacked=True, legend=True, label='Aboard of sample of '+str(samplesize))

ax.axvline(x=df["Aboard"].mean(),color='grey')
plt.show()

for samplesize in [100,500,1000]:

    for i in range(0, no_of_samples):
        sample = df.sample(samplesize)
        sample_means.loc[i] = [sample["Aboard"].mean(),sample["Fatalities"].mean(),sample["Ground"].mean(),sample["Survived"].mean()]
    bx = sample_means['Fatalities'].plot(kind='kde', stacked=True, legend=True, label='Fatalities of sample of '+str(samplesize))

bx.axvline(x=df["Fatalities"].mean(),color='grey')
plt.show()

for samplesize in [100,500,1000]:

    for i in range(0, no_of_samples):
        sample = df.sample(samplesize)
        sample_means.loc[i] = [sample["Aboard"].mean(),sample["Fatalities"].mean(),sample["Ground"].mean(),sample["Survived"].mean()]
    cx = sample_means['Ground'].plot(kind='kde', stacked=True, legend=True, label='Ground of sample of '+str(samplesize))

cx.axvline(x=df["Ground"].mean(),color='grey')
plt.show()

for samplesize in [100,500,1000]:

    for i in range(0, no_of_samples):
        sample = df.sample(samplesize)
        sample_means.loc[i] = [sample["Aboard"].mean(),sample["Fatalities"].mean(),sample["Ground"].mean(),sample["Survived"].mean()]
    dx = sample_means['Survived'].plot(kind='kde', stacked=True, legend=True, label='Survived of sample of '+str(samplesize))
    print(sample_means['Survived'].var())

dx.axvline(x=df["Survived"].mean(),color='grey')
plt.show()


# sample = df.sample(100)
# sample['Fatalities'].plot(kind='kde',stacked=True,legend = True,label='Fatalities of sample of 100 ')
# print("Mean of means Fatalities of five Samples of ",samplesize,":", mean_of_sample[0])
# print("Mean of means Aboard of five Samples of ",samplesize,":", mean_of_sample[1])
# print("Mean of means Ground of five Samples of ",samplesize,":", mean_of_sample[2])
# print("Mean of means Survived of five Samples of ",samplesize,":", mean_of_sample[3])
