# Azure Function App Demo Project
---
- ## [Local Environment Setup Guide on Apple Silicon(*M1 - ARM Architecture*) for Python Runtime](./LOCAL_SETUP.md)

## Create new Azure Fucntion and run it locally

- Create new local project usig Python template
```bash
❯ func init LocalFunctionProj --python

# Following files will be created
# requirements.txt
# getting_started.md
# gitignore
# host.json
# local.settings.json
```

- Create new Azure Function
```bash
❯ cd LocalFunctionProj
❯ func new test_func

# Following files will be created
# test-func/__init__.py
# test-func/function.json
```

- Now, open `local.settings.json` file, there set `AzureWebJobStorage` to `UseDevelopementStorage=true`

- Start the storage emulator on another tab of `rosettaTerm`
```bash
❯ azurite
# Sample output
# Azurite Blob service is starting at http://127.0.0.1:10000
# Azurite Blob service is successfully listening at http://127.0.0.1:10000
# Azurite Queue service is starting at http://127.0.0.1:10001
# Azurite Queue service is successfully listening at http://127.0.0.1:10001
# Azurite Table service is starting at http://127.0.0.1:10002
# Azurite Table service is successfully listening at http://127.0.0.1:10002
```

- Finally, run the function.
```bash
❯ conda activate rosetta
❯ cd LocalFunctionProj/
❯ pip install -r requirements.txt
❯ func start host
# Found Python version 3.10.8 (python3).

# Azure Functions Core Tools
# Core Tools Version:       4.0.4865 Commit hash: N/A  (64-bit)
# Function Runtime Version: 4.12.2.19454

# [2022-11-17T10:20:16.290Z] Worker process started and initialized.

# Functions:

# 	HttpTrigger1:  http://localhost:7071/api/hello

# For detailed output, run func with --verbose flag.
# [2022-11-17T10:20:20.719Z] Host lock lease acquired by instance ID '000000000000000000000000914B231E'.
```

- To Publish the Function to Azure Function App `TestFunctionApp` created via Portal. 
```bash
❯ az login # will be redirected to browser
❯ func azure functionapp publish TestFunctionApp
# Deployment successful. deployer = Push-Deployer deploymentPath = Functions App ZipDeploy. Extract zip. Remote build.
# Remote build succeeded!
# Syncing triggers...
# Functions in TestFunctionApp:
#     test-func - [httpTrigger]
#         Invoke url: https://tjdemoapp.azurewebsites.net/api/test-func
```

And you are done! 
Please check your portal and test the Function...
