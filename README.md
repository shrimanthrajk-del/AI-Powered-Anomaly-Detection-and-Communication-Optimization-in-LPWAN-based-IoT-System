## Overview
This project implements a lightweight anomaly detection system for LPWAN-based IoT networks using a GRU (Gated Recurrent Unit) model. It processes network traffic data, converts it into symbolic sequences, and detects anomalies by learning and predicting communication patterns.

⚠️ This project is currently a work in progress.

## Features
* Symbolic representation of network traffic data
* Sequence generation using sliding window approach
* GRU-based deep learning model for sequence prediction
* Anomaly detection using prediction deviation
* Lightweight and efficient design for LPWAN environments
* Model training with validation and performance tracking
* Scalable approach for real-time anomaly detection

## Methodology
### Data Processing
* Raw IoT network traffic data is preprocessed
* Features are binned into categories
* Each packet is converted into a unique symbol

### Sequence Generation
* Sliding window technique used
* Fixed sequence length (e.g., 5)
* Generates input-output pairs for training

### Model Architecture
* Embedding Layer → converts symbols to vectors
* GRU Layer → learns temporal patterns
* Dropout Layer → prevents overfitting
* Dense Layer → predicts next symbol

### Anomaly Detection Logic
* Model predicts next symbol in sequence
* Compare predicted vs actual symbol
* Significant deviation → anomaly detected

### System Flow
* Input IoT traffic data
* Preprocess and convert to symbols
* Generate sequences
* Train GRU model
* Predict next symbol
* Compare prediction with actual
* Detect anomalies

## Project Structure
LPWAN-GRU/
│
├── dataset/                # Input dataset (external link if large)
├── preprocessing.py        # Data cleaning & symbol generation
├── sequence.py             # Sequence creation logic
├── model.py                # GRU model architecture
├── train.py                # Training pipeline
├── results/                # Output graphs / logs
├── README.md               # Project documentation

## Results
The model effectively learns communication patterns, demonstrates stable training and validation performance, handles a large output space of 4605 symbols, and remains suitable for anomaly detection despite a moderate accuracy of around 28%, with further improvements planned as part of ongoing development.

## Dataset
Due to size constraints, the dataset is hosted externally:
https://drive.google.com/drive/folders/1aGqEdRtFPELTTzuBT_bvc5JWgqH8KLjq?usp=drive_link

## Conclusion
This project demonstrates an efficient approach for anomaly detection in LPWAN IoT systems using GRU-based sequence modeling, while ongoing improvements are being made as part of its development
