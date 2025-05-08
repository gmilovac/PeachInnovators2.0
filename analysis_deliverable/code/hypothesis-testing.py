import pandas as pd
from scipy.stats import pearsonr

# Peach Innovators

data = pd.read_csv('/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/data-by-boat.csv')

filtered_data = data

correlation_watts_speed = pearsonr(filtered_data['Average Watts'], filtered_data['Speed'])
print(f'Correlation between Average Watts and Speed: {correlation_watts_speed}')

correlation_effective_length_speed = pearsonr(filtered_data['Variance Watts'], filtered_data['Speed'])
print(f'Correlation between Variance of Watts and Speed: {correlation_effective_length_speed}')

correlation_length_speed = pearsonr(filtered_data['Average Effective Length'], filtered_data['Speed'])
print(f'Correlation between Average Effective Length and Speed: {correlation_length_speed}')

# Peach Innovators 2.0

data_normalized = pd.read_csv('/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/normalized_outputs_v3.csv')

filtered_data_normalized = data_normalized

correlation_watts_speed_normalized = pearsonr(filtered_data_normalized['Average Watts'], filtered_data_normalized['Average Normalized Speed'])
print(f'Correlation between Average Watts and Average Normalized Speed: {correlation_watts_speed_normalized}')

correlation_effective_length_speed_normalized = pearsonr(filtered_data_normalized['Variance Watts'], filtered_data_normalized['Average Normalized Speed'])
print(f'Correlation between Variance of Watts and Average Normalized Speed: {correlation_effective_length_speed_normalized}')

correlation_length_speed_normalized = pearsonr(filtered_data_normalized['Average Effective Length'], filtered_data_normalized['Average Normalized Speed'])
print(f'Correlation between Average Effective Length and Average Normalized Speed: {correlation_length_speed_normalized}')