import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    # Note: DO NOT modify anything else!
    
    df.ix[start_index:end_index]
    df = df[columns]
    df.plot()
    plt.show

def symbol_to_path(symbol, base_dir="data"):
    """ Returns CSV file path given ticker symbol. ie. "data/IBM.csv" """
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """ Read stock data (adjusted close) for given symbols from CSV files. """
    df = pd.DataFrame(index=dates)
    if "SPY" not in symbols:
        symbols.insert(0, "SPY")
    for symbol in symbols:
        temp = pd.read_csv(symbol_to_path(symbol, base_dir="data"), 
                           index_col="Date", 
                           parse_dates=True, 
                           usecols=["Date", "Adj Close"])
       
        temp = temp.rename(columns={"Adj Close": symbol})
        
        df = df.join(temp, how="inner")
        df = df.sort_index(axis=0, ascending=[1])
         
    return df

def normalize_data(df):
    """ Normalize stock prices using the first row of the dataframe. """
    return df / df.ix[0,:]


def plot_data(df, title="Stock Prices"):
    ax = df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def test():
    start_date = "2010-01-01"
    end_date = "2010-12-31"
    dates = pd.date_range(start_date,end_date)
    symbols = ["GOOG", "IBM", "GLD"]
    
    df1 = get_data(symbols,dates)
    df1 = normalize_data(df1)
    # df1 = df1[["SPY", "IBM"]]
    print df1
    plot_data(df1)
    plot_selected(df1, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')


if __name__ == "__main__":
    test()