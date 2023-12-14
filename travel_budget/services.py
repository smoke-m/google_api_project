import json
import os

from aiogoogle.auth.creds import ServiceAccountCreds
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient import discovery

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

load_dotenv()

CREDENTIALS_FILE = os.environ['CREDENTIALS_FILE']
EMAIL_USER = os.environ['EMAIL']

CREDENTIALS = Credentials.from_service_account_file(
    filename=CREDENTIALS_FILE, scopes=SCOPES
    )
SHEETS_SERVICE = discovery.build('sheets', 'v4', credentials=CREDENTIALS)
DRIVE_SERVICE = discovery.build('drive', 'v3', credentials=CREDENTIALS)

# тест импорта
cred = ServiceAccountCreds(
    scopes=SCOPES, **json.load(open(CREDENTIALS_FILE))
)


# def auth_sheets():
#     credentials = Credentials.from_service_account_file(
#         filename=CREDENTIALS_FILE, scopes=SCOPES
#     )
#     service = discovery.build('sheets', 'v4', credentials=credentials)
#     return service, credentials


# def auth_drive():
#     credentials = Credentials.from_service_account_file(
#         filename=CREDENTIALS_FILE, scopes=SCOPES
#     )
#     service = discovery.build('drive', 'v3', credentials=credentials)
#     return service, credentials
