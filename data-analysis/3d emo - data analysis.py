import pandas as pd
import numpy as np
import os

# 1. Load and Clean Dataset 
df = pd.read_csv(r"C:\Users\Akassh Manikandan\OneDrive\Desktop\Dissertation\Data Analysis\3D-EMO User Evaluation (Responses) - Form Responses FINAL.csv")

# Drop Timestamp 
if 'Timestamp' in df.columns:
    df.drop(columns=['Timestamp'], inplace=True)


def clean_text(text):
    if isinstance(text, str) and text.strip().lower() in ['na', 'nil', '-', 'none', 'n/a']:
        return np.nan
    return text

df = df.applymap(clean_text)

# 2. Prepare for Expanded Accuracy Analysis
column_mapping = {
    "Q1": "Q1: What emotion do you think the character is expressing in this image? ",
    "Q2": "Q2: What emotion do you think the character is expressing in this image? ",
    "Q3": "Q3: What emotion do you think the character is expressing in this image? ",
    "Q4": "Q4: What emotion do you think the character is expressing in this image? ",
    "Q5": "Q5: What emotion do you think the character is expressing in this image? ",
    "Q6": "Q6: What emotion do you think the character is expressing in this image? ",
    "Q7": "Q7: What emotion do you think the character is expressing in this image? ",
    "Q8": "Q8: What emotion do you think the character is expressing in this image? ",
    "Q9": "Q9: What emotion do you think the character is expressing in this image? ",
    "Q10": "Q10: What emotion do you think the character is expressing in this image? "
}

# Emotion labels for the questions
emotion_labels = {
    "Q1": "Smile",
    "Q2": "Sad",
    "Q3": "Fear",
    "Q4": "Surprise",
    "Q5": "Disgust",
    "Q6": "Angry",
    "Q7": "Fake Smile",
    "Q8": "Tired",
    "Q9": "Mesmerized",
    "Q10": "Annoyed"
}

# Accepted responses per question
accepted_answers = {
    "Q1": ["smile", "happy"],
    "Q2": ["sad", "disappointed"],
    "Q3": ["fear", "shock"],
    "Q4": ["surprise", "amazed"],
    "Q5": ["disgust", "uncomfortable"],
    "Q6": ["angry", "rage"],
    "Q7": ["fake smile", "evil smile"],
    "Q8": ["sad", "tired"],
    "Q9": ["mesmerized", "amazed"],
    "Q10": ["annoyed", "tense"]
}

# Calculate Expanded Accuracy
accuracy_results = {}
for q, valid_answers in accepted_answers.items():
    col = column_mapping[q]
    df[col] = df[col].astype(str).str.strip().str.lower()
    total_responses = df[col].notna().sum()
    correct_count = df[col].isin(valid_answers).sum()
    accuracy = (correct_count / total_responses) * 100 if total_responses else 0
    accuracy_results[q] = {
        "Emotion": emotion_labels[q],
        "Correct Responses": correct_count,
        "Total Responses": total_responses,
        "Expanded Accuracy (%)": round(accuracy, 2)
    }

# Create accuracy DataFrame
accuracy_df = pd.DataFrame.from_dict(accuracy_results, orient='index')
accuracy_df = accuracy_df[["Emotion", "Correct Responses", "Total Responses", "Expanded Accuracy (%)"]]


# 3. Save both sheets into one Excel workbook
output_path = r"C:\Users\Akassh Manikandan\OneDrive\Desktop\Dissertation\Data Analysis\3d_EMO_User_Analysis.xlsx"
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Cleaned Data', index=False)
    accuracy_df.to_excel(writer, sheet_name='Expanded Accuracy', index=False)

print(f"Excel file created at: {output_path}")
