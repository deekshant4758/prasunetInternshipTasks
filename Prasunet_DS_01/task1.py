import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('population_data.csv')

# Preview the dataset
print(data.head())

# Assuming we want to visualize the population distribution for a specific year, e.g., 2020
year = '2022'
population_data = data[['Country Name', 'Country Code', year]]

# Drop any rows with missing data for the selected year
population_data = population_data.dropna()

# Convert the population data to integers
population_data[year] = population_data[year].astype(int)

# Select a subset of countries for better visualization
# Let's select the top 20 most populous countries for the year 2020
top_countries = population_data.nlargest(40, year)

# Sort by population for a better visual effect
top_countries = top_countries.sort_values(by=year, ascending=True)

# Plotting
plt.figure(figsize=(14, 10))
plt.barh(top_countries['Country Name'], top_countries[year], color='skyblue')
plt.xlabel('Population')
plt.title(f'Top 20 Most Populous Countries in {year}')
plt.tight_layout()

# Show plot
plt.show()
