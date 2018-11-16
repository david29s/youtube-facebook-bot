import json
import requests

from flask import Flask, request

from pymessenger.bot import Bot

from main_api import youtube_search

app = Flask(__name__)
ACCESS_TOKEN = 'EAAKqyQDZBZBPIBAOn1ODbcyFqaCNtGRTp1sxF17R9R39pVsOJeE11reJhPHykPSNv5NhZAfpCxRCopsxwWvawBPYi51h1kxuf72aoxEOyTaPU9KeEVREGD0FC0Ru5CRWZCcEWF2jUG2rZAN0qaZBMJaq2JuXEalf6lvTeyt35ql1R084ZBVGn38'
VERIFY_TOKEN = 'verysecrettoken'
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']

          for message in messaging:
            recipient_id = message['sender']['id']
            header = {'Content-Type': 'application/json'}
            if message.get('postback'):
                if message['postback'].get('payload') == 'GET_STARTED_PAYLOAD':
                    names = requests.get(
                        'https://graph.facebook.com/{}?fields=first_name,last_name&access_token={}'.format(
                            message['sender']['id'], ACCESS_TOKEN)).json()

                    print(names)

                    send_message(recipient_id, 'Greetings, {} {}'.format(
                        names['first_name'],
                        names['last_name']
                    ))
            if message.get('message'):
                if message['message'].get('text'):
                    print(message['message'].get('text'))
                    send_message(recipient_id, message['message'].get('text'))
    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def send_message(recipient_id, response):
    print(recipient_id)
    header = {

        'Content-Type': 'application/json'
    }



    body = {
        'messaging_type': 'RESPONSE',
        'recipient': {
            'id': recipient_id
        },
        'message':{
            'text': response
        }
    }

    res = youtube_search(response)
    carousel = \
        {
             "recipient":
                 {
               "id": recipient_id
                },
             "message":
                {
               "attachment":
                   {
                 "type":"template",
                 "payload":
                     {
                   "template_type": "generic",
                   "elements": res
                     }
                    }
                }
        }

    r = requests.post('https://graph.facebook.com/v2.6/me/messages?access_token={}'.format(ACCESS_TOKEN), data=json.dumps(carousel), headers=header)
    print(r.status_code, r.text)


if __name__ == "__main__":
    app.run(port='6900')
