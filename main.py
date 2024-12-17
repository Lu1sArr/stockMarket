from stock import Stock
from yahoo_fin import stock_info 
import yfinance as yf
import warnings
warmings.filterwarnings("ignore")

portfolio = []

def addStock(name,ticker,sector,):
    price = round(float(stock_info.get_live_price(ticker)),2)
    newStock = Stock(name,ticker,sector,price,numOfShares)
    portfolio.append(newStock)