import sys
import os
#import time
#from random import randint
#from google.cloud import storage

def create_sqlInstance():
  try:
    INSTANCE_NAME = raw_input("Enter Sql Instance Name : ")
    MACHINE_TYPE = raw_input("Enter Machine Type : ")
    REGION = raw_input("Enter Region : ")
    #STORAGE_SIZE = input("Enter Storage Size : ")
    create_cmd = 'gcloud sql instances create {0} --tier={1} --region={2}'.format(INSTANCE_NAME, MACHINE_TYPE, REGION) #--storage-size=STORAGE_SIZE
    os.system(create_cmd)
  except Exception as e:
    print(str(e))
    print("Exception in creating SQL INSTANCE")


def create_cloudStorage():
  try:
      BUCKET_NAME = raw_input("Enter Bucket Name : ")
      BUCKET_LOCATION = raw_input("Enter Bucket Location : ")
      STORAGE_CLASS = raw_input("Enter Storage Class : ")
      #PROJECT_NAME = input("Enter Project Name : ")
      bucket_create_cmd = 'gsutil mb -c {0} -l {1} gs://{2}'.format(STORAGE_CLASS, BUCKET_LOCATION, BUCKET_NAME)
      os.system(bucket_create_cmd)
  except Exception as e:
    print(str(e))
    print("Exception in creating CLOUD STORAGE BUCKET")

create_choice = raw_input("1. Create SQL INSTANCE \n2. Create Storage Bucket\nEnter your choice:  ")

if create_choice == '1':
    create_sqlInstance()
elif create_choice == '2':
    create_cloudStorage()
else:
    print("Invalid Choice")

