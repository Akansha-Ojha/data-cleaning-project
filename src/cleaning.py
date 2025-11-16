
"""Data cleaning pipeline module.

Run as script: python src/cleaning.py
"""
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(path):
    return pd.read_csv(path)

def basic_cleaning(df):
    # Convert salary to numeric
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    # Standardize text
    df['City'] = df['City'].astype(str).str.strip().str.title().replace({'None':'Unknown'})
    df['Department'] = df['Department'].astype(str).str.strip().str.title()
    # Parse dates
    df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')
    return df

def impute_values(df):
    df['Age'] = SimpleImputer(strategy='median').fit_transform(df[['Age']])
    df['Salary'] = SimpleImputer(strategy='mean').fit_transform(df[['Salary']])
    df['City'] = df['City'].fillna('Unknown')
    df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
    return df

def feature_engineer(df, today=pd.to_datetime('2025-11-15')):
    df['Tenure_days'] = (today - df['JoinDate']).dt.days
    df['Tenure_years'] = (df['Tenure_days'] / 365).round(2)
    df['Age_group'] = pd.cut(df['Age'], bins=[0,25,35,45,60,200], labels=['<25','25-35','35-45','45-60','60+'], include_lowest=True)
    return df

def encode_and_scale(df):
    # One-hot city
    df = pd.get_dummies(df, columns=['City'], drop_first=True)
    # Label encode Department and Attrition
    le = LabelEncoder()
    df['Department_le'] = le.fit_transform(df['Department'])
    if 'Attrition' in df.columns:
        df['Attrition_le'] = le.fit_transform(df['Attrition'])
    # Scale numeric
    scaler = StandardScaler()
    num_cols = ['Age','Salary','Tenure_years']
    for c in num_cols:
        if c not in df.columns:
            df[c] = np.nan
    df[[c + '_scaled' for c in num_cols]] = scaler.fit_transform(df[num_cols])
    return df

def save_clean(df, path):
    df.to_csv(path, index=False)

def run_pipeline(raw_path='data/raw/raw_hr_dataset.csv', cleaned_path='data/cleaned/cleaned_hr_dataset.csv'):
    df = load_data(raw_path)
    df = basic_cleaning(df)
    df = impute_values(df)
    df = feature_engineer(df)
    df = encode_and_scale(df)
    save_clean(df, cleaned_path)
    print('Cleaning complete. Clean file saved to', cleaned_path)

if __name__ == '__main__':
    run_pipeline()
