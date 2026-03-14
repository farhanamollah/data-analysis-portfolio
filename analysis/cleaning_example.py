import pandas as pd

data = pd.read_csv("example_data.csv")

# Remove missing values
cleaned = data.dropna()

# Rename columns (example)
cleaned = cleaned.rename(columns={"response": "response_value"})

print(cleaned.head())
