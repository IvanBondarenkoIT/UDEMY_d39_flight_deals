from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData


def main():
    """This file will need to use the DataManager,FlightSearch,
     FlightData, NotificationManager classes to achieve the program requirements."""
    dm = DataManager()
    sheet_data = dm.read_google_sheet()
    print(sheet_data)

    sheet_data = {'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'LCY', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}, {'city': 'Batumi', 'iataCode': 'BUS', 'lowestPrice': 500, 'id': 11}]}

    have_new_prices = False

    print(sheet_data)
    for row in sheet_data['prices']:
        fs = FlightSearch()
        if row['iataCode'] == '':
            row['iataCode'] = fs.get_iata_code(row['city'])
            print(row['iataCode'])

        flight_data = fs.searching_for_flight(row['iataCode'])
        if row['lowestPrice'] > flight_data.price:
            have_new_prices = True
            row['lowestPrice'] = flight_data.price
            pass
            # send_sms
    print(f'RESULT:\n{sheet_data}')

    if have_new_prices:
        dm.write_google_sheet(flight_data=sheet_data)


if __name__ == '__main__':
    main()
