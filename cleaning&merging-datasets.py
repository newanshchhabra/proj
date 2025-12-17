import pandas as pd
import re


# formatting text features: remove non alpha. characters & uppercase the field
def formatting(txt):
    return re.sub('[^a-zA-Z]+', '', txt).upper()


# dataset 1 : Medicare Part D

df1 = pd.read_csv("data/Medicare_Part_D_Prescribers_by_Provider_and_Drug_2023.csv",  # import data
                  usecols=['Brnd_Name', 'Gnrc_Name', 'Tot_Clms',  # select features
                           'Tot_30day_Fills', 'Tot_Day_Suply', 'Tot_Drug_Cst'],
                  )

df1 = df1.drop_duplicates(subset=['Brnd_Name'])

df1 = df1.rename(columns={'Brnd_Name': 'brand_name', 'Gnrc_Name': 'generic_name',  # rename feat.
                          'Tot_Clms': 'total_claims',
                          'Tot_30day_Fills': 'total_30day_fills',
                          'Tot_Day_Suply': 'total_days_supply',
                          'Tot_Drug_Cst': 'total_drug_cost'})

df1['brand_name'] = df1['brand_name'].apply(formatting)  # format cat.
df1['generic_name'] = df1['generic_name'].apply(formatting)

df1num = ['total_claims', 'total_30day_fills', 'total_days_supply', 'total_drug_cost']  # format num.
df1[df1num] = df1[df1num].apply(pd.to_numeric, errors='coerce')

# dataset 2: FDA Orange Book

df2 = pd.read_csv("data/products.txt", sep='~',  # import data
                  usecols=['Ingredient', 'Appl_Type'])  # select features

df2['Ingredient'] = df2['Ingredient'].apply(formatting)  # format cat.

df2['type'] = df2['Appl_Type'].map({'N': 1, 'A': 0})  # make brand(1) vs generic(0) binary
del df2['Appl_Type']

# dataset 3: FAERS

df3 = pd.read_csv("data/DRUG25Q1.txt", sep='$',  # import data
                  usecols=['primaryid', 'caseid', 'drugname', 'role_cod'])  # select features

df3 = df3.rename(columns={'primaryid': 'primary_id', 'caseid': 'case_id',  # rename feat.
                          'drugname': 'drug_name', 'role_cod': 'role'})

df3['drug_name'] = df3['drug_name'].apply(formatting)  # format cat.

df3num = ['primary_id', 'case_id']
df3[df3num] = df3[df3num].apply(pd.to_numeric, errors='coerce')  # format num.

df3 = df3.drop_duplicates(subset=['primary_id', 'drug_name'])  # removes duplicates

df3 = df3[df3['role'].isin(['PS', 'SS'])]  # removes all drugs that are not suspected of causing a health event
del df3['role']  # drops the role feature as all rows in datatable are suspected

df3agg = (df3.groupby('drug_name')  # group and aggregate to display drug_name and its event frequency
          .agg(event_total=('drug_name', 'size'))
          .reset_index()
          )

# merge datasets

df1['drug_key'] = df1['generic_name']  # aggregated medicare D data
df2['drug_key'] = df2['Ingredient']  # FDA Orange book data
df3agg['drug_key'] = df3agg['drug_name']  # aggregated FAERS data

df12 = df1.merge(df2[['drug_key', 'type']], how='left', on='drug_key')
df_full = df12.merge(df3agg[['drug_key', 'event_total']], how='left', on='drug_key')
df_full['event_total'] = df_full['event_total'].fillna(0)


df_full.to_csv("data/mergedset.csv", index=False)


