from findCO2Anomaly import *
import threading

linearRegression = CO2LinearRegression();
    
x = threading.Thread(target=linearRegression.checkForAnomaly args=(3500.45))
x.start()
