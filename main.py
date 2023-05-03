#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager


def main():
    dm = DataManager()
    flight_data = dm.read_google_sheet()
    print(flight_data)
    have_new_prices = {}
    if have_new_prices:
        dm.write_google_sheet(flight_data=flight_data,
                              new_prices=have_new_prices)


if __name__ == '__main__':
    main()
