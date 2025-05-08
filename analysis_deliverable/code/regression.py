import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def read_data(path):
    """
    Reads the data at the provided files path.

    :param path: path to dataset
    :return: raw data
    """
    with open(path) as data_file:
        data = pd.read_csv(data_file)
    return data

# Peach Innovators

data = read_data(
    '/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/final-data-with-watts-stats.csv')

X = pd.DataFrame(data, columns=['Variance Watts', 'Speed'])
Y = pd.DataFrame(data, columns=['Speed'])
sns.lmplot(x="Variance Watts", y="Speed", data=X, order=1, ci=None)
plt.title('Variance in Crew Watts vs Speed')
plt.xlabel('Variance in Crew Watts (W)')
plt.ylabel('Speed (m/s)')
plt.savefig('Variance Watts.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()

# Peach Innovators 2.0

data_normalized = read_data(
    '/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/normalized_outputs_v3.csv')

X_normalized = pd.DataFrame(data_normalized, columns=['Variance Watts', 'Average Normalized Speed'])
sns.lmplot(x="Variance Watts", y="Average Normalized Speed", data=X_normalized, order=1, ci=None)
plt.title('Variance in Crew Watts vs Average Normalized Speed')
plt.xlabel('Variance in Crew Watts (W)')
plt.ylabel('Average Normalized Speed (m/s)')
plt.savefig('Variance_Watts_Normalized_Speed.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()
