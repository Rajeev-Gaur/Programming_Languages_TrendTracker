# src/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from src.preprocessing_data import load_data, preprocess_data

def train_model():
    print("Model training started...")
    df = load_data()  # Load the data
    df = preprocess_data(df)  # Preprocess the data

    X = df[['Year', 'MonthNum']]
    y = df['Python Worldwide(%)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    return df, y_test, y_pred  # Return the DataFrame and predictions


if __name__ == "__main__":
    train_model()
