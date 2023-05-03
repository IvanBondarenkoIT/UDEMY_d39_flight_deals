import config
import os
import datetime
import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass
        # safety must be reset
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

    def write_google_sheet(self, flight_data: dict = {}, new_prices: dict = {}):
        bearer_headers = {
            'Authorization': f'Bearer {config.Authorization}',
        }

        for item in flight_data["prices"]:
            object_id = item.get('id')
            have_new_price = new_prices.get(item["iataCode"])

            sheet_endpoint = f'https://api.sheety.co/{config.USER}/{config.PROJECT}/{config.SHEETY}/{object_id}'
            sheet_inputs = {
                "price":
                    {
                     'city': item["city"].title(),
                     'iataCode': item["iataCode"],
                     'lowestPrice': have_new_price if have_new_price else item["lowestPrice"],
                     'id': 2
                    }
                }
            sheet_response = requests.put(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
            print(sheet_response.text)

