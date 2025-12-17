import pandas as pd

df = pd.read_csv("data/mergedset.csv")

dfnum = ['total_claims', 'total_30day_fills', 'total_days_supply',
         'total_drug_cost', 'event_total']

shape = df.shape
desc = df[dfnum].describe()

# measures of center

means = df[dfnum].mean()
medians = df[dfnum].median()
modes = df[dfnum].mode().iloc[0]

# measures of spread

q1 = df[dfnum].quantile(0.25)
q3 = df[dfnum].quantile(0.75)
iqr = q3 - q1
lowerb = q1 - 1.5 * iqr
upperb = q3 + 1.5 * iqr
outliers = df[dfnum][(df[dfnum] < lowerb) | (df[dfnum] > upperb)]

range = (df[dfnum].max() - df[dfnum].min())
variance = df[dfnum].var()
std_dev = df[dfnum].std()

# skew and correlation

skew = df[dfnum].skew()
corr = df[dfnum].corr(method='pearson')

# print

print("measures of center")
print("\nmean:", means)
print("\nmedians:", medians)
print("\nmode:", modes)

print("\nmeasures of spread")
print("\niqr:", iqr)
print("\nrange:", range)
print("\nvariance:", variance)
print("\nstandard deviation:", std_dev)
print("\noutliers:", outliers)

print("\nskew and correlation")
print("\nskew:", skew)
print("\npearson correlation:", corr)


corr.to_csv("2deliverables/correlation_matrix.csv")
outliers.to_csv("2deliverables/outliers.csv")