from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import discovery
from googleapiclient import http
from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload
import io

def text_upload(file_name,creds,folder_id):
    service = build('drive', 'v3', credentials=creds)
    file_name=file_name+'.txt'
    file_metadata = {'name': file_name,'parents' : [folder_id]}
    media = MediaFileUpload(file_name,
                                mimetype='text/csv')
    file = service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
    file_id=file.get('id')
    f=open("file_id.csv","a+")
    f.write(file_name+','+file_id+'\n')