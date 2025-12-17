import pandas as pd
import numpy as np
import matplotlib.pyplot

matplotlib.use("TkAgg")
from sklearn.preprocessing import RobustScaler

df = pd.read_csv("data/mergedset.csv")

# remove brand_name feature and duplicates

df = (df
      .groupby(['drug_key', 'generic_name', 'type'])
      .agg(med_claims=('total_claims', 'median'),
           med_days_supply=('total_days_supply', 'median'),
           med_drug_cost=('total_drug_cost', 'median'),
           event_total=('event_total', 'sum')
           )
      .reset_index()
      )

df = df[df['type'].notna()]  # ensuring no empty values

# creating a split dataset

check = (df
         .groupby('generic_name')
         ['type']
         .nunique())

valid = check[check == 2].index
df = df[df['generic_name'].isin(valid)]  # removes all drugs that don't hae both a brand and a generic

brand = df[df['type'] == 1]
generic = df[df['type'] == 0]

df = brand.merge(  # creates separation of brand and generic within the features
    generic,
    on='drug_key',
    how='left',
    suffixes=('_brand', '_generic'))


# feature engineering & dealing with outliers

df['log_event_total_brand'] = np.log1p(df['event_total_brand'])
df['log_event_total_generic'] = np.log1p(df['event_total_generic'])

df['log_med_drug_cost_brand'] = np.log1p(df['med_drug_cost_brand'])
df['log_med_drug_cost_generic'] = np.log1p(df['med_drug_cost_generic'])

# feature selection

features2 = ['med_claims_brand', 'med_claims_generic',
             'med_days_supply_brand', 'med_days_supply_generic',
             'log_med_drug_cost_brand', 'log_med_drug_cost_generic',
             'log_event_total_brand', 'log_event_total_generic']


df = df[features2]
df.to_csv("data/final_modeling.csv", index=False)
