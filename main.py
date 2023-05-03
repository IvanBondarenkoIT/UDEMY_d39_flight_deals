#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch


def main():
    # dm = DataManager()
    # sheet_data = dm.read_google_sheet()
    # print(sheet_data)
    # have_new_prices = {}
    # if have_new_prices:
    #     dm.write_google_sheet(flight_data=sheet_data,
    #                           new_prices=have_new_prices)
    sheet_data = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
                {'city': 'Berlin', 'iataCode': 'LCY', 'lowestPrice': 42, 'id': 3},
                {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
                {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
                {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
                {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
                {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
                {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
                {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}
    print(sheet_data)
    for row in sheet_data['prices']:
        if row['iataCode'] == '':
            # print(row['city'])
            row['iataCode'] = FlightSearch().get_iata_code(row['city'])
    print(sheet_data)


if __name__ == '__main__':
    main()
