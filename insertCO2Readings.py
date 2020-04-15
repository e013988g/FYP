import jaydebeapi

username = 'e013988g'
password = 'lukefyp2020!'
driver= '/usr/local/lib/python2.7/dist-packages/pyodbc.so'
conn = jaydebeapi.connect("org.hsqldb.jdbcDriver", "jdbc:hsqldb:mem:e013988g.database.windows.net/lukefyp", [username, password], "/path/to/hsqldb.jar")
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
curs = conn.cursor()
cursor.execute("SELECT TOP 20 FROM Device_Details")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()