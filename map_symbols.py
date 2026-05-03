import pandas as pd

# Absolute paths
INPUT_PATH = (
    "C:/Users/shrim/OneDrive/Documents/"
    "CAPSTONE W4 6th sem 3rd year ece btech 2023-2027 batch pes university rr campus , "
    "banashankari 3rd stage bengaluru 560067. good/data/processed/binned_features.csv"
)

OUTPUT_PATH = (
    "C:/Users/shrim/OneDrive/Documents/"
    "CAPSTONE W4 6th sem 3rd year ece btech 2023-2027 batch pes university rr campus , "
    "banashankari 3rd stage bengaluru 560067. good/data/processed/symbol_sequence.csv"
)

# Load binned features
df = pd.read_csv(INPUT_PATH)

symbol_map = {}       # maps feature tuple -> symbol id
symbol_sequence = []
symbol_id = 0

# Convert each row into a symbol
for _, row in df.iterrows():

    # tuple representing packet behaviour
    key = tuple(row.values)   
    # (Protocol Type, LLC, UDP, pkt_size_bin, iat_bin, rate_bin, duration_bin)

    if key not in symbol_map:
        symbol_map[key] = symbol_id
        symbol_id += 1

    symbol_sequence.append(symbol_map[key])


# Save symbol sequence
pd.DataFrame({"symbol": symbol_sequence}).to_csv(OUTPUT_PATH, index=False)


print("Total unique symbols:", len(symbol_map))
print("First 10 symbols:", symbol_sequence[:10])
