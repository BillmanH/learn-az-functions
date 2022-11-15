#%%
import asyncio
import yaml
import datetime

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

#%%
message = yaml.safe_load(open("example_request.json"))
local_settings_json = yaml.safe_load(open("../local.settings.json"))
function_json = yaml.safe_load(open("function.json"))

#%%


async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(
        conn_str=local_settings_json["Values"]["AzureEventHubConnectionString"],
        eventhub_name=function_json['bindings'][0]['eventHubName'],
    )

    now = datetime.datetime.now()
    s = "%Y-%m-%dT%H:%M:%SZ"
    
    message["payload"]["timestamp"] = now.strftime(s)

    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData(str(message)))
        event_data_batch.add(EventData(str(message)))
        event_data_batch.add(EventData(str(message)))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

#%%

# Note that if you are running this in repl (like a jupyter notebook or ipython). You'll need to set the event loop policy (as there is already a loop running)
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# import nest_asyncio
# # this is required for running in a Jupyter Notebook. 
# nest_asyncio.apply()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

# %%
