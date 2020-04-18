import pyodbc
conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=e013988g.database.windows.net;PORT=1433;DATABASE=learpfyp;UID=e013988g;PWD=lukefyp2020!;TDS_Version=8.0;')
cursor = conn.cursor()
sql_text= 'SELECT * FROM Device_Details'
cursor.execute(sql_text)
result=cursor.fetchall()
for row in result:
       p=row[1] 
       q=row[2]
       print p
       print q