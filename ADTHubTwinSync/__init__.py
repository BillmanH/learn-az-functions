# Loaded by AZ Functions by default
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

def create_patch(metadata):
    pass

def main(event: func.EventHubEvent):
    # To reference a different URL, change the `AZURE_ADT_URL` in the enviornment variables
    # Note, must contain `https://`
    logging.info('***** Begin Function ****** ')

    url = os.getenv("AZURE_ADT_URL", "AZURE_ADT_URL not found in env variables")
    client = get_credential(url)
    logging.info(f'Function triggered to process a message: {event.get_body().decode()}')
    logging.info(f'  EnqueuedTimeUtc = {event.enqueued_time}')
    logging.info(f'  SequenceNumber = {event.sequence_number}')
    logging.info(f'  Offset = {event.offset}')

    deviceID = event.metadata.get(os.getenv("DEVICE_ID", "DEVICE_ID not found in env variables"))
    logging.info(f"request to get update data for: [{deviceID}] in ADT instance [{url}]")



    
    # Metadata
    for key in event.metadata:
        logging.info(f'Metadata: {key} = {event.metadata[key]}')

    logging.info('***** function completed ****** ')