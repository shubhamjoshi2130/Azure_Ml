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
# our csv can be created using multiple csv files present in the dataset
# we can ghave several tuples in one path list
csv_path=[(az_store,"<filepath>.csv"),(az_store,"<filepath2>.csv")]

#%%
# Create the dataset
loan_dataset=Dataset.Tabular.from_delimited_files(path=csv_path)

#%%
# Register the dataset to workspace
loan_dataset=loan_dataset.register(workspace=ws,
                                   name="Loan application using SDK",
                                   create_new_version=True)