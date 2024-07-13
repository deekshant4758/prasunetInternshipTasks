import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'acc_16.csv'
df = pd.read_csv(file_path)

print(df.head())

print(df.info())

plt.figure(figsize=(12, 6))
sns.histplot(df['HOUR'], bins=24, kde=False, color='blue')
plt.title('Distribution of Accidents by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='WEATHER', palette='viridis')
plt.title('Distribution of Accidents by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='LGT_COND', palette='viridis')
plt.title('Distribution of Accidents by Road Condition')
plt.xlabel('Road Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='DAY_WEEK', palette='viridis')
plt.title('Distribution of Accidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='MONTH', palette='viridis')
plt.title('Distribution of Accidents by Month')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

region_urban = df.groupby(['REGION', 'URBANICITY']).size().unstack().fillna(0)
print(region_urban)

plt.figure(figsize=(14, 8))
sns.heatmap(region_urban, annot=True, fmt='d', cmap='viridis')
plt.title('Accident Hotspots by Region and Urbanicity')
plt.xlabel('Urbanicity')
plt.ylabel('Region')
plt.show()
