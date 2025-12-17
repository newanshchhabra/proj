import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
matplotlib.use("TkAgg")

df = pd.read_csv("data/mergedset.csv")

# correlation matrix

dfnum = ['total_claims', 'total_30day_fills', 'total_days_supply',
         'total_drug_cost', 'event_total']
matrix = df[dfnum].corr()

plt.figure()
plt.imshow(matrix, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.xticks(np.arange(len(dfnum)), dfnum, rotation= 90)
plt.yticks(np.arange(len(dfnum)), dfnum)

plt.title("correlation matrix ")
plt.tight_layout()
plt.savefig("3deliverables/correlation.png", dpi=300, bbox_inches='tight')
plt.show()

# scatter

brand = df[df['type'] == 1]
generic = df[df['type'] == 0]
plt.scatter(generic['total_claims'], generic['event_total'], alpha=0.2, label='Generic', color='blue')
plt.scatter(brand['total_claims'], brand['event_total'], alpha=0.2, label='Brand', color='grey')

plt.xlabel("total claims on log scale")
plt.xscale('log')
plt.ylabel("adverse events")
plt.legend()
plt.title("total claims(log) vs adverse events")
plt.savefig("3deliverables/scatterplot.png", dpi=300, bbox_inches='tight')
plt.show()

# KDE

brand = df[df['type'] == 1]['event_total']
generic = df[df['type'] == 0]['event_total']

brand.plot(kind='kde', label='Brand', linewidth=2)
generic.plot(kind='kde', label='Generic', linewidth=2)

plt.xlabel("adverse events")
plt.ylabel("density")
plt.title("KDE of adverse events (comparing generic vs brand)")
plt.legend()
plt.savefig("3deliverables/KDE.png", dpi=300, bbox_inches='tight')
plt.show()

# bar plot

df['cost_per_claim'] = df['total_drug_cost'] / df['total_claims']
median_cost = df.groupby('type')['cost_per_claim'].median()
mean_cost = df.groupby('type')['cost_per_claim'].mean()

bar_names = ['Generic (median)', 'Generic (mean)', 'Brand(median)', 'Brand(mean)']
values = [median_cost[0], mean_cost[0], median_cost[1], mean_cost[1]]
plt.bar(bar_names, values, color='black', )

plt.ylabel("cost per claim ($)")
plt.title("cost per claim: brand vs generic & mean vs median")
plt.savefig("3deliverables/barplot.png", dpi=300, bbox_inches='tight')
plt.show()