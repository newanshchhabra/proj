import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler

# load data
df = pd.read_csv("data/final_modeling.csv")

# target and features

X = df[
    ['med_claims_brand',
     'med_days_supply_brand',
     'log_med_drug_cost_brand',
     'log_event_total_brand']
]

y = df['med_days_supply_generic']

# train-test split
Xtrain, Xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# pipeline
pipeline = Pipeline(
    [("scaler", RobustScaler()),
     ("model", ElasticNet(
         alpha=1.0,
         l1_ratio=0.5,
         max_iter=10000,
         random_state=42
     ))]
)

# fit
cv_scores = cross_val_score(pipeline, Xtrain, ytrain, cv=5, scoring="r2")
pipeline.fit(Xtrain, ytrain)
ypredtrain = pipeline.predict(Xtrain)
ypredtest = pipeline.predict(Xtest)

# metrics
trainrmse = mean_squared_error(ytrain, ypredtrain) ** 0.5
testrmse = mean_squared_error(ytest, ypredtest) ** 0.5
trainmae = mean_absolute_error(ytrain, ypredtrain)
testmae = mean_absolute_error(ytest, ypredtest)
trainr2 = r2_score(ytrain, ypredtrain)
testr2 = r2_score(ytest, ypredtest)

# print
print("model performance:")
print("train RMSE:", trainrmse)
print("test RMSE:", testrmse)
print("train MAE:", trainmae)
print("test MAE:", testmae)
print("train R²:", trainr2)
print("test R²:", testr2)
print("CV R² scores:", cv_scores)
print("mean CV R²:", cv_scores.mean())
