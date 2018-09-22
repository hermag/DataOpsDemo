import time
import pandas as pd
import numpy as np
import datetime

def data_generation():
    #time.sleep(10)
    datetime_now = datetime.datetime.now()
    print(datetime_now)
    datetime_shifted = datetime.datetime.now()+datetime.timedelta(seconds=300)
    print(datetime_shifted)
    days = pd.date_range(datetime_now, datetime_shifted, freq='sec')
    print(days)
    np.random.seed(seed=1111)
    temperatures = np.random.randint(1, high=100, size=len(days))
    humidity = np.random.randint(1, high=100, size=len(days))
    df = pd.DataFrame({'timestamp':days, 'temperature':temperatures, 'humidity':humidity})
    df = df.set_index('timestamp')
    print(df)
    return 0
 
if __name__ == "__main__":
    while True:
        data_generation()

