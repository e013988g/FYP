from findCO2Anomaly import *
from threading import *

def runThread():
    linearRegression = CO2LinearRegression();
    print(linearRegression.checkForAnomaly(3500.45))
    
x = threading.Thread(target=runThread, args=(1,))
x.start()
