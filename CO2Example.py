from mqCO2 import *
from mqCO import *
from sendCO2Text import *
from sendCO2Email import *
from sendCOText import *
import sys, time

try:
    CO2Trigerred = False
    PreviousTriggeredState = False
    COPreviousTriggeredState = False
    mqCO2 = MQCO2();
    mqCO = MQCO();
    CO2Text = sendCO2Text();
    COText = sendCOText();
    sendCarbonDioxideEmail = sendCO2Email();
    while True:
            CO2Perc = mqCO2.MQPercentage()
            COPerc = mqCO.MQPercentage()                    
            sys.stdout.write("\r")
            sys.stdout.write("\033[K")
            sys.stdout.write("CO2: %g ppm, CO: %g ppm" % ((CO2Perc["SMOKE"] * 20000), (COPerc["CO"])))
            sys.stdout.flush()
            time.sleep(0.1)
            if ((CO2Perc["SMOKE"]) * 20000) > 1000:
                if previousTriggeredState == False:
                    message = CO2Text.createClientMessage()
                    email = sendCarbonDioxideEmail.createEmail()
                previousTriggeredState = True
            
            if ((CO2Perc["SMOKE"]) * 20000) <= 1000:
                previousTriggeredState = False
            
            if COPerc > 70:
                if COPreviousTriggeredState == False:
                    message = COText.createClientMessage()
                    previousTriggeredState = True
            
            if COPerc <= 70:
                previousTriggeredState = False    
except:
    e = sys.exc_info()[0]
    print("error: %s" % e)