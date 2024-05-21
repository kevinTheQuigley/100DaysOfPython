from twilio.rest import Client
from arsewards import arsewards_dict


class NotificationManager:
    def __init__(self) -> None:
            self.client = Client(arsewards_dict["twilio_account_sid"],arsewards_dict["twilio_auth_token"])
            self.messages = []
    #This class is responsible for sending notifications with the deal flight details.

    def take_message(self,message):
        self.messages.append(message)

    def produce_message(self):
        text = "Congratulations, we have a hit!\n"
        for message in self.messages:
            text +=message
        self.theMessage  = text

    def send_message(self):
        message = self.client.messages.create(
            from_='+12177658194',
            to=arsewards_dict["the_number"],
            body= self.theMessage
            )