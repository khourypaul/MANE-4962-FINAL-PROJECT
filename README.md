# MANE-4962-FINAL-PROJECT

# EMG Signal Classification for Prosthetic Control

## Author
Paul Khoury

## Description
This project develops machine learning models to interpret surface electromyographic (sEMG) signals for classifying hand gestures, with applications in smart prosthetic control. The objective is to create an accurate classifier that predicts user intent from raw electrode sensor data.

## Dataset
UC Irvine Machine Learning Repository. Linked in data folder.

## Models/Methods Overview
- **Feature Extraction**: Root Mean Square, Mean Absolute Value, and Slope Sign Changes
- **Preprocessing**: Data aggregation, data filtering, StandardScaler
- **Models**: Support Vector Machine  and then Neural Network

## Results
- Neural Network achieved 94% classification accuracy
- SVM with MAV features reached 92.8% accuracy
- MAV features outperformed RMS features
