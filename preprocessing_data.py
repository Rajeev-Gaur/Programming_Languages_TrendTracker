import pandas as pd
from src.config import DATA_FILE_PATH

# src/preprocessing_data.py

import pandas as pd
from src.config import DATA_FILE_PATH

def load_data():
    return pd.read_csv(DATA_FILE_PATH)

def preprocess_data(df):
    df = df.dropna()
    df['Month'] = pd.to_datetime(df['Month'])
    df['Year'] = df['Month'].dt.year
    df['MonthNum'] = df['Month'].dt.month
    return df

