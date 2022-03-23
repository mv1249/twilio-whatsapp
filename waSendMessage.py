import os

from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()

ACCOUNT_SID = "ACd32b923452389686a101281f89886fda"
AUTH_TOKEN = "31a0beedf0125d40796703a870c1383c"
FROM = "whatsapp:+14155238886"

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def sendMessage(senderId, message):

    res = client.messages.create(
        body=message,
        from_=FROM,
        to=f'whatsapp:+{senderId}'
    )
    return res
