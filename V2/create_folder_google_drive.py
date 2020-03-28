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

def create_folder(creds):
    service = build('drive', 'v3', credentials=creds)    
    file_metadata = {
    'name': 'Results_text',
    'mimeType': 'application/vnd.google-apps.folder'
        }
    file = service.files().create(body=file_metadata,fields='id').execute()
    return file.get('id')