#%%
from azureml.core import Workspace

# Create Workspace
ws = Workspace.create(name='Azureml-SDK-WS01',
                      subscription_id='9b4f5d78-71a6-46fe-b682-f9ae0c3b6796',
                      resource_group='my_test_resource_group',
                      create_resource_group=True,   # True if it does not exist
                      location='eastus2')

#%%
ws.write_config(path=./config)