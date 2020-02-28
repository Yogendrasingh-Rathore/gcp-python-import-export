import sys
import os

def cleanup_bucket():
    try:
        BUCKET_NAME = raw_input("Enter Bucket Name : ")
        choice = raw_input("1.Remove an empty bucket\n 2.Remove bucket with objects \n 3.Remove a Specific Object from Specific Bucket \n Please Choose your Choice :\t")

        if choice == '1': 
            cmd = 'gsutil rb gs://{0}'.format(BUCKET_NAME)
        elif choice == '2':
            print("Warning: The following command also deletes all objects stored within the bucket. These objects cannot be recovered")
            cmd = 'gsutil rm -r gs://{0}'.format(BUCKET_NAME)
        elif choice == '3':
            OBJECT_NAME = raw_input("Enter the Name of Object : ")
            cmd = 'gsutil rm gs://{0}/{1}'.format(BUCKET_NAME, OBJECT_NAME)
        else:
            print("Invalid Choice")
        os.system(cmd)
    except Exception as e:
        print(str(e))
        print("Exception in deleting Bucket")


def cleanup_sql_instance():
    try:
        INSTANCE_NAME = raw_input("Enter Sql Instance Name : ")
        print("Warning: All data on an instance, including backups, is permanently lost when that instance is deleted. \nTo preserve your data, export it to Cloud Storage before you delete it.") 
        cmd = 'gcloud sql instances delete {0}'.format(INSTANCE_NAME)
        os.system(cmd)
    except Exception as e:
        print(str(e))
        print("Exception in deleting Bucket, Note the Following Points : ")
        print("You cannot delete an instance that has any replicas. You must delete all replicas first.")
        print("After you delete an instance, it might continue to appear in your project with an unknown size but with a Being deleted status. This is normal and the instance should disappear completely after a brief period of time.")
        print("You cannot reuse an instance name for up to a week after you have deleted an instance.")


cleanup_choice = raw_input("1. Cleanup Bucket \n2. Cleanup SQL Instance\nEnter your choice:  ")

if cleanup_choice == '1':
    cleanup_bucket()
elif cleanup_choice == '2':
    cleanup_sql_instance()
else:
    print("Invalid Choice")
