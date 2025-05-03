import pandas as pd
from scipy.stats import pearsonr

# data = pd.read_csv('data-sample.csv')
data = pd.read_csv('/data_deliverable/data/full_data/data-by-boat.csv')

# filtered_data = data[data['Piece Number'] == 1]
filtered_data = data

correlation_watts_speed = pearsonr(filtered_data['Average Watts'], filtered_data['Speed'])
print(f'Correlation between Average Watts and Speed: {correlation_watts_speed}')

correlation_effective_length_speed = pearsonr(filtered_data['Variance Watts'], filtered_data['Speed'])
print(f'Correlation between Variance of Watts and Speed: {correlation_effective_length_speed}')

correlation_length_speed = pearsonr(filtered_data['Average Effective Length'], filtered_data['Speed'])
print(f'Correlation between Average Effective Length and Speed: {correlation_length_speed}')
