import os
import json
import pyodbc

def getRecentDatabaseData(self):
    line_items = []
    conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=e013988g.database.windows.net;PORT=1433;DATABASE=learpfyp;UID=e013988g;PWD=lukefyp2020!;TDS_Version=8.0;')
    cursor = conn.cursor()
    user_name = "lukeearp98@outlook.com"
    password = "password"
    sql_text = "SELECT * FROM Device_Details WHERE Email='" + user_name +"' AND Password='" + password + "'"
    cursor.execute(sql_text)
    row = cursor.fetchone()
    
    while row:
        jsonObject = {
                'sendText': row[3],
                'sendEmail': row[4]
            }
        line_items.append(jsonObject)
        row = cursor.fetchone()
    
    conn.close()
    
    print(jsonObject)
    
    return json.dumps(line_items)

getRecentDatabaseData();