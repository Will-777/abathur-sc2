import os
import sys
import json

import requests
from flask import Flask, request

# Let's go and make that in Python 3 ?!

app = Flask(__name__)


@app.route('/', methods=['GET'])

def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])

def webhook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text

                    send_message(sender_id, "got it, thanks!")

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


def abathur_menu(user_id):
    #key_word_menu = ""

    #if key_word_menu ==
    pass

def add_build():
    full_build = [build_id, race_vs_race, title_build, best_match_build_id, worst_match_build_id ]
    build_id = 0
    race_vs_race = "ZvP"
    race_vs_race_cat = ["ZvT","ZvP","ZvZ","TvT", "TvP","TvZ", "PvT","PvP","PvZ"]
    title_build = "Zergling, Banneling, Muta"
    best_match_build_id = [1,2,5,7]
    worst_match_build_id = [3, 6, 7, 10, 11]
    order_build = [[1,"0:02","drone"],[3,"0:10", "drone"],[6,"0:15", "drone"],[8,"0:15", "pool"]]

    # if title_build already exist
    print "This name already exists. Please change it."

    return ("The build %s has been correctly added to the database.") % (title_build)

# Should have a json file to fill in with build
db_all_sc2_builds.json = []


def list_build(arg1):
    if arg1 in race_vs_race_cat :
        for i in db_all_sc2_builds.json:
            print build_id + " - " + "title_build"
            #build_id += 1

        select_build = raw_input("which build would you like to display ?")
        print [db_all_sc2_builds.json][build_id]

    #if arg1 in title_build:
    #    print build where arg1 == [title_build]
    pass


def view_build(arg1):
    #if arg1 has a build_id:
    #    print build

    #if arg1 is char:
        #if arg1 in db_all_sc2_builds.json
        # print order_build

    #else:
    #    print("I didn't understand your command. Please try again.")

    pass




if __name__ == '__main__':
    app.run(debug=True)
