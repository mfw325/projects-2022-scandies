#Function to retrieve data

import pandas_datareader as pdr

def get_fred_data(start, end, var_name):
    """Extract data from the Federal Reserve Bank of St. Louis
    
    Args: 
    start (datetime): start date
    end (datetime): end date
    var_name (string): name of the timeseries extracted from the fred

    Returns: 
    (tuple): table with given timeseries from the fred
    """
    table = pdr.DataReader(var_name, 'fred', start, end)
    return table.reset_index()