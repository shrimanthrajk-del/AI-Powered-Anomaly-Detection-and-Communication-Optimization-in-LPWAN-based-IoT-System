import pandas as pd

# Load CICIoT CSV file
df = pd.read_csv(
    "C:/Users/shrim/OneDrive/Documents/CAPSTONE W4 6th sem 3rd year ece btech 2023-2027 batch pes university rr campus , banashankari 3rd stage bengaluru 560067. good/data/raw/BenignTraffic.csv"
)
print("Shape of dataset:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())
