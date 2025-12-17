# measures of center

## mean: 
total_claims         1.499011e+06
total_30day_fills    2.898102e+06
total_days_supply    8.256319e+07
total_drug_cost      7.031466e+07
event_total          6.283970e+02
dtype: float64

## medians: 
total_claims            8204.00
total_30day_fills       9229.70
total_days_supply     251354.00
total_drug_cost      2579252.96
event_total              370.00
dtype: float64

## mode: 
total_claims             12.00
total_30day_fills        12.00
total_days_supply       360.00
total_drug_cost      128016.34
event_total             392.00
Name: 0, dtype: float64

# measures of spread

## iqr: 
total_claims           192137.00
total_30day_fills      231758.90
total_days_supply     5869955.00
total_drug_cost      27652797.14
event_total               845.00
dtype: float64

## range: 
total_claims         6.762890e+07
total_30day_fills    1.662571e+08
total_days_supply    4.932589e+09
total_drug_cost      1.739216e+10
event_total          5.833000e+03
dtype: float64

## variance: 
total_claims         3.286956e+13
total_30day_fills    1.681661e+14
total_days_supply    1.464645e+17
total_drug_cost      2.261710e+17
event_total          6.898031e+05
dtype: float64

## standard deviation: 
total_claims         5.733198e+06
total_30day_fills    1.296789e+07
total_days_supply    3.827068e+08
total_drug_cost      4.755744e+08
event_total          8.305439e+02
dtype: float64

## outliers:        
total_claims  total_30day_fills  ...  total_drug_cost  event_total
0               NaN                NaN  ...              NaN          NaN
1               NaN                NaN  ...              NaN          NaN
2               NaN                NaN  ...              NaN          NaN
3               NaN                NaN  ...              NaN          NaN
4               NaN                NaN  ...              NaN          NaN
...             ...                ...  ...              ...          ...
69132           NaN                NaN  ...              NaN          NaN
69133           NaN                NaN  ...              NaN          NaN
69134           NaN                NaN  ...              NaN          NaN
69135           NaN                NaN  ...              NaN          NaN
69136           NaN                NaN  ...              NaN          NaN

[69137 rows x 5 columns]

# skew and correlation

## skew: 
total_claims          6.621480
total_30day_fills     7.654387
total_days_supply     7.754937
total_drug_cost      24.898620
event_total           2.988900
dtype: float64

## pearson 
correlation:                    total_claims  ...  event_total
total_claims           1.000000  ...     0.063250
total_30day_fills      0.983831  ...     0.021683
total_days_supply      0.977843  ...     0.010703
total_drug_cost        0.232900  ...     0.057894
event_total            0.063250  ...     1.000000

[5 rows x 5 columns]
