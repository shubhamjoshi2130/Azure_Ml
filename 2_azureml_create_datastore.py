#%%
from azureml.core import Workspace , DataStore

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
