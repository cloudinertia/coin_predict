from pandas_datareader import data
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2017,01,01)
end = datetime.datetime(2017,12,01)
apple = data.DataReader('AAPL','yahoo',start,end)

apple.Close.plot()
plt.show()
