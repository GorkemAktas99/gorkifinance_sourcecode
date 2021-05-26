import matplotlib.pyplot as plt,mpld3
import pandas_datareader as web
import datetime as dt
import mplfinance as mpf

crypto = "XLM"
currency = "USD"

delta = dt.timedelta(days=7)
end = dt.datetime.now()
start = end-delta

data = web.DataReader(f"{crypto}-{currency}","yahoo",start,end)
print(data)
plt.plot(data['Close'])
mpld3.show()
