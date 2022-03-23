# Getting Started with Azure Function (100% Python)

Adding templates here so I can spin up AZ functions quickly. 

Following the tutorial from [the MSFT docs](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash%2Cbrowser) Last updated: March 8th 2021

# Functions listed
| Name | Folder | Description | State |
|---|---|---|---|
| HTTP trigger | AZfuncHTTPtrig | Basic HTTP function. This is the one you set up first. | working |
| Azure Event Hub trigger | AZfuncEHtrigger | EventHub trigger | started |

## You need to add:
* `local.settings.json` - [which you can get here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-local#local-settings-file), but it's also generated when you run `func init`.
* `function.json` - for each app, there are specific function parameters that are omited from the code here. You'll need to create that file. 
* to build an environment you can use the `requirements.txt`. That has everything for the trigger-simulators as well as the functions. 

### Running locally
* run `func init` to create the extra json files that you will need, as well as starting the project
* `func start` to start the local functions repo