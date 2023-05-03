import config
import os
import datetime
import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass
        # self.USERNAME = os.environ.get("USER")
        # self.PROJECT_NAME = os.environ.get("PROJECT")
        # self.SHEETY_NAME = os.environ.get("SHEETY")
        # self.SHEET_PASSWORD = os.environ.get("Authorization")

    def read_google_sheet(self):
        sheet_endpoint = f'https://api.sheety.co/{config.USER}/{config.PROJECT}/{config.SHEETY}'

        bearer_headers = {
            'Authorization': f'Bearer {config.Authorization}',
        }

        sheet_response = requests.get(sheet_endpoint, headers=bearer_headers)

        return sheet_response.json()
