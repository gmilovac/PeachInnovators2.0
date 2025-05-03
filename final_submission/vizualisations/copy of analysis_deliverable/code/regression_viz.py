import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv(
    '/Users/adamvonbismarck/Desktop/CS1951A/final-project-peach-innovators/data_deliverable/data/full_data/final-data'
    '-with-watts-stats.csv')

X = pd.DataFrame(data, columns=['Variance Watts', 'Speed'])
Y = pd.DataFrame(data, columns=['Speed'])
sns.lmplot(x="Variance Watts", y="Speed", data=X, order=1, ci=None)
plt.title('Variance in Crew Watts vs Speed')
plt.xlabel('Variance in Crew Watts (W)')
plt.ylabel('Speed (m/s)')
plt.savefig('Variance Watts.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()

X = pd.DataFrame(data, columns=['Average Effective Length', 'Speed'])
Y = pd.DataFrame(data, columns=['Speed'])
sns.lmplot(x="Average Effective Length", y="Speed", data=X, order=1, ci=None)
plt.title('Average Effective Length vs Speed')
plt.xlabel('Average Effective Length (W)')
plt.ylabel('Speed (m/s)')
plt.savefig('Average Effective Length.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()

X = pd.DataFrame(data, columns=['Average Watts', 'Speed'])
Y = pd.DataFrame(data, columns=['Speed'])
sns.lmplot(x="Average Watts", y="Speed", data=X, order=1, ci=None)
plt.title('Average Watts vs Speed')
plt.xlabel('Average Watts (W)')
plt.ylabel('Speed (m/s)')
plt.savefig('Average Watts.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()
