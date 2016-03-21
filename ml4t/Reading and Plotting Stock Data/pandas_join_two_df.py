import os
import pandas as pd

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

def test():
    start_date = "2010-03-10"
    end_date = "2010-03-15"
    dates = pd.date_range(start_date,end_date)
    symbols = ["GOOG", "IBM", "GLD"]
    
    df1 = get_data(symbols,dates)
    df1 = df1[["SPY", "IBM"]]
    print df1


if __name__ == "__main__":
    test()