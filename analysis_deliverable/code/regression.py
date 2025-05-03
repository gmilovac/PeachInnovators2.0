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


data = read_data(
    '/Users/adamvonbismarck/Desktop/CS1951A/final-project-peach-innovators/data_deliverable/data/full_data/final-data-with-watts-stats.csv')

X = pd.DataFrame(data, columns=['Variance Watts', 'Speed'])
Y = pd.DataFrame(data, columns=['Speed'])
sns.lmplot(x="Variance Watts", y="Speed", data=X, order=1, ci=None)
plt.title('Variance in Crew Watts vs Speed')
plt.xlabel('Variance in Crew Watts (W)')
plt.ylabel('Speed (m/s)')
plt.savefig('Variance Watts.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()
