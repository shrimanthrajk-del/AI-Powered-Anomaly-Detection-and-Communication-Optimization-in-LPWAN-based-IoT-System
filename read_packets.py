import pandas as pd

# Load CSV file (each row ≈ one packet)
csv_path = ("C:/Users/shrim/OneDrive/Documents/CAPSTONE W4 6th sem 3rd year ece btech 2023-2027 batch pes university rr campus , banashankari 3rd stage bengaluru 560067. good/data/raw/BenignTraffic.csv"
)
df = pd.read_csv(csv_path)

print("Total packets (rows):", len(df))
print("\nColumns available:")
print(df.columns)

print("\nFirst packet (row):")
print(df.iloc[0])
