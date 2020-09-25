from datetime import datetime
from dateutil.relativedelta import relativedelta
import FinanceDataReader as fdr
import numpy as np

# code = input("종목코드:")
code = "GOOG"

df = fdr.DataReader(code, datetime.today()+relativedelta(days=-180))

print(df.axes)

global_min = float("INF")
max_profit = float("-INF")
global global_min_time
global global_max_time

for index, row in df.iterrows():
    if row.Low < global_min:
        global_min = row.Low
        global_min_time = index
    if row.High - global_min > max_profit:
        max_profit = row.High - global_min
        global_max_time = index

print(df.loc(np.datetime64(global_max_time.date())))

print(global_min_time.strftime('%Y-%m-%d'), global_max_time.strftime('%Y-%m-%d'),  "%.2f$" %(max_profit))

# nasdaq = fdr.StockListing('NASDAQ')


# if nasdaq[nasdaq.Symbol == "AAPL"].empty:
#     print("True")
# else:
#     print("False")