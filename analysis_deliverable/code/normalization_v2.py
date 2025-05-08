import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

file_path = '/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/final-data-with-conditions-edited.csv'
df = pd.read_csv(file_path, sep=';')

group_cols = ['Date', 'Box Number', 'Session Number', 'Piece Number']

agg_df = df.groupby(group_cols).agg({
    'Watts': 'mean',
    'Rate': 'mean',
    'Effective Length': 'mean',
    'Wind Speed (mph)': 'mean',
    'Speed': 'mean',
    'Wind Direction': lambda x: x.mode().iloc[0],
    'Tide': lambda x: x.mode().iloc[0]
}).reset_index()

agg_df.rename(columns={'Speed': 'Observed Speed'}, inplace=True)

feature_cols = ['Watts', 'Rate', 'Effective Length', 'Wind Speed (mph)', 'Wind Direction', 'Tide']
target_col = 'Observed Speed'

categorical_features = ['Wind Direction', 'Tide']
numerical_features = ['Watts', 'Rate', 'Effective Length', 'Wind Speed (mph)']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_features),
    ('cat', OneHotEncoder(drop='first'), categorical_features)
])

pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('regressor', XGBRegressor(n_estimators=100, random_state=42))
])

X = agg_df[feature_cols]
y = agg_df[target_col]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'RMSE on held-out test set: {rmse:.4f}')

agg_df['Predicted Normalized Speed'] = pipeline.predict(X)

df = df.merge(agg_df[group_cols + ['Predicted Normalized Speed']], on=group_cols, how='left')
df['Normalized Speed'] = df['Predicted Normalized Speed']

output_path = '/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/normalized_outputs_v2.csv'
df.to_csv(output_path, index=False)
print(f'Normalized speeds saved to {output_path}')