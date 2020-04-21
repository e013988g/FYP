import tensorflow as tf
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import json
import pyodbc

def getRecentDatabaseData():
    line_items = []
    conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=e013988g.database.windows.net;PORT=1433;DATABASE=learpfyp;UID=e013988g;PWD=lukefyp2020!;TDS_Version=8.0;')
    cursor = conn.cursor()
    sql_text = "SELECT TOP 100 ReadingPPM, DateRegistered FROM CO2_Readings ORDER BY DateRegistered DESC"
    cursor.execute(sql_text)
    row = cursor.fetchone()
    while row:
        jsonObject = {
                'reading': str(row[0]),
                'dateReg': str(row[1])
            }
        print(jsonObject)
        line_items.append(jsonObject)
    #print(json.dumps(line_items))
    conn.close()
    
    return line_items

getRecentDatabaseData()
