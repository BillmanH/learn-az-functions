# Getting Started with Azure Function (100% Python)

Adding templates here so I can spin up AZ functions quickly. 

Following the tutorial from [the MSFT docs](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash%2Cbrowser) Last updated: March 8th 2021

# Functions listed
| Name | Folder | Description | State |
|---|---|---|---|
| Digital Twin HTTP Trigger | AZfuncHTTPtrig | Given an id, fetches remaining twin data from ADT | working |
| Azure Event Hub trigger | AZfuncEHtrigger | Given a eventhub message, patches a tiwn in ADT | started |

## You need to add:
* `local.settings.json` - [which you can get here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file), but it's also generated when you run `func init`.
* `function.json` - for each app, there are specific function parameters that are omited from the code here. You'll need to create that file. 
* to build an environment you can use the `requirements.txt`. That has everything for the trigger-simulators as well as the functions. 

```
az dt role-assignment create --dt-name <your-Azure-Digital-Twins-instance> --assignee "<principal-ID>" --role "Azure Digital Twins Data Owner"
```


### Running locally
* run `func init` to create the extra json files that you will need, as well as starting the project
* `func start` to start the local functions repo

