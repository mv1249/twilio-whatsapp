from helperfunction.waSendMessage import sendMessage
import os

import flask
from flask import send_from_directory, request


app = flask.Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')


@app.route('/')
@app.route('/home')
def home():
    return "Hello World"


@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp():

    print(request.get_data())
    message = request.form['Body']
    senderId = request.form['From'].split('+')[1]
    print(message)
    print(type(message))
    print(str(message))
    if message == "1":

        send_msg = "Please find our Products below.\r\nSolutions: Twilio Flex,Marketing Campaigns,TwilioFrontline\r\nServices:\r\nLookup,Verify,Authy,Twilio\r\nConversations,Studio,TaskRouter,Trust Hub,Event Streams\r\nChannel APIs:Programmable Messaging,Programmable Voice,Twilio SendGrid Email API,Programmable Video,WhatsApp Business API:\r\nSuper Network:Phone Numbers,Progammable Wireless,ShortCodes,Super SIM,Elastic SIP Trunking,Narrowband,Interconnect,Runtime,Sync\r\nYou can find more information here:\r\nhttps://www/twilio.com/products\" \r\n\r\nPlease reply 9 to go back to Main menu or # to end this chat"

        dummymsg = "Hello i am twilio"
        print(send_msg)
        res = sendMessage(senderId=senderId, message=send_msg)
        print(f'This is the response --> {res}')
        return '200'

    elif message == "2":

        send_msg = "Please request support assistance from \'Submit a Ticket\' page in Console and our Support Agent will get in touch with you shortly.\r\n\r\nPlease reply 9 to go back to Main menu or # to end this chat.\r\n\r\nThank you!"
        res = sendMessage(senderId=senderId, message=send_msg)
        print(f'This is the response --> {res}')
        return '200'

    elif message == "3":
        send_msg = "Please reach out to our sales team via our Help Page:\r\nhttps://www/twilio.com/help/sales and our Sales representative will get in touch with you shortly.\r\n\r\nPlease reply 9 to go back to Main menu or # to end this chat. Thank You!"
        res = sendMessage(senderId=senderId, message=send_msg)
        print(f'This is the response --> {res}')
        return '200'

    elif message == "9":
        send_message = "Hi User"+"\n\n" + \
            "Thanks for contacting Twilio and I'm glad that you are building with Twilio!"+"\n\n"
        main_msg = "Please reply\n"+".1 to get the List of Products that we offer." + "\n"+".2 for contacting the Support team." + \
            "\n"+".3 for contacting the Sales Team." + \
            "\n"+"# to end this chat."+"\n"+"Thank you!"

        send_msg = send_message+main_msg

        res = sendMessage(senderId=senderId, message=send_msg)
        print(f'This is the response --> {res}')
        return '200'

    elif message == '#':
        send_msg = "Thank you for using our live chat service!\r\n\r\nI am now closing this chat.If you have any more issues,feel free to reach out to me anytime.\r\n\r\nHave a great rest of your day!\r\n\r\n-Twilio EIC Bot\r\n"
        res = sendMessage(senderId=senderId, message=send_msg)
        print(f'This is the response --> {res}')
        return '200'

    else:

        send_message = "Hi User"+"\n\n" + \
            "Thanks for contacting Twilio and I'm glad that you are building with Twilio!"+"\n\n"
        main_msg = "Please reply\n"+".1 to get the List of Products that we offer." + "\n"+".2 for contacting the Support team." + \
            "\n"+".3 for contacting the Sales Team." + \
            "\n"+"# to end this chat."+"\n"+"Thank you!"

        send_msg = send_message+main_msg

        res = sendMessage(senderId=senderId, message=send_msg)
        print(f'This is the response --> {res}')
        return '200'


if __name__ == "__main__":
    app.run(port=5000, debug=True)
