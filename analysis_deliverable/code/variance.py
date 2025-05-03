import pandas as pd

data = pd.read_csv('/Users/adamvonbismarck/Desktop/CS1951A/final-project-peach-innovators/data_deliverable/data'
                   '/full_data/final-data.csv')

average_watts = data.groupby(['Box Number', 'Session Number', 'Piece Number'])['Watts'].mean().reset_index()
average_watts.columns = ['Box Number', 'Session Number', 'Piece Number', 'Average Watts']

average_eff_length = data.groupby(['Box Number', 'Session Number', 'Piece Number'])[
    'Effective Length'].mean().reset_index()
average_eff_length.columns = ['Box Number', 'Session Number', 'Piece Number', 'Average Effective Length']

variance_watts = data.groupby(['Box Number', 'Session Number', 'Piece Number'])['Watts'].var().reset_index()
variance_watts.columns = ['Box Number', 'Session Number', 'Piece Number', 'Variance Watts']

data = pd.merge(data, average_watts, on=['Box Number', 'Session Number', 'Piece Number'], how='left')
data = pd.merge(data, variance_watts, on=['Box Number', 'Session Number', 'Piece Number'], how='left')
data = pd.merge(data, average_eff_length, on=['Box Number', 'Session Number', 'Piece Number'], how='left')

data.to_csv('/Users/adamvonbismarck/Desktop/CS1951A/final-project-peach-innovators/data_deliverable/data'
            '/full_data/final-data-with-watts-stats.csv', index=False)
