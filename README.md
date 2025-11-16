
# Data Cleaning & Processing Project

This is a beginner-friendly, GitHub-ready project demonstrating data cleaning and processing steps using Python (pandas, numpy, scikit-learn).

## Contents
- `notebooks/` - Jupyter notebooks with step-by-step EDA and cleaning workflows.
- `src/` - Reusable Python modules for data cleaning and processing.
- `data/raw/` - Raw (dirty) sample dataset.
- `data/cleaned/` - Cleaned dataset produced by the pipeline.
- `requirements.txt` - Python dependencies.
- `README.md` - This file.

## Project Overview
Steps included:
1. Data loading & inspection
2. Missing value handling (median/mean/mode/imputation)
3. Duplicates removal
4. Data type conversions (strings → numeric / datetime)
5. Text standardization (title-case, strip)
6. Outlier detection (IQR / Z-score) and winsorization
7. Feature engineering (tenure, age bins)
8. Encoding categorical features (one-hot / label)
9. Scaling (StandardScaler, MinMaxScaler)
10. Export cleaned dataset

## How to use
1. Clone this repo.
2. (Optional) Create and activate a virtual environment.
3. Install requirements: `pip install -r requirements.txt`
4. Run the notebook in `notebooks/` or run the pipeline script at `src/cleaning.py`.

## License
MIT
