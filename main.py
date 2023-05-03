#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager


def main():
    dm = DataManager()
    print(dm.read_google_sheet())


if __name__ == '__main__':
    main()
