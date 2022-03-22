import asyncio
import yaml
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

# edited this so that I can pull in the same values from the bindings witout having to create a special yaml file
params = yaml.safe_load(open('function.json'))['bindings'][0]


async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(
        conn_str=params["connection"], eventhub_name=params["eventHubName"])
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData('First event '))
        event_data_batch.add(EventData('Second event'))
        event_data_batch.add(EventData('Third event'))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
