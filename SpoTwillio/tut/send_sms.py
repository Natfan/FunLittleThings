# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACe68ceccef6a94ded82ed6cd708de83c9"
auth_token = "a1fdc805a130849b705ecb7cad4371d0"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+447453787998",
                                             from_="+441728752053",
                                             body="Hello there!")
