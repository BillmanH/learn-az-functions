# https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/digitaltwins/azure-digitaltwins-core/samples/notebooks

# Defaults
from asyncio.log import logger
import logging
import azure.functions as func

# Needed for this app
from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import DefaultAzureCredential
import os


def get_credential(url):
    # you will get this from the ADT resource at portal.azure.com
    credential = DefaultAzureCredential()
    serviceClient = DigitalTwinsClient(url, credential)
    return serviceClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    # To reference a different URL, change the `AZURE_ADT_URL` in the enviornment variables
    # Note, must contain `https://`
    url = os.getenv("AZURE_ADT_URL")
    client = get_credential(url)

    # Used for easy reading in the logs
    logging.info('***** Begin Function ****** ')

    req_body = req.get_json()
    # will use whatever env variable is specified for the `DEVICE_ID` and fetch the metadata for that item. 
    # To change this, simply change the value in the environmental variables. 
    deviceID = req_body.get(os.getenv("DEVICE_ID"), "DEVICE_ID not found in env variables")


    logging.info(f"request to get metadata for: [{deviceID}] in ADT instance [{url}]")

    if deviceID:
        query_expression = f"""
                SELECT  *
                FROM DigitalTwins T  
                WHERE T.$dtId = {deviceID}
            """
        
        query_result = client.query_twins(query_expression)       
        data = [i.to_dict() for i in query_result]
        response = {
            'AZURE_ADT_URL': url,
            'data':data

        }
        return func.HttpResponse(
             response,
             status_code=200
        )
    else:
        response = f"ERROR: request does not have the `DEVICE_ID` field: {os.getenv('DEVICE_ID')}"
        logging.info(response)
        return func.HttpResponse(
             response,
             status_code=200
        )

