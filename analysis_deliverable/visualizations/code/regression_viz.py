import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Peach Innovators

data = pd.read_csv(
    '/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/final-data-with-watts-stats.csv')

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


# Peach Innovators 2.0

data = pd.read_csv(
    '/Users/gordanmilovac/Desktop/cs1420/PeachInnovators2.0/data_deliverable/data/full_data/normalized_outputs_v3.csv')

sns.lmplot(x="Variance Watts", y="Average Normalized Speed", data=data, order=1, ci=None)
plt.title('Variance in Crew Watts vs Average Normalized Speed')
plt.xlabel('Variance in Crew Watts (W)')
plt.ylabel('Average Normalized Speed (m/s)')
plt.savefig('Variance_Watts_Normalized_Speed.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()

sns.lmplot(x="Average Effective Length", y="Average Normalized Speed", data=data, order=1, ci=None)
plt.title('Average Effective Length vs Average Normalized Speed')
plt.xlabel('Average Effective Length (cm)')
plt.ylabel('Average Normalized Speed (m/s)')
plt.savefig('Average_Effective_Length_Normalized_Speed.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()

sns.lmplot(x="Average Watts", y="Average Normalized Speed", data=data, order=1, ci=None)
plt.title('Average Watts vs Average Normalized Speed')
plt.xlabel('Average Watts (W)')
plt.ylabel('Average Normalized Speed (m/s)')
plt.savefig('Average_Watts_Normalized_Speed.png', transparent=True, bbox_inches='tight', dpi=300)
plt.show()