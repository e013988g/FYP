import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from pandas import read_json
import json
import pyodbc
from pandas.plotting import autocorrelation_plot
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA

def getRecentDatabaseData():
    line_items = []
    conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=e013988g.database.windows.net;PORT=1433;DATABASE=learpfyp;UID=e013988g;PWD=lukefyp2020!;TDS_Version=8.0;')
    cursor = conn.cursor()
    sql_text = "SELECT TOP 1000 ReadingPPM, DateRegistered FROM CO2_Readings WHERE DateRegistered >= DATEADD(day,-1,GETDATE()) ORDER BY DateRegistered DESC "
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

series = read_json(getRecentDatabaseData())
print(series)
model = ARIMA(series['reading'], order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())
