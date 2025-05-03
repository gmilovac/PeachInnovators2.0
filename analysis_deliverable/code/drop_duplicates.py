import pandas as pd

data = pd.read_csv('/Users/adamvonbismarck/Desktop/CS1951A/final-project-peach-innovators/data_deliverable/data'
                   '/full_data/final-data-with-watts-stats.csv')

data = data.drop_duplicates(subset=['Box Number', 'Session Number', 'Piece Number'])

data.to_csv('/Users/adamvonbismarck/Desktop/CS1951A/final-project-peach-innovators/data_deliverable/data/trimmed-data'
            '.csv', index=False)