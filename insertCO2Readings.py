import pyodbc
server = 'e013988g.database.windows.net'
database = 'lukefyp'
username = 'e013988g'
password = 'lukefyp2020!'
cnxn = pyodbc.connect('SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT TOP 20 FROM Device_Details")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()