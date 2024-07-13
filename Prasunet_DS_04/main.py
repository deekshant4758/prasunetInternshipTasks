import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'twitter_training.csv'
df = pd.read_csv(file_path)

print(df.head())

# Basic data information
print(df.info())

sentiment_counts = df['sentiment'].value_counts()
print(sentiment_counts)

# Plot the sentiment distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='sentiment', palette='viridis')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.show()

# Count the number of tweets per topic
topic_counts = df['topic'].value_counts()
print(topic_counts)

plt.figure(figsize=(14, 8))
sns.countplot(data=df, y='topic', palette='viridis', order=topic_counts.index)
plt.title('Topic Distribution')
plt.xlabel('Number of Tweets')
plt.ylabel('Topic')
plt.show()

topic_sentiment = df.groupby(['topic', 'sentiment']).size().unstack().fillna(0)
print(topic_sentiment)

topic_sentiment.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='viridis')
plt.title('Sentiment Distribution by Topic')
plt.xlabel('Topic')
plt.ylabel('Number of Tweets')
plt.legend(title='Sentiment')
plt.show()
