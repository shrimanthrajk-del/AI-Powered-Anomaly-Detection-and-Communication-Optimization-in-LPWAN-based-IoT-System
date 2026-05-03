import pandas as pd

CSV_PATH = (
    "C:/Users/shrim/OneDrive/Documents/"
    "CAPSTONE W4 6th sem 3rd year ece btech 2023-2027 batch pes university rr campus , "
    "banashankari 3rd stage bengaluru 560067. good/data/raw/BenignTraffic.csv"
)

df = pd.read_csv(CSV_PATH)

# Select DÏoT-relevant features from your dataset
selected_df = df[
    [   
        "Protocol Type",
        "Duration",
        "Rate",
        "Srate",
        "LLC",               
        "UDP",               
        "Tot size",          
        "IAT",
        "Number",
        "Variance",
        "Weight"               
        
    ]
]

print("Selected features preview:\n")
print(selected_df.head())

# Save selected features
selected_df.to_csv(
    "C:/Users/shrim/OneDrive/Documents/"
    "CAPSTONE W4 6th sem 3rd year ece btech 2023-2027 batch pes university rr campus , "
    "banashankari 3rd stage bengaluru 560067. good/data/processed/selected_features.csv",
    index=False
)



