import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GRU, Dense, Dropout

# Load sequences
X = np.load("X_sequences.npy")
y = np.load("y_targets.npy")

print("X shape:", X.shape)
print("y shape:", y.shape)

# Vocabulary size
vocab_size = int(np.max(y)) + 1
print("Vocabulary size:", vocab_size)

# Build improved model
model = Sequential()

model.add(
    Embedding(
        input_dim=vocab_size,
        output_dim=64,
        input_shape=(X.shape[1],)
    )
)

model.add(GRU(128))

model.add(Dropout(0.1))

model.add(Dense(128, activation='relu'))

model.add(Dense(vocab_size, activation="softmax"))

# Compile
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# Train model (ONLY ONCE)
history = model.fit(
    X,
    y,
    epochs=10,
    batch_size=128,
    validation_split=0.2
)

# Print results
for i in range(len(history.history['loss'])):
    print(f"Epoch {i+1}/10")
    print(
        f"loss: {history.history['loss'][i]:.4f} - "
        f"accuracy: {history.history['accuracy'][i]:.4f} - "
        f"val_loss: {history.history['val_loss'][i]:.4f} - "
        f"val_accuracy: {history.history['val_accuracy'][i]:.4f}"
    )

# -------- Graph 1: Loss --------
plt.figure()
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('GRU Model Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

# -------- Graph 2: Accuracy --------
plt.figure()
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('GRU Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()

# Save model
model.save("gru_model.h5")

print("Training finished ")
