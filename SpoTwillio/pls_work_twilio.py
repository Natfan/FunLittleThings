from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_receive():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    message = request.values.get("Body", None)
    print(message)

    if "STOP" in message.upper():
        print("test1")
    if "SKIP" in message.upper():
        print("test2")
    if "BIEBER" in message.upper():
	# rickroll pls
        print("test3")

    # stop, skip etc

    resp.message("YOU HAVE BEEN HEARD!")

    return str(resp)

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=8889, debug=True)
