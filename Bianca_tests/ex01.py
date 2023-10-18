import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

data = pd.read_csv('')

x = data.drop('TIPO_VIDRO',axis=1)
y = data['TIPO_VIDRO']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

norm = normalizer()
x_train = norm.fit_transform(x_train)
x_test = norm.transform(x_test)

logistic_model = LogisticRegression()
logistic_model.fit(x_train,y_train)
