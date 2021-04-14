#%%
from azureml.core import Workspace,Datastore,Dataset,Experiment

#%%
# Access the Workspace , Datastore, Dataset
ws=Workspace.from_config('./config')
az_store=Datastore.get(ws,'azure_sdk_blob01')
az_dataset=Datastore.get_by_name(ws,"<dtst name>")
az_default_store=ws.get_default_datastore()

#%%
# Create an Experiment object
experiment= Experiment(workspace=ws,name='Loan-SDK-Exp01')


#%%
# Run Experiment
new_run=experiment.start_logging()

df=az_dataset.to_pandas_dataframe()

# Complete an Experiment before below line experiment is alive
new_run.complete()



#%%
