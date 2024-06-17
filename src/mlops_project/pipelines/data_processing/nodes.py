import pandas as pd

def remove_duplicates(data: pd.DataFrame) -> pd.DataFrame:
    return data.drop_duplicates()

def remove_zero_bp(data: pd.DataFrame) -> pd.DataFrame:
    return data[data['resting bp s'] != 0]

def remove_zero_cholesterol(data: pd.DataFrame) -> pd.DataFrame:
    return data[data['cholesterol'] != 0]

def max_heart_rate_outliers(data: pd.DataFrame) -> pd.DataFrame:
    return data[(data['max heart rate'] >= 72) & (data['max heart rate'] <= 202)]

def bin_age(data: pd.DataFrame) -> pd.DataFrame:
    data['age'] = pd.cut(data['age'], bins=[0, 40, 50, 60, 70, 80, 90], labels=['0-40', '41-50', '51-60', '61-70', '71-80', '81-90'])
    return data

def bin_cholesterol(data: pd.DataFrame) -> pd.DataFrame:
    data['cholesterol'] = pd.cut(data['cholesterol'], bins=[0, 200, 240, 1000], labels=['normal', 'borderline high', 'high'])
    return data
