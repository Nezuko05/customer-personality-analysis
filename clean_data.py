import pandas as pd

# Step 1: Load the dataset using tab delimiter
df = pd.read_csv("marketing_campaign.csv", delimiter='\t')

# Step 2: Drop duplicates
df = df.drop_duplicates()

# Step 3: Handle missing values
# Drop rows where critical fields are missing
df = df.dropna(subset=['ID', 'Income'])

# Fill categorical nulls with most frequent value
df['Education'].fillna(df['Education'].mode()[0], inplace=True)
df['Marital_Status'].fillna(df['Marital_Status'].mode()[0], inplace=True)

# Step 4: Convert date column to datetime
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format="%d-%m-%Y", errors='coerce')

# Step 5: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 6: Save the cleaned dataset (optional)
df.to_csv("cleaned_marketing_campaign.csv", index=False)

# Step 7: Check result
print("Cleaned DataFrame shape:", df.shape)
print(df.head())
