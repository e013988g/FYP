from mailjet_rest import Client
import os
import sys, time
from datetime import datetime

now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
api_key = '01de10d12429fa1f80909ceb234c3da3'
api_secret = '20fcff66d6358ce7518e1307810a2167'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "lukeearp98@outlook.com",
        "Name": "Luke"
      },
      "To": [
        {
          "Email": "lukeearp98@outlook.com",
          "Name": "Luke"
        }
      ],
      "Subject": "CO Warning! " + date_time,
      "TextPart": "CO levels have breached a safe level. " + date_time,
      "HTMLPart": "",
      "CustomID": "sendnow"
    }
  ]
}
result = mailjet.send.create(data=data)