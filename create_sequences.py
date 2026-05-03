import pandas as pd
import numpy as np

INPUT_PATH = "data/processed/symbol_sequence.csv"

# Load symbol sequence
df = pd.read_csv(INPUT_PATH)

symbols = df["symbol"].values

WINDOW_SIZE = 10

X = []
y = []

for i in range(len(symbols) - WINDOW_SIZE):

    sequence = symbols[i:i+WINDOW_SIZE]
    target = symbols[i+WINDOW_SIZE]

    X.append(sequence)
    y.append(target)

X = np.array(X)
y = np.array(y)

print("Input shape:", X.shape)
print("Target shape:", y.shape)

np.save("X_sequences.npy", X)
np.save("y_targets.npy", y)

print("Sequences saved successfully")
