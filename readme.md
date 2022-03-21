# Getting Started with Azure Function (100% Python)

Adding templates here so I can spin up AZ functions quickly. 

Following the tutorial from [the MSFT docs](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash%2Cbrowser) Last updated: March 8th 2021

# Functions listed
| Name | Folder | Description | State |
|---|---|---|---|
| HTTP trigger | AZfuncHTTPtrig | Basic HTTP function. This is the one you set up first. | working |
| Azure Event Hub trigger | AZfuncEHtrigger | EventHub trigger (because I couldn't find a tutorial for it in Python) | started |


#### Project Structure
The main project folder (<project_root>) can contain the following files:

* **requirements.txt** - Contains the list of Python packages the system installs when publishing to Azure.

* **host.json** - Contains global configuration options that affect all functions in a function app. This file does get published to Azure. Not all options are supported when running locally. To learn more, see [host.json](https://aka.ms/azure-functions/python/host.json).

* **.funcignore** - (Optional) Declares files that shouldn't get published to Azure. Usually, this file contains .vscode/ to ignore your editor setting, .venv/ to ignore local Python virtual environment, tests/ to ignore test cases, and local.settings.json to prevent local app settings being published.

Each function has its own code file and binding configuration file ([**function.json**](https://aka.ms/azure-functions/python/function.json)).

#### Developing your first Python function using VS Code

If you have not already, please checkout our [quickstart](https://aka.ms/azure-functions/python/quickstart) to get you started with Azure Functions developments in Python. 

#### Publishing your function app to Azure 

For more information on deployment options for Azure Functions, please visit this [guide](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python#publish-the-project-to-azure).

#### Next Steps

* To learn more about developing Azure Functions, please visit [Azure Functions Developer Guide](https://aka.ms/azure-functions/python/developer-guide).

* To learn more specific guidance on developing Azure Functions with Python, please visit [Azure Functions Developer Python Guide](https://aka.ms/azure-functions/python/python-developer-guide).