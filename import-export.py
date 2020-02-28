import sys
import os

def create_empty_db():
    try:
        INSTANCE_NAME = raw_input("Enter Sql Instance Name : ")
        user_choice = raw_input("1.Connect with Default root User\n2.Connect with Specific user\n3.Enter your Choice")
        if user_choice == '1':
            print("configure the default user")
            pwd_cmd = 'gcloud sql users set-password root --host=% --instance={0} --prompt-for-password'.format(INSTANCE_NAME)
            os.system(pwd_cmd)
            cmd = 'gcloud sql connect {0} --user=root'.format(INSTANCE_NAME)
        elif user_choice == '1':
            USER = raw_input("Enter User Name:")
            cmd = 'gcloud sql connect {0} --user={1}'.format(INSTANCE_NAME, USER)
        else:
            print("Invalid Choice!")
        os.system(cmd)

        DATABASE_NAME = raw_input("Enter Database Name to Create : ")
        db_create_cmd = 'CREATE DATABASE {0};'.format(DATABASE_NAME)
    except Exception as e:
        print(str(e))
        print("Exception in creating Empty Database")


def import_from_bucket():
    try:
        SERVICE_ACCOUNT_ADDRESS = raw_input("Enter Service Account :  ")  
        BUCKET_NAME = raw_input("Enter Bucket Name :  ")
        INSTANCE_NAME = raw_input("Enter Instance Name : ")
        sqldumpfileName = raw_input("Enter Object Name :  ")
        DATABASE_NAME = raw_input("Enter Database Name :  ")
        Extention = raw_input("Enter Object Extention :  ")
        
        acl_cmd = 'gsutil acl ch -u {0}:R gs://{1}/{2}.{3}'.format(SERVICE_ACCOUNT_ADDRESS, BUCKET_NAME, sqldumpfileName, Extention)
        print("Adding READ Permission")
        os.system(acl_cmd)

        import_cmd = 'gcloud sql import sql {0} gs://{1}/{2}.{3} --database={4}'.format(INSTANCE_NAME, BUCKET_NAME, sqldumpfileName, Extention, DATABASE_NAME)
        print("Importing Data ...")
        os.system(import_cmd)
    except Exception as e:
        print(str(e))
        print("Exception in Importing Database")



def export_db_to_bucket():
    try:
        SERVICE_ACCOUNT_ADDRESS = raw_input("Enter Service Account :  ")  
        BUCKET_NAME = raw_input("Enter Bucket Name :  ")
        INSTANCE_NAME = raw_input("Enter Instance Name : ")
        sqldumpfileName = raw_input("Enter Object Name :  ")
        DATABASE_NAME = raw_input("Enter Database Name :  ")
        Extention = raw_input("Enter Object Extention :  ")
        
        acl_cmd = 'gsutil acl ch -u {0}:W gs://{1}'.format(SERVICE_ACCOUNT_ADDRESS, BUCKET_NAME)
        print("Adding WRITE Permission")
        os.system(acl_cmd)

        export_cmd = 'gcloud sql export sql {0} gs://{1}/{2}.{3} --database={4}'.format(INSTANCE_NAME, BUCKET_NAME, sqldumpfileName, Extention, DATABASE_NAME)
        print("Importing Data ...")
        os.system(export_cmd)
    except Exception as e:
        print(str(e))
        print("Exception in Exporting Database")

choice = raw_input("1. Create Empty Database \n2. Import Data from Storage Bucket\n3. Export Data to Storage Bucket\nEnter your choice:  ")

if choice == '1':
    create_empty_db()
elif choice == '2':
    import_from_bucket()
elif choice == '3':
    export_db_to_bucket()
else:
    print("Invalid Choice")
