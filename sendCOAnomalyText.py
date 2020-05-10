from twilio.rest import Client
import sys, time

class sendCOAnomalyText():
    
    def createClientMessage(self, sendText):
        if sendText > 0:
            ACCOUNT_SID = 'ACd1cd65da15d96c2208c441a1f4dd7fa0'
            AUTH_TOKEN = '35c51c29ccd1475af7bc6a4abaacf127'   
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            message = client.messages.create(body='Your carbon monoxide readings are higher than this time last week.', from_='+441873740096', to='+447746103651')
        else:
            message = ""
            
        return message


