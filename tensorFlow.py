from findCO2Anomaly import *
import threading

linearRegression = CO2LinearRegression();
    
x = threading.Thread(target=linearRegression.checkForAnomaly(3500.45))
x.start()
