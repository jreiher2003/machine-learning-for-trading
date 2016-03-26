 # -*- coding: utf-8 -*-
import os

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """ Returns CSV file path given ticker symbol. ie. "data/IBM.csv" """
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """ Read stock data (adjusted close) for given symbols from CSV files. """
    df = pd.DataFrame(index=dates)
    for symbol in symbols:
        temp = pd.read_csv(symbol_to_path(symbol, base_dir="data"), 
                           index_col="Date", 
                           parse_dates=True, 
                           usecols=["Date", "Adj Close"])
       
        temp = temp.rename(columns={"Adj Close": symbol})
        df = df.join(temp, how="inner")
        df = df.sort_index(axis=0, ascending=[1])   
    return df

def plot_data(df, title="Stock Prices"):
    ax = df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def test_run():
    dates = pd.date_range("2010-01-01", "2012-12-31")
    symbols = ["SPY", "XOM", "GOOG", "GLD"]
    df = get_data(symbols, dates)
    # plot_data(df)
    print df.head()

def test_run2():
    dates = pd.date_range("2012-01-01", "2012-12-31")
    symbols = ["SPY"]
    df = get_data(symbols, dates)
    ax = df["SPY"].plot(title="SPY rolling mean", label="SPY")
    rm_SPY = pd.rolling_mean(df["SPY"], window=20)
    rm_SPY.plot(label="Rolling Mean", ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")
    plt.show()

def get_bollinger_bands(rm, rstd):
    """ Return upper and lower Bollinger Bands. """
    upper_band = (rm + (rstd * 2))
    lower_band = (rm - (rstd * 2))
    return upper_band, lower_band

def computer_daily_returns(df):
    """ compute and return the daily return values. """
    return (price1/price2) -1

def test_run3():
    dates = pd.date_range("2012-01-01", "2012-12-31")
    symbols = ["SPY"]
    df = get_data(symbols,dates) 

    ax = df["SPY"].plot(title=r"Bollinger Bands &0174;")
    ax.set_xlabel("DATE")
    ax.set_ylabel("Price")
    ax.legend(loc="upper right")

    rm_SPY = pd.rolling_mean(df["SPY"], window=20)
    rstd_SPY = pd.rolling_std(df["SPY"], window=20)


    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)
    
    rm_SPY.plot(label="Rolling Mizean", ax=ax)

    upper_band.plot(label="upper band", ax=ax)
    lower_band.plot(label="lower band", ax=ax)
    plt.show()




if __name__ == "__main__":
    test_run()
    # test_run2()
    # test_run3()
