from twilio.rest import Client
import config


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, list_of_flights):
        self.list_of_flights = list_of_flights

    def get_sms_text(self):
        sms_message = ''
        for flight in self.list_of_flights:
            sms_message += f"{flight.price}$\n" \
                           f"{flight.origin_city}\n" \
                           f"{flight.origin_airport}\n" \
                           f"{flight.destination_city}\n" \
                           f"{flight.destination_airport}\n" \
                           f"{flight.out_date}\n" \
                           f"{flight.return_date}\n"
        return sms_message

    def send_sms(self):
        sms_text = self.get_sms_text()
        to_number = config.my_actual_phone_number
        account_sid = config.account_sid
        auth_token = config.auth_token
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"{sms_text}",
            from_=f"{config.my_twilio_phone_number}",
            to=f"{to_number}"
        )

        return f"Sms sended successfully:\n{sms_text}\n{to_number}\n{message.sid}"
