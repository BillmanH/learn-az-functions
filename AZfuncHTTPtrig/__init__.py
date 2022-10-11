# Defaults
import logging
import azure.functions as func

# Needed for this app
from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import DefaultAzureCredential
import os


def get_credential():
    # you will get this from the ADT resource at portal.azure.com
    credential = DefaultAzureCredential()
    serviceClient = DigitalTwinsClient(os.getenv("AZURE_ADT_URL"), credential)
    return serviceClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    client = get_credential()

    logging.info('Python HTTP trigger function processed a request.')

    deviceID = req.params.get('name')
    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
