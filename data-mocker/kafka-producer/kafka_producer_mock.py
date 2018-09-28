#!/usr/bin/python
import os
import glob
import time
import shutil
import pandas
from kafka import KafkaProducer
from kafka.errors import KafkaError

def get_data_frame_column_names(df):
    column_names_list=[]
    for i in range(len(df.columns)):
        column_names_list.append(str(df.columns[i]))
    return column_names_list    



raw_files_list=[]

producer = KafkaProducer(bootstrap_servers='16.168.0.3,9092')

csv_raw_files_location="/nvme/CodeArea/DataOpsDemo/data-mocker/data/new"
csv_processed_files_location="/nvme/CodeArea/DataOpsDemo/data-mocker/data/processed"

while True:
    raw_files_list=glob.glob("%s/*csv"%csv_raw_files_location)
    if len(raw_files_list)>0:
        for raw_file in raw_files_list:
            csv_data=pandas.read_csv(raw_file)
            column_names_list=get_data_frame_column_names(csv_data)
            for index, row in csv_data.iterrows():
                for column_name in column_names_list:
                    print(column_name,row[column_name])
                    message="%s:%s"%(str(column_name),str(row[column_name]))
                    future = producer.send('test', str.encode(message))
                    record_metadata = future.get(timeout=1)
                    time.sleep(1)
            shutil.move(raw_file, "%s/%s"%(csv_processed_files_location,os.path.basename(raw_file)))        
    else:
        continue



# Asynchronous by default
#for i in range(1000):
#    future = producer.send('test', b'RAW DATA %d'%i)
#    # Block for 'synchronous' sends
#    record_metadata = future.get(timeout=1)
#    # Successful result returns assigned partition and offset
#    print (record_metadata.topic)
#    print (record_metadata.partition)
#    print (record_metadata.offset)
#    time.sleep(2)
#
