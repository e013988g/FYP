import pyodbc
import datetime
import sys

class insertReading():
    def insertCO2Reading(self, ReadingPPM):
        try:
            conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=e013988g.database.windows.net;PORT=1433;DATABASE=learpfyp;UID=e013988g;PWD=lukefyp2020!;TDS_Version=8.0;')
            cursor = conn.cursor()
            now = datetime.datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S.%s")
            sql_text = "INSERT INTO CO2_Readings (DeviceID, ReadingPPM) VALUES (1," + str(ReadingPPM) + ")"
            print(sql_text)
            cursor.execute(sql_text)
            conn.commit()
            conn.close()
        except:
            e = sys.exc_info()[1]
            print("error: %s" % e)
            