import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path_1 = 'path/to/your/csvfile1.csv'  
file_path_2 = 'path/to/your/csvfile2.csv'  
file_path_3 = 'path/to/your/csvfile3.csv'  

data_1 = pd.read_csv('test.csv')
data_2 = pd.read_csv('gender_submission.csv')
data_3 = pd.read_csv('train.csv')

data = data_3

print(data.isnull().sum())

data['Age'].fillna(data['Age'].median(), inplace=True)

data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

data['Cabin'].fillna('Unknown', inplace=True)

print(data.isnull().sum())

data['Sex'] = data['Sex'].astype('category')
data['Embarked'] = data['Embarked'].astype('category')

sns.set(style="whitegrid")

plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', data=data)
plt.title('Survival Count')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', hue='Survived', data=data)
plt.title('Survival Count by Class')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', hue='Survived', data=data)
plt.title('Survival Count by Sex')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(data=data, x='Age', hue='Survived', multiple='stack', bins=30)
plt.title('Age Distribution by Survival')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(data['Fare'], bins=30, kde=True)
plt.title('Fare Distribution')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Pclass', y='Fare', data=data)
plt.title('Fare Distribution by Class')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x='Embarked', hue='Survived', data=data)
plt.title('Survival Count by Embarkation Port')
plt.show()

plt.figure(figsize=(10, 8))
sns.pairplot(data[['Survived', 'Pclass', 'Sex', 'Age', 'Fare', 'Embarked']], hue='Survived')
plt.title('Pairplot of Variables')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
