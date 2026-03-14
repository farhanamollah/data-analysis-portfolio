import pandas as pd

# Load dataset
data = pd.read_csv("example_data.csv")

# Show first rows
print("First five rows:")
print(data.head())

# Calculate summary statistics
print("\nSummary statistics:")
print(data.describe())
