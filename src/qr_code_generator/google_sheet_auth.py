import sys
project_root = "C:\\Users\\casag\\Qrcode_generator"
sys.path.insert(0, project_root)
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource
from src.interfaces.google_sheet_auth import GoogleSheetAuthInterface


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

class GoogleSheetAuth(GoogleSheetAuthInterface): 
    def __init__(self):
        # Define um metodo construtor que sempre que classe for chamada já executa o metodo get_service() que por sua vez retora o _get_setvice, privado.
        self.service = self._get_service()
        #"teste"

    def _get_service(self):
        creds = None

        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "C:\\Users\\casag\\Qrcode_generator\\src\\qr_code_generator\\client_secret.json", SCOPES
                )
                
                
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        return build("sheets", "v4", credentials=creds)

    def get_service(self) -> Resource:
        return self.service

# if __name__ ==  "__main__":
#     auth = GoogleSheetAuth()
#     auth.get_service()