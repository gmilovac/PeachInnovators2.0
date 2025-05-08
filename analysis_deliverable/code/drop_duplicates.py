import pandas as pd

data = pd.read_csv('/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/final-data-with-watts-stats.csv')

data = data.drop_duplicates(subset=['Box Number', 'Session Number', 'Piece Number'])

data.to_csv('/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/trimmed_data.csv', index=False)