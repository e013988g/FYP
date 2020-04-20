import pyodbc
import datetime

class insertReading():
    def insertCO2Reading(ReadingPPM):
        try:
            #conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=e013988g.database.windows.net;PORT=1433;DATABASE=learpfyp;UID=e013988g;PWD=lukefyp2020!;TDS_Version=8.0;')
            #cursor = conn.cursor()
            #now = datetime.datetime.now()
            #now = now.strftime("%Y-%m-%d %H:%M:%S.%s.%f")[:-3]
            #sql_text= "INSERT INTO CO2_Readings (DeviceID, ReadingPPM, DateRegistered) VALUES (1," + ReadingPPM + "," + now  + ")"
            #cursor.execute(sql_text)
            #conn.commit()
            #cursor.close()
            #conn.close()
        except:
            e = sys.exc_info()[0]
            print("error: %s" % e)
            
        
    def insertCOReading(ReadingPPM):
        try:
            conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=e013988g.database.windows.net;PORT=1433;DATABASE=learpfyp;UID=e013988g;PWD=lukefyp2020!;TDS_Version=8.0;')
            cursor = conn.cursor()
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S.%s.%f")[:-3]
            sql_text= "INSERT INTO CO_Readings (DeviceID, ReadingPPM, DateRegistered) VALUES (1," + ReadingPPM + "," + now  + ")"
            cursor.execute(sql_text)
            conn.commit()
            cursor.close()
            conn.close()
            print("affected rows = {}".format(cursor.rowcount))
        except:
            e = sys.exc_info()[0]
            print("error: %s" % e)

    