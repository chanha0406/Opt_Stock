from django.http import HttpResponse
from django.shortcuts import render
from .models import stock
from django.utils import timezone

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import io, urllib, base64
import numpy as np

def optimal_stock(symbol = "AAPL"):
    df = fdr.DataReader(symbol, datetime.today()+relativedelta(days=-180))    

    min_Low = float("INF")
    profit = float("-INF")
    buy_time = np.datetime64('nat')
    sell_time = np.datetime64('nat')

    for index, row in df.iterrows():
        if row.Low < min_Low:
            min_Low = row.Low
            buy_time = index
        if row.High - min_Low > profit:
            profit = row.High - min_Low
            sell_time = index

    plt.clf()
    plt.figure(figsize=(8, 5))
    plt.plot(df[["Close", "Open", "Low", "High"]])

    plt.axvline(x=buy_time, label='buy time', c='r')
    plt.axvline(x=sell_time, label='sell time', c='b')
    # plt.legend(["Close", "Open", "Low", "High", "Buy Time", "Sell Time"], bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.legend(["Close", "Open", "Low", "High", "Buy Time", "Sell Time"], bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol = 4, mode="expand", borderaxespad=0.) 
    #plt.axis('scaled')
    
    # fig = plt.plot(df[["Close", "Open", "Low", "High"]])
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    plot = base64.b64encode(buf.read())
    plot = urllib.parse.quote(plot)

    return buy_time.date(), sell_time.date(), profit, plot

def get_stock_data(symbol):
    # snp = fdr.StockListing('S&P500')

    try:
        fdr.DataReader(symbol, datetime.today())    
    except ValueError:
        return False

    return True
    # return not snp[snp.Symbol==symbol].empty

def stock_view(request):
    if not request.GET.get('symbol'):
        symbol = "AAPL"
    else :
        symbol = request.GET.get('symbol')

    symbol = symbol.upper()
    try:
        selected_stock = stock.objects.get(symbol = symbol)
        #delata = selected_stock.update_time - timezone.now()
        if (timezone.now() - selected_stock.update_time)  > timedelta(seconds=6): 
             opt = optimal_stock(symbol)
             selected_stock.updtae(opt[0], opt[1], opt[2], opt[3])
        else:
            opt = selected_stock.get_data()

    except stock.DoesNotExist:
        if get_stock_data(symbol):
            opt = optimal_stock(symbol)
            stock.objects.create(buy_date=opt[0], sell_date=opt[1], profit=opt[2], symbol = symbol, plot=opt[3])
        else:
            return render(request, 'no_data.html', {'symbol': symbol})     
        
    return render(request, 'stock.html', {'opts': opt, 'symbol':symbol})     

def index(request):
    return render(request, 'index.html')     
