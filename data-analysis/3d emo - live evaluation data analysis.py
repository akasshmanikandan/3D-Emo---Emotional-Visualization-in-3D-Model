import pandas as pd
import numpy as np

# 1. Load the Live Prototype Responses
input_path = "C:/Users/Akassh Manikandan/OneDrive/Desktop/Dissertation/Data Analysis/3D EMO – Live Interactive Prototype Evaluation  (Responses) - FINAL Responses.csv"
df = pd.read_csv(input_path)

# 2. Basic Cleaning
# Drop Timestamp 
if 'Timestamp' in df.columns:
    df.drop(columns=['Timestamp'], inplace=True)

# Standardize text entries
text_cols = df.select_dtypes(include='object').columns
for col in text_cols:
    df[col] = df[col].str.strip().str.capitalize()

# Replace common 'None' values with actual NaN
replace_none = ['None', 'Nil', '-', 'Na', 'N/a']
df.replace(replace_none, np.nan, inplace=True)

# Clean specific Yes/No questions
yes_no_cols = [
    'Do you have prior experience with 3d models or games?',
    'Were you able to trigger the emotions using the keyboard keys?',
    'Did the lighting changes help express the emotions better?'
]
for col in yes_no_cols:
    if col in df.columns:
        df[col] = df[col].str.strip().str.title()

# 3. Save Cleaned Data
output_path = "C:/Users/Akassh Manikandan/OneDrive/Desktop/Dissertation/Data Analysis/3D_EMO_Live_Evaluation_Cleaned.xlsx"
df.to_excel(output_path, index=False)

print(f"Cleaned evaluation data saved as: {output_path}")
