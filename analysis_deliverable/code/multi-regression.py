import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score

# Load data
data = pd.read_csv(
    '/Users/adamvonbismarck/Desktop/CS1951A/final-project-peach-innovators/data_deliverable/data/full_data/final-data'
    '-with-watts-stats.csv')

#X = data[['Length', 'Catch Slip', 'Watts', 'Average Watts', 'Variance Watts']]
X = data[['Average Watts', 'Variance Watts', 'Average Effective Length']]

y = data['Speed']

X = sm.add_constant(X)

model = sm.OLS(y, X)

kf = KFold(n_splits=10, shuffle=True, random_state=1)

lm = LinearRegression()
mse_scores = cross_val_score(lm, X, y, scoring='neg_mean_squared_error', cv=kf)

mse_scores = -mse_scores

mean_mse = np.mean(mse_scores)
print(mean_mse)
print(np.sqrt(mean_mse))
variance_mse = np.var(mse_scores)

# print("Cross-validated MSE scores:", mse_scores)
# print("Mean MSE across all folds:", mean_mse)
print("Variance of MSE across all folds:", variance_mse)

model = model.fit()
print(model.summary())
