from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import os
from dotenv import load_dotenv




load_dotenv() 


ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
RECIPIENT_NUMBER = os.getenv("RECIPIENT_NUMBER")

if not all([ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER, RECIPIENT_NUMBER]):
    print("ERROR: One or more required environment variables are missing.")
    print("Please ensure TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER, and RECIPIENT_NUMBER are set in your .env file.")
    exit()


def create_twiml_message():

    response = VoiceResponse()

    response.say(
        'Hello. This is an automated phone call from a custom dialer system. Please listen carefully.',
        voice='man',
        language='en-US'
    )


    response.pause(length=1)

    response.say(
        'Thank you for taking this call. Goodbye.',
        voice='man',
        language='en-US'
    )
    

    return str(response)



if __name__ == "__main__":
    

    TwiML_INSTRUCTIONS = create_twiml_message()
    
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        
        call = client.calls.create(
            to=RECIPIENT_NUMBER,
            from_=TWILIO_NUMBER,
            twiml=TwiML_INSTRUCTIONS  
        )

        print("--------------------------------------------------")
        print(f"Call initiated successfully!")
        print(f"Call SID: {call.sid}")
        print("--------------------------------------------------")

    except Exception as e:

        print("--------------------------------------------------")
        print(f"An error occurred while initiating the call:")
        print(e)
        print("--------------------------------------------------")