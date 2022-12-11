from __future__ import print_function
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from settings import *

import google.auth
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


def add( service_table, values, range = None):
    range = 'Лист1!A1'
    SPREADSHEET_ID = ID_TABLE
    body = {'values': [values]}
    result = service_table.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID, range=range,
        valueInputOption='USER_ENTERED', body=body).execute()


def upload_to_folder(folder_id, file_for_load, data):
    SCOPES = ['https://www.googleapis.com/auth/drive'+'https://www.googleapis.com/auth/spreadsheets']
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print('flow')
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try:
        # create drive api client
        service_drive = build('drive', 'v3', credentials=creds)
        service_table = build('sheets', 'v4', credentials=creds)
        file_metadata = {
            'name': f'{data[-1]}',
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_for_load, mimetype='video/mp4', resumable=True)
        file = service_drive.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()


        # запись в таблицу
        file_id_drive = file.get('id')
        data[-1] = f'=ГИПЕРССЫЛКА("https://drive.google.com/file/d/{file_id_drive}/view?usp=sharing"; "{data[-1]}")'
        add(service_table=service_table, values=data)

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None


    return file.get('id')

