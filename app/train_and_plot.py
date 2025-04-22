import pickle

import pandas as pd
import math
import datetime
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

# Load data (you should replace this with a mounted volume or cloud storage in deployment)
GOOGL = 'GOOGL.csv'
df = pd.read_csv(GOOGL)

df = df[['Open','High','Low','Close','Volume']]
df['HL_PCT'] = (df['High'] - df['Low']) / df['Low'] * 100
df['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100

df = df[['Close','HL_PCT','PCT_change','Volume']]

forecast_col = 'Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'],axis=1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
y = np.array(df['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train, y_train)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)

accuracy = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)
df['Forecast'] = np.nan

if not isinstance(df.index, pd.DatetimeIndex):
    df.index = pd.to_datetime(df.index)

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
