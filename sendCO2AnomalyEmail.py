from mailjet_rest import Client
import os
import sys, time
from datetime import datetime

class sendCO2AnomalyEmail():
    def createEmail(self, sendEmail):
        if sendEmail > 0:
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            api_key = 'ce9426e7bb33fe2fc0ebf344f67d7a38'
            api_secret = 'e860031699212a48d2b2d2972b3a56b8'
            mailjet = Client(auth=(api_key, api_secret), version='v3.1')
            data = {
              'Messages': [
                {
                  "From": {
                    "Email": "lukeearpp98@outlook.com",
                    "Name": "Luke"
                  },
                  "To": [
                    {
                      "Email": "lukeearp98@outlook.com",
                      "Name": "Luke"
                    }
                  ],
                  "Subject": "CO2 level higher than usual!",
                  "TextPart": "Your carbon dioxide readings are higher than this time last week." + date_time,
                  "HTMLPart": ""
                }
              ]
            }
            result = mailjet.send.create(data=data)
        else:
            result = []
        return result

