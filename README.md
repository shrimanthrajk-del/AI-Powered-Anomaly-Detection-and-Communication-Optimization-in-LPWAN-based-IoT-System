## Overview
This project implements a lightweight anomaly detection system for LPWAN-based IoT networks using a GRU (Gated Recurrent Unit) model. It processes network traffic data, converts it into symbolic sequences, and detects anomalies by learning and predicting communication patterns.

⚠️ This project is currently a work in progress and is intended for learning, experimentation, and demonstration purposes.

## Features
Symbolic representation of network traffic data

Sequence generation using sliding window approach

GRU-based deep learning model for sequence prediction

Anomaly detection using prediction deviation

Lightweight and efficient design for LPWAN environments

Model training with validation and performance tracking

Scalable approach for real-time anomaly detection

## Methodology
Data Processing
Raw IoT network traffic data is preprocessed

Features are binned into categories

Each packet is converted into a unique symbol

## Sequence Generation
Sliding window technique used

Fixed sequence length (e.g., 5)

Generates input-output pairs for training

## Model Architecture
Embedding Layer → converts symbols to vectors

GRU Layer → learns temporal patterns

Dropout Layer → prevents overfitting

Dense Layer → predicts next symbol

## Anomaly Detection Logic
Model predicts next symbol in sequence

Compare predicted vs actual symbol

Significant deviation → anomaly detected

## System Flow
Input IoT traffic data

Preprocess and convert to symbols

Generate sequences

Train GRU model

Predict next symbol

Compare prediction with actual

Detect anomalies

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
Model learns communication patterns effectively

Stable training and validation performance

Handles large output space (4605 symbols)

Suitable for anomaly detection despite moderate accuracy (~28%)

## Key Concepts
Sequence Learning using GRU

Symbolic representation of network behavior

Temporal pattern recognition

Lightweight AI for LPWAN

## Limitations
Accuracy affected by large number of classes

Limited sequence length may reduce context

Depends on quality of input data

## Future Work
Improve accuracy using longer sequences

Optimize model for real-time deployment

Explore hybrid or attention-based models

Integrate with live IoT systems

## Dataset
Due to size constraints, the dataset is hosted externally:
https://drive.google.com/drive/folders/1aGqEdRtFPELTTzuBT_bvc5JWgqH8KLjq?usp=drive_link

## Conclusion
This project demonstrates an efficient approach for anomaly detection in LPWAN IoT systems using GRU-based sequence modeling, while ongoing improvements are being made as part of its development
