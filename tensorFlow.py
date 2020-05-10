import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from pandas import read_json
from pandas import to_datetime
import json
import pyodbc
from pandas.plotting import autocorrelation_plot
from pandas import DataFrame
from pandas import Series
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller
def getRecentDatabaseData():
        line_items = []
        conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=e013988g.database.windows.net;PORT=1433;DATABASE=learpfyp;UID=e013988g;PWD=lukefyp2020!;TDS_Version=8.0;')
        cursor = conn.cursor()
        sql_text = "SELECT TOP 200 ReadingPPM, DateRegistered FROM CO2_Readings WHERE DATEPART(dd,DateRegistered) = DATEPART(dd, GETDATE() - 7) AND DATEPART(hh, DateRegistered) = (DATEPART(hh, GETDATE()) + 1) ORDER BY DateRegistered ASC"
        cursor.execute(sql_text)
        row = cursor.fetchone()
        while row:
            jsonObject = {
                    'reading': float(row[0]),
                    'dateReg': str(row[1])
                }
            line_items.append(jsonObject)
            row = cursor.fetchone()
        
        conn.close()
        
        return json.dumps(line_items)
        
def checkForAnomaly(reading):
    anomalyFound = False
    series = read_json(getRecentDatabaseData())
    train = series['reading'][:150]
    test = series['reading'][150:]
    model = ARIMA(train, order=(1, 1, 1))  
    fitted = model.fit(disp=-1)  

    # Forecast
    fc, se, conf = fitted.forecast(150, alpha=0.05)  # 95% conf
    # Make as pandas series
    fc_series = Series(fc, index=test.index)
    lower_series = Series(conf[:, 0], index=test.index)
    upper_series = Series(conf[:, 1], index=test.index)
    # Plot
    print(upper_series)
    plt.figure(figsize=(12,5), dpi=100)
    plt.plot(train, label='training')
    plt.plot(test, label='actual')
    plt.plot(fc_series, label='forecast')
    plt.fill_between(lower_series.index, lower_series, upper_series, 
                     color='k', alpha=.15)
    plt.title('Forecast vs Actuals')
    plt.legend(loc='upper left', fontsize=8)
    plt.show()
    for i in upper_series:
        if(reading > i):
            anomalyFound = True
    return anomalyFound

print(checkForAnomaly(300))