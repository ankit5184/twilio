import requests
import time
import os
from twilio.rest import Client

# API URL to monitor
# api_url = 'https://reqres.in/api/'
api_url = 'https://reqres.in/api/users?page=2'

# Twilio credentials
twilio_account_sid = 'Your Twilio Account SID'
twilio_auth_token = 'Your Twilio Auth Token'
twilio_phone_number = 'Your Twilio Phone Number'
recipient_phone_number = 'Recipient Phone Number'

# Configuration file
config_file = 'configuration.txt'


# Function to make a Twilio call
def make_twilio_call():
    # client = Client(twilio_account_sid, twilio_auth_token)
    # call = client.calls.create(
    #     to=recipient_phone_number,
    #     from_=twilio_phone_number,
    #     url='http://demo.twilio.com/docs/voice.xml'  # Replace with your own TwiML URL
    # )
    # print(f"Twilio call initiated: {call.sid}")
    print("call made")


# Function to check for data from the API
def check_for_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        print(response.json())
        return True
    else:
        print(response.status_code)
        return False


# Function to store the current timestamp in the configuration file
def store_timestamp():
    current_time = int(time.time())
    with open(config_file, 'w') as file:
        file.write(str(current_time))


# Function to read the last timestamp from the configuration file
def read_last_timestamp():
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            return int(file.read())
    else:
        return 0


# Run the program
data_received = check_for_data()
last_timestamp = read_last_timestamp()
current_time = int(time.time())
elapsed_time = current_time - last_timestamp

# if not data_received:
#     if elapsed_time > 1800:  # 1800 seconds (30 minutes)
#         # 30 minutes have passed, make a call and store the timestamp
#         make_twilio_call()
#         store_timestamp()
#         print('Twilio call initiated as data was not received for 30 minutes.')
#     else:
#         print(f'Data has not been received for {elapsed_time} seconds.')
# else:
#     print('Data received.')
#     try:
#         os.remove(config_file)
#     except FileNotFoundError:
#         pass  # File does not exist, no need to remove it
#     make_twilio_call()

if not data_received and elapsed_time > 1800:  # Data not received and 30 minutes elapsed
    # 30 minutes have passed, make a call and store the timestamp
    make_twilio_call()
    store_timestamp()
    print(f'Twilio call initiated as data was not received for {elapsed_time} seconds.')
elif not data_received:
    print(f'Data has not been received for {elapsed_time} seconds.')
else:
    print('Data received.')
    try:
        os.remove(config_file)
    except FileNotFoundError:
        pass
    make_twilio_call()
