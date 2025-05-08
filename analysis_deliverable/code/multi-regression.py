import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score

# Peach Innovators

data = pd.read_csv(
    '/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/final-data-with-watts-stats.csv')

X = data[['Average Watts', 'Variance Watts', 'Average Effective Length']]

y = data['Speed']

X = sm.add_constant(X)

model = sm.OLS(y, X)

kf = KFold(n_splits=10, shuffle=True, random_state=1)

lm = LinearRegression()
mse_scores = cross_val_score(lm, X, y, scoring='neg_mean_squared_error', cv=kf)

mse_scores = -mse_scores

mean_mse = np.mean(mse_scores)
print(f"Mean MSE for Raw Speed: {mean_mse}")
print(f"RMSE for Raw Speed: {np.sqrt(mean_mse)}")

variance_mse = np.var(mse_scores)
print("Variance of MSE across all folds for Raw Speed:", variance_mse)

model = model.fit()
print(model.summary())

# Peach Innovators 2.0

data_normalized = pd.read_csv('/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/normalized_outputs_v3.csv')

X_normalized = data_normalized[['Average Watts', 'Variance Watts', 'Average Effective Length']]

y_normalized = data_normalized['Average Normalized Speed']

X_normalized = sm.add_constant(X_normalized)

model_normalized = sm.OLS(y_normalized, X_normalized)

kf_normalized = KFold(n_splits=10, shuffle=True, random_state=1)

lm_normalized = LinearRegression()

mse_scores_normalized = cross_val_score(lm_normalized, X_normalized, y_normalized, scoring='neg_mean_squared_error', cv=kf)

mse_scores_normalized = -mse_scores_normalized

mean_mse_normalized = np.mean(mse_scores_normalized)
print(f"Mean MSE for Normalized Speed: {mean_mse_normalized}")
print(f"RMSE for Normalized Speed: {np.sqrt(mean_mse_normalized)}")

variance_mse_normalized = np.var(mse_scores_normalized)
print(f"Variance of MSE across all folds for Normalized Speed: {variance_mse_normalized}")

model_normalized = model_normalized.fit()
print(model_normalized.summary())
