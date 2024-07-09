import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = 'population_by_age_group.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Display the first few rows of the data to understand its structure
print(data.head())

# Process the data to get the age distribution
age_groups = ['65+', '25-64 years', '15-24 years', '5-14 years', '0-4 years']
age_distribution = data[age_groups].sum()

# Create a bar chart for the age distribution
plt.figure(figsize=(10, 6))
plt.bar(age_groups, age_distribution, color='skyblue')
plt.xlabel('Age Groups')
plt.ylabel('Population')
plt.title('Age Distribution in the Population')
plt.xticks(rotation=45)
plt.show()
