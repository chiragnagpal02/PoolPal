#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

from invokes import invoke_http

import json
import os

import amqp_setup

monitorBindingKey = '*.user'


def receiveuserLog():
    amqp_setup.check_setup()

    queue_name = 'User'

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    # an implicit loop waiting to receive messages;
    amqp_setup.channel.start_consuming()
    # it doesn't exit by default. Use Ctrl+C in the command window to terminate it.


# required signature for the callback; no return
def callback(channel, method, properties, body):
    print("\nReceived an user log by " + __file__)
    processUserLog(json.loads(body))
    print()  # print a new line feed


def processUserLog(user):
    print("Recording an user log:")
    print(user)
    print(user['PPhone'])
    user_URL = "http://localhost:5001/api/v1/passenger/add_new_passenger"
    data = {
        "user_item": [{
            "PName": user["PName"],
            "PUserName": user["PUserName"],
            "PAge": user["PAge"],
            "PGender": user["PGender"],
            "PEmail": user["PEmail"],
            "PPassword": user["PPassword"],
            "PAddress": user["PAddress"],
            "PPhone": user["PPhone"]
        }]
    }
    dictionary_data = data['user_item'][0]
    json_data = json.dumps(dictionary_data)
    print(json_data)
    review_data = json.loads(json_data)
    print(review_data)

    user_result = invoke_http(user_URL, method='POST', json=review_data)
    print('user_result:', user_result)


# execute this program only if it is run as a script (not by 'import')
if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    receiveuserLog()
