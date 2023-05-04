import config
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.TEQUILA_KIWI_API = config.TEQUILA_KIWI_API
        self.TEQUILA_SERVER = config.TEQUILA_SERVER

    def get_iata_code(self, city_name: str):
        tequila_endpoint = f'{self.TEQUILA_SERVER}/locations/query'
        tequila_header = {'apikey': self.TEQUILA_KIWI_API}

        tequila_query = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=tequila_endpoint,
                                headers=tequila_header,
                                params=tequila_query)
        print(response.json())

        results = response.json()["locations"]
        code = results[0]["code"]
        return code
