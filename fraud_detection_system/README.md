# Fraud Detection System

This project is a simple fraud detection application that predicts whether a bank transaction is likely to be fraudulent.

## Project Overview

The system uses a trained machine learning pipeline to classify a transaction based on features such as:

- transaction type
- amount
- sender balance before and after the transaction
- receiver balance before and after the transaction

The app is built with Python and Streamlit, making it easy to run locally in a browser.

## Project Structure

```text
fraud_detection_system/
├── main.py                     # Streamlit app entry point
├── fraud_detection_pipeline,pkl  # Trained ML pipeline
├── analysis_model.ipynb        # Notebook for model analysis/training exploration
├── data/
│   └── transactions.csv        # Transaction dataset used for analysis/modeling
└── README.md                   # Project documentation
```

## Features

- Select a transaction type from the dropdown
- Enter transaction values for sender and receiver balances
- Click Predict to get a fraud or non-fraud classification
- Shows the predicted result directly in the app

## Requirements

Install the required Python packages:

```bash
pip install streamlit pandas scikit-learn joblib
```

## Setup

1. Open a terminal in the project folder.
2. Make sure the trained model file `fraud_detection_pipeline,pkl` is present in the same folder as `main.py`.
3. Run the application.

## Run the App

```bash
streamlit run main.py
```

After the app starts, a browser tab will open and you can input transaction details to make a prediction.

## Model Behavior

The application loads the trained model pipeline from the pickle file and predicts on a single transaction record built from the user inputs.

- Prediction result `1` indicates likely fraud
- Prediction result `0` indicates likely legitimate transaction

## Data

The dataset in the `data/` folder contains transaction records used for analysis and model creation. It is intended for demonstration and educational purposes.

## Notes

- The model file name includes a comma: `fraud_detection_pipeline,pkl`.
- Keep this file in the same directory as `main.py` or the app will not load the model correctly.
- This project is a basic example of a fraud detection workflow and can be extended with more advanced features, such as:
  - preprocessing improvements
  - additional models
  - model evaluation metrics
  - deployment to cloud services

## License

This project is for learning and demonstration purposes.
