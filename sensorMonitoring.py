from mqCO2 import *
from mqCO import *
from sendCO2Text import *
from sendCO2AnomalyText import *
from sendCO2Email import *
from sendCO2AnomalyEmail import *
from sendCOEmail import *
from sendCOAnomalyEmail import *
from sendCOText import *
from sendCOAnomalyText import *
from sendDataToDB import *
from getNotificationSettings import *
import sys, time, json
from findCO2Anomaly import *
from findCOAnomaly import *
import threading

anomalyCheckCount = 4
upperCO2Forecast = 0
CO2Forecast = 0
upperCOForecast = 0
COForecast = 0
def findAnomalies(CO2Reading, COReading):
    global anomalyCheckCount
    global upperCO2Forecast
    global CO2Forecast
    global upperCOForecast
    global COForecast
    
    if anomalyCheckCount == 4:
        CO2AnomFound = False
        COAnomFound = False
        notifs = getNotifications();
        notifSettings = json.loads(notifs.getSettings())
        sendText = notifSettings[0]["sendText"]
        sendEmail = notifSettings[0]["sendEmail"]
        CO2AnomText = sendCO2AnomalyText()
        COAnomText = sendCOAnomalyText()
        CO2AnomEmail = sendCO2AnomalyEmail()
        COAnomEmail = sendCOAnomalyEmail()
        
        findCO2Anomaly = CO2LinearRegression();
        CO2AnomFound, CO2Forecast, upperCO2Forecast = findCO2Anomaly.checkForAnomaly(CO2Reading);

        findCOAnomaly = COLinearRegression();
        COAnomFound, COForecast, upperCOForecast = findCOAnomaly.checkForAnomaly(COReading);
        
        if CO2AnomFound == True:
            CO2AnomText.createClientMessage(sendText)
            CO2AnomEmail.createEmail(sendEmail)
            
        if COAnomFound == True:
            COAnomText.createClientMessage(sendText)
            COAnomEmail.createEmail(sendEmail)
        anomalyCheckCount = 1
        
    anomalyCheckCount = anomalyCheckCount + 1
    
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
            anomalyThread = threading.Thread(target=findAnomalies, args=(CO2Perc["SMOKE"], COPerc["CO"],))
            anomalyThread.start()
            sys.stdout.write("\r")
            sys.stdout.write("\033[K")
            sys.stdout.write("[CO2: %g ppm, Forecasted Reading: %g, Upper Forecast: %g], [CO: %g ppm, Forecasted Reading: %g, Upper Forecast: %g]" % ((CO2Perc["SMOKE"]), CO2Forecast, upperCO2Forecast, (COPerc["CO"]), COForecast, upperCOForecast))
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