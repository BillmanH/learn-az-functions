# Azure Function to sync Event Hub with Azure Digital Twin

Based on a very similar tool from the Azure Team [based in .net but does the same thing](https://learn.microsoft.com/en-us/azure/digital-twins/how-to-ingest-iot-hub-data)

This recieves a message from the event hup and, with it, updates a digital twin as specified. 

Using Environment Variables:
| Name | Purpose |
|---|---|
| DEVICE_ID | The filed in the input message that is to be used as the device ID | 
| ADT_URL | URL of the ADT instance that will be updated, for connection purposes |

