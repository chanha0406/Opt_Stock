from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime
from dateutil.relativedelta import relativedelta
import FinanceDataReader as fdr

def optimal_stock(code = "AAPL"):
    df = fdr.DataReader(code, datetime.today()+relativedelta(days=-180))

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

    return (global_min_time.strftime('%Y-%m-%d'), global_max_time.strftime('%Y-%m-%d'), "%.2f$" %(max_profit))

def stock(request, stock):
    opt = optimal_stock(stock)
    return render(request, 'stock.html', {'opts': opt})     

def index(request):
    opt = optimal_stock()
    return HttpResponse(opt[0]+ " " + opt[1] + " " + opt[2])