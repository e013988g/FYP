from tensor import *
from threading import *

linearRegression = CO2LinearRegression();
def runThread(): 
    print(linearRegression.checkForAnomaly(3500.45))
    
x = threading.Thread(target=runThread, args=(1,))
x.start()
