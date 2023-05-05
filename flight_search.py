import config
import requests
import datetime
from flight_data import FlightData


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self):
        self.TEQUILA_KIWI_API_TOKEN = config.TEQUILA_KIWI_API_TOKEN
        self.TEQUILA_SERVER = config.TEQUILA_SERVER
        self.API_CALL_QUERY = config.API_CALL_QUERY
        self.API_CALL_SEARCH = config.API_CALL_SEARCH

    def get_iata_code(self, city_name: str):
        tequila_endpoint = f'{self.TEQUILA_SERVER}/{self.API_CALL_QUERY}'
        tequila_header = {'apikey': self.TEQUILA_KIWI_API_TOKEN}

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

    def searching_for_flight(self, destination_city_code: str):
        tequila_endpoint = f'{self.TEQUILA_SERVER}/{self.API_CALL_SEARCH}'

        tequila_header = {
            'apikey': self.TEQUILA_KIWI_API_TOKEN
        }

        date_tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        date_half_year_future = datetime.datetime.now() + datetime.timedelta(days=6 * 30)

        tequila_query = {
            "fly_from": config.HOME_CODE,
            "fly_to": destination_city_code,
            "dateFrom": date_tomorrow.strftime("%d/%m/%Y"),
            "dateTo": date_half_year_future.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }



        response = requests.get(url=tequila_endpoint,
                                headers=tequila_header,
                                params=tequila_query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
        #
        # results = response.json()["locations"]
        # code = results[0]["code"]

        # {price: '', departure_airport_code: '', departure_city: ''}