import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
import numpy as np

file_path = '/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/final-data-with-conditions-edited.csv'
df = pd.read_csv(file_path, sep=';')

for col in df.columns:
    if df[col].dtype == object and df[col].str.contains(',', regex=False).any():
        df[col] = df[col].str.replace(',', '.').astype(float)

df['Wind Direction'] = df['Wind Direction'].fillna('none')
df['Tide'] = df['Tide'].fillna('slack')

features = ['Watts', 'Effective Length', 'Rate', 'Wind Speed (mph)', 'Wind Direction', 'Tide']
target = 'Speed'

categorical = ['Wind Direction', 'Tide']
numerical = ['Watts', 'Effective Length', 'Rate', 'Wind Speed (mph)']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numerical),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical)
    ]
)

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', XGBRegressor(n_estimators=100, random_state=42))
])

X = df[features]
y = df[target]
model.fit(X, y)

neutral_df = df.copy()
neutral_df['Wind Speed (mph)'] = 0
neutral_df['Wind Direction'] = 'none'
neutral_df['Tide'] = 'slack'

df['Normalized Speed'] = model.predict(neutral_df[features])

group_cols = ['Date', 'Box Number', 'Session Number', 'Piece Number']
averaged_df = df.groupby(group_cols)['Normalized Speed'].mean().reset_index()
averaged_df.rename(columns={'Normalized Speed': 'Average Normalized Speed'}, inplace=True)

df = df.merge(averaged_df, on=group_cols, how='left')

output_path = '/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/normalized_outputs_v3.csv'
df.to_csv(output_path, index=False)
print(f"Final data with average normalized speeds saved to: {output_path}")