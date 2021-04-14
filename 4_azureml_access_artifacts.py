#%%
from azureml.core import Workspace , DataStore, Dataset

#%%
# Create Workspace
ws = Workspace.from_config(path="./config")

#%%
az_store=DataStore.register_azure_blob_container(
    workspace=ws,
    datastore_name="azure_sdk_blob01",
    account_name="azuremlstb01",
    container_name="azuremlstbb01blob",
    account_key="<acc key>"
)

#%%
# List all Workspacees in a subscription
ws_list=Workspace.list(subscription_id="<sub id>",
                       # below is optional
                       resource_group="<resource group>" 
                      )
# Output: Returns a dictionay with workspace name as 'key'
# We can convert it to normal python list as 
ws_list=list(ws_list)

#%%
# Access default data store
az_default_store=ws.get_default_datastore()

#%%
# List all datastores
store_list=list(ws.datastores)


#%%
# List all datasets in a datastore
ds_lst=list(ws.datasets.keys())
for items in ds_lst:
    print(items)

#%%
# Fetch dataset from workspace
az_dataset=Dataset.get_by_name(ws,'<ds name>')