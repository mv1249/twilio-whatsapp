import os

from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()

ACCOUNT_SID = ""
AUTH_TOKEN = ""
FROM = ""

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def sendMessage(senderId, message):

    res = client.messages.create(
        body=message,
        from_=FROM,
        to=f'whatsapp:+{senderId}'
    )
    return res
