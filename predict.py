import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=20,10
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv('datasheet.csv')
df.head(30)
df["Date"] = pd.to_datetime(df.Date, format="%d/%m/%Y")
df.index = df['Date']
df = df.sort_index(ascending=True,axis=0)
data = pd.DataFrame(index=range(0,len(df)),columns=['Date','Bangkok','My Tho','Batdambang','Jessore','Churu','Chennai','Muscat','Riyadh'])
for i in range(0,len(data)):
    data["Date"][i]=df['Date'][i]
    data["Close"][i]=df["Close"][i]
data.head(30)
