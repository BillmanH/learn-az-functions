# https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/digitaltwins/azure-digitaltwins-core/samples/notebooks

# Defaults
from asyncio.log import logger
import logging
import azure.functions as func

# Needed for this app
from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import DefaultAzureCredential
import os, json


def get_credential(url):
    # you will get this from the ADT resource at portal.azure.com
    credential = DefaultAzureCredential()
    serviceClient = DigitalTwinsClient(url, credential)
    return serviceClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    # To reference a different URL, change the `AZURE_ADT_URL` in the enviornment variables
    # Note, must contain `https://`
    url = os.getenv("AZURE_ADT_URL", "AZURE_ADT_URL not found in env variables")
    client = get_credential(url)

    # Used for easy reading in the logs
    logging.info('***** Begin Function ****** ')

    req_body = req.get_json()
    # will use whatever env variable is specified for the `DEVICE_ID` and fetch the metadata for that item. 
    # To change this, simply change the value in the environmental variables. 
    deviceID = req_body.get(os.getenv("DEVICE_ID", "DEVICE_ID not found in env variables"))


    logging.info(f"request to get metadata for: [{deviceID}] in ADT instance [{url}]")

    if deviceID:
        ## This is the query
        ## You could modify this to get different information
        ## Test your query in the ADT tool before comitting here
        query_expression = f"""
            SELECT  *
            FROM DigitalTwins T  
            WHERE T.$dtId = '{deviceID}'
        """
        query_result = client.query_twins(query_expression)

        # There should only be one returned object, but for resiliancy I've returned the items in a list. 
        data = [i for i in query_result]
        logging.info(f'{len(data)} : Items returned from query')

        response = {
            'AZURE_ADT_URL': url,
            'data':data,
            'source':'azure function',
            'status':'ok'
        }

        logging.info('***** query returned data successfully ****** ')
        return func.HttpResponse(
            json.dumps(response),
            mimetype="application/json",
            status_code=200
        )
    else:
        response = {
            'AZURE_ADT_URL': url,
            'data':f"ERROR: request does not have the `DEVICE_ID` field: {os.getenv('DEVICE_ID', 'DEVICE_ID not found in env variables')}",
            'source':'azure function',
            'status':'error'
            }
        logging.info(response)
        return func.HttpResponse(
            json.dumps(response),
            mimetype="application/json",
            status_code=300
        )

