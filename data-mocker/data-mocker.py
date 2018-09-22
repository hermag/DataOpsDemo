import os
import time
import pandas as pd
import numpy as np
import datetime

def mock_the_data():
    datetime_now = datetime.datetime.now().replace(microsecond=0)
    datetime_shifted = datetime_now+datetime.timedelta(seconds=30)
    days = pd.date_range(datetime_now,datetime_shifted,freq='S')
    np.random.seed(seed=1111)
    temperatures = np.random.randint(1, high=50, size=len(days))
    humidity = np.random.randint(1, high=100, size=len(days))
    df = pd.DataFrame({'timestamp': days, 'temperature': temperatures, 'humidity':humidity})
    df = df.set_index('timestamp')
    return df

if __name__=="__main__":
    #output_location = os.getcwd()
    #output_location = os.path.dirname(os.path.abspath( __file__ ))
    output_location=""
    while True:
        output_file_name = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%dT%H_%M_%S.csv")
        #output_file = "%s/data/new/%s"%(output_location,output_file_name)
        output_file = "/data/new/%s"%(output_file_name)
        df = mock_the_data()
        df.to_csv(output_file)
        time.sleep(30)
