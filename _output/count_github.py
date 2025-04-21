import pandas as pd
import os

files = ["stackoverflow/question_tags.csv", "stackoverflow/questions.csv"]
count = 0

for file in files:
    try:
        df = pd.read_csv(file, dtype=str, on_bad_lines='skip')
      
        count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False).any(), axis=1).sum()
    except FileNotFoundError:
        print(f"Warning: {file} not found.")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Total lines containing 'GitHub': {count}")


with open("_output/github_count.txt", "w") as f:
    f.write(f"Total lines containing 'GitHub': {count}\n")
