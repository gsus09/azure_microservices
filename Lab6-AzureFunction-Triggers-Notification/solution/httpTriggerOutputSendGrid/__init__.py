import logging
import azure.functions as func
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import json

def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

    value = "Sent from Azure Functions"

    message = {
        "personalizations": [ {
          "to": [{
            "email": "gsus09@web.de"
            }],
          "from": [{
            "email": "gsus09@googlemail.com"
            }]
        }],
        "subject": "[AZURE] Azure Functions email with SendGrid",
        "content": [{
            "type": "text/plain",
            "value": value }]}

    sendGridMessage.set(json.dumps(message))
    print("SENT............")
    return func.HttpResponse(json.dumps(message), mimetype="application/json", status_code=200)
