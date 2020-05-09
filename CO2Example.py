from mqCO2 import *
from mqCO import *
from sendCO2Text import *
from sendCO2Email import *
from sendCOEmail import *
from sendCOText import *
from sendDataToDB import *
from getNotificationSettings import *
import sys, time, json
from findCO2Anomaly import *
from findCOAnomaly import *
import threading

def findAnomalies(CO2Reading, COReading):
    findCO2Anomaly = CO2LinearRegression();
    findCO2Anomaly.checkForAnomaly(CO2Reading);
    
    findCOAnomaly = COLinearRegression();
    findCOAnomaly.checkForAnomaly(COReading);
try:
    CO2Trigerred = False
    PreviousTriggeredState = False
    COPreviousTriggeredState = False
    mqCO2 = MQCO2();
    mqCO = MQCO();
    sendDataToDb = insertReading();
    CO2Text = sendCO2Text();
    COText = sendCOText();
    sendCarbonDioxideEmail = sendCO2Email();
    sendCarbonMonoxideEmail = sendCOEmail();
    notifications = getNotifications();
    
    while True:
            
            CO2Perc = mqCO2.MQPercentage()
            COPerc = mqCO.MQPercentage()
            sendDataToDb.insertCO2Reading(CO2Perc["SMOKE"])
            sendDataToDb.insertCOReading(COPerc["CO"])
            readingThread = threading.Thread(target=findAnomalies, args=(CO2Perc["SMOKE"], COPerc["CO"],))
            readingThread.start()
            sys.stdout.write("\r")
            sys.stdout.write("\033[K")
            sys.stdout.write("CO2: %g ppm, CO: %g ppm" % ((CO2Perc["SMOKE"]), (COPerc["CO"])))
            sys.stdout.flush()
            time.sleep(15)
            notificationSettings = json.loads(notifications.getSettings())
            sendText = notificationSettings[0]["sendText"]
            sendEmail = notificationSettings[0]["sendEmail"]
            if (CO2Perc["SMOKE"]) > 1000:
                if PreviousTriggeredState == False:
                    message = CO2Text.createClientMessage(sendText)
                    email = sendCarbonDioxideEmail.createEmail(sendEmail)
                PreviousTriggeredState = True
            
            if ((CO2Perc["SMOKE"])) <= 1000:
                PreviousTriggeredState = False
            
            if COPerc["CO"] > 70:
                if COPreviousTriggeredState == False:
                    message = COText.createClientMessage(sendText)
                    email = sendCarbonMonoxideEmail.createEmail(sendEmail)
                COPreviousTriggeredState = True
            
            if COPerc["CO"] <= 70:
                COPreviousTriggeredState = False    
except:
    e = sys.exc_info()[1]
    print("error: %s" % e)