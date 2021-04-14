#%%
from azureml.core import Workspace,Datastore,Dataset

#%%
# Access the Workspace , Datastore, Dataset
ws=Workspace.from_config('./config')
az_store=Datastore.get(ws,'azure_sdk_blob01')
az_dataset=Datastore.get_by_name(ws,"<dtst name>")
az_default_store=ws.get_default_datastore()


#%%
# Convert Azure Dataset into pandas dataframe
df=az_dataset.to_pandas_dataframe()

#%
# Uploading data
df_sub=df[['Married','Gender','Loan_status']]

az_ds_from_df=Dataset.Tabular.register_pandas_dataframe(dataframe=df_sub,
                                                        target=az_store,
                                                        name="Loan DataSet from Dataframe")


#%%
# Upload files
files_list=['./data/test1.csv',
            './data/test2.csv']
az_store.upload_files(files=files_list,
                      target_path="Loan Data/",
                      relative_root="./data/",
                      overwrite=True)

#%%
# Upload directories
az_store.upload(src_dir="./data"
                target_path='Loan data/data',
                overwrite=True)