import pandas as pd

# Absolute paths
INPUT_PATH = (
    "C:/Users/shrim/OneDrive/Documents/"
    "CAPSTONE W4 6th sem 3rd year ece btech 2023-2027 batch pes university rr campus , "
    "banashankari 3rd stage bengaluru 560067. good/data/processed/selected_features.csv"
)

OUTPUT_PATH = (
    "C:/Users/shrim/OneDrive/Documents/"
    "CAPSTONE W4 6th sem 3rd year ece btech 2023-2027 batch pes university rr campus , "
    "banashankari 3rd stage bengaluru 560067. good/data/processed/binned_features.csv"
)

# Load selected features
df = pd.read_csv(INPUT_PATH)

# -------------------------
# 1️⃣ Packet size binning
# -------------------------
def bin_packet_size(size):
    if size < 200:
        return 0
    elif size < 800:
        return 1
    else:
        return 2

# -------------------------
# 2️⃣ IAT binning
# -------------------------
def bin_iat(iat):
    if iat < 0.001:
        return 0
    elif iat < 0.05:
        return 1
    else:
        return 2

# -------------------------
# 3️⃣ Rate binning
# -------------------------
def bin_rate(rate):
    if rate < 10:
        return 0
    elif rate < 100:
        return 1
    else:
        return 2

# -------------------------
# 4️⃣ Duration binning
# -------------------------
def bin_duration(duration):
    if duration < 10:
        return 0
    elif duration < 100:
        return 1
    else:
        return 2


# Apply binning
df["pkt_size_bin"] = df["Tot size"].apply(bin_packet_size)
df["iat_bin"] = df["IAT"].apply(bin_iat)
df["rate_bin"] = df["Rate"].apply(bin_rate)
df["duration_bin"] = df["Duration"].apply(bin_duration)


# Final features used for symbol mapping
binned_df = df[
    [
        "Protocol Type",
        "LLC",
        "UDP",
        "pkt_size_bin",
        "iat_bin",
        "rate_bin",
        "duration_bin"
    ]
]


# Save output
binned_df.to_csv(OUTPUT_PATH, index=False)

print("Binned features preview:\n")
print(binned_df.head())
