import logging

import azure.functions as func


def main(event: func.EventHubEvent):
    logging.info('*********** Process has begun **************')
