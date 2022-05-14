import os
import dropbox
from dropbox.files import WriteMode
from numpy import intp

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                #local path
                local_path = os.path.join(root, fileName)
                
                #dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                #uploading the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
        access_token = 'sl.BHlhsasCc3TVpzdxlaQe8TmjyESuv-WYlgjEMETcqOuAAGso2iqd_9BFw3eN6G99MBq1BXxWnm5Sz8pdRFuwiRr1JrF2djPXvVoIST9IQcv6LPd0_uuSaj91d87yh3iPddEVLVc'
        transferData = TransferData(access_token)
        
        #to check if a number is even or odd
        #at the time of execution asking the path
        file_from = str(input("Enter folder path to transfer: "))
        file_to = str(input("Enter full path to upload to dropbox: "))

        transferData.upload_file(file_from, file_to)
        print("File has been transfered")

    
main()