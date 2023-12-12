import pandas as pd
# Let's define the path to the files based on the uploads
file_paths = ['backend/app/Red.csv', 'backend/app/Rose.csv', 'backend/app/Sparkling.csv', 'backend/app/White.csv']

# Initialize an empty list to store the DataFrames
dataframes = []

# Loop through the file paths and read them into pandas DataFrames
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Concatenate all the DataFrames into one
all_wines_df = pd.concat(dataframes, ignore_index=True)


all_wines_df.to_csv('/Users/veronicafarinazzo/Documents/GitHub/swdevel-lab-hfarm/backend/app/merged_df.csv', index=False)