from pandas import Series, DataFrame
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from nba_game_logs_pandas import *

def rolling_mean(data, window, min_periods=1, center=False):
    ''' Function that computes a rolling mean

    Parameters
    ----------
    data : DataFrame or Series
           If a DataFrame is passed, the rolling_mean is computed for all columns.
    window : int or string
             If int is passed, window is the number of observations used for calculating 
             the statistic, as defined by the function pd.rolling_mean()
             If a string is passed, it must be a frequency string, e.g. '90S'. This is
             internally converted into a DateOffset object, representing the window size.
    min_periods : int
                  Minimum number of observations in window required to have a value.

    Returns
    -------
    Series or DataFrame, if more than one column    
    '''
    def f(x):
        '''Function to apply that actually computes the rolling mean'''
        if center == False:
            dslice = col[x-pd.datetools.to_offset(window).delta+timedelta(0,0,1):x]
                # adding a microsecond because when slicing with labels start and endpoint
                # are inclusive
        else:
            dslice = col[x-pd.datetools.to_offset(window).delta/2+timedelta(0,0,1):
                         x+pd.datetools.to_offset(window).delta/2]
        if dslice.size < min_periods:
            return np.nan
        else:
            return dslice.mean()

    data = DataFrame(data.copy())
    dfout = DataFrame()
    if isinstance(window, int):
        dfout = pd.rolling_mean(data, window, min_periods=min_periods, center=center)
    elif isinstance(window, basestring):
        idx = Series(data.index.to_pydatetime(), index=data.index)
        for colname, col in data.iteritems():
            result = idx.apply(f)
            result.name = colname
            dfout = dfout.join(result, how='outer')
    if dfout.columns.size == 1:
        dfout = dfout.ix[:,0]
    return dfout


if __name__ == "__main__":
    # Example
    idx = [datetime(2011, 2, 7, 0, 0),
           datetime(2011, 2, 7, 0, 1),
           datetime(2011, 2, 7, 0, 1, 30),
           datetime(2011, 2, 7, 0, 2),
           datetime(2011, 2, 7, 0, 4),
           datetime(2011, 2, 7, 0, 5),
           datetime(2011, 2, 7, 0, 5, 10),
           datetime(2011, 2, 7, 0, 6),
           datetime(2011, 2, 7, 0, 8),
           datetime(2011, 2, 7, 0, 9)]
    idx = pd.Index(idx)
    print idx
    vals = np.arange(len(idx)).astype(float)
    print vals
    s = Series(vals, index=idx)
    rm = rolling_mean(s, window='2min')
    print rm
    print find_player("Arron Afflalo")
