# Loaded by AZ Functions by default
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

def main(event: func.EventHubEvent):
    logging.info(f'Function triggered to process a message: {event.get_body().decode()}')
    logging.info(f'  EnqueuedTimeUtc = {event.enqueued_time}')
    logging.info(f'  SequenceNumber = {event.sequence_number}')
    logging.info(f'  Offset = {event.offset}')

    # Metadata
    for key in event.metadata:
        logging.info(f'Metadata: {key} = {event.metadata[key]}')

