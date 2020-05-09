from findCO2Anomaly import *
import threading

def runThread():
    linearRegression = CO2LinearRegression();
    print(linearRegression.checkForAnomaly(3500.45))
    
x = threading.Thread(target=runThread)
x.start()
