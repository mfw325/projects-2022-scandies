#Function to retrieve data

def get_fred_data(start, end, var_name):
    
    table = pdr.DataReader(var_name, 'fred', start, end)
    """We first create a function that is used to retrieve all four datasets. 
    By creating this function, we are able to reset the index and get the DATE field as a column, 
    which we will need for the visualization and analysis.
    """
    return table.reset_index()