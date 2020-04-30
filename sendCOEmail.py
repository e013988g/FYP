from mailjet_rest import Client
import os
import sys, time

class sendCOEmail():
    def createEmail(self, sendEmail):
        if sendEmail > 0:
            api_key = '2a7dd591bb2a78637787a36bc2d6474a'
            api_secret = '62cf4950c335e184afc4af7ee386f465'
            mailjet = Client(auth=(api_key, api_secret), version='v3.1')
            data = {
              'Messages': [
                {
                  "From": {
                    "Email": "e013988g@student.staffs.ac.uk",
                    "Name": "Luke"
                  },
                  "To": [
                    {
                      "Email": "lukeearp98@outlook.com",
                      "Name": "Luke"
                    }
                  ],
                  "Subject": "CO Warning!",
                  "TextPart": "CO levels have breached a safe level.",
                  "HTMLPart": "",
                  "CustomID": "sendnow"
                }
              ]
            }
            result = mailjet.send.create(data=data)
        else:
            result = []
        return result
