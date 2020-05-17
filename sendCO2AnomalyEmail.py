from mailjet_rest import Client
import os
import sys, time
from datetime import datetime

class sendCO2AnomalyEmail():
    def createEmail(self, sendEmail):
        if sendEmail > 0:
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            api_key = 'a2f01e3d78fe1648ec67a88cdbdc4be5'
            api_secret = 'da007df5625c3780cfec835fd320589d'
            mailjet = Client(auth=(api_key, api_secret), version='v3.1')
            data = {
              'Messages': [
                {
                  "From": {
                    "Email": "e013988g@gmail.com",
                    "Name": "Luke"
                  },
                  "To": [
                    {
                      "Email": "e013988g@gmail.com",
                      "Name": "Luke"
                    }
                  ],
                  "Subject": "CO2 level higher than usual!",
                  "TextPart": "Your carbon dioxide readings have increased within the last hour." + date_time,
                  "HTMLPart": ""
                }
              ]
            }
            result = mailjet.send.create(data=data)
        else:
            result = []
        return result

