import azure.storage.blob as azureblob
import azure.batch.batch_service_client as batch
import azure.batch.batch_auth as batchauth
import azure.batch.models as batchmodels
import config

    # Create a Batch service client. We'll now be interacting with the Batch
    # service in addition to Storage
credentials = batchauth.SharedKeyCredentials(config._BATCH_ACCOUNT_NAME,
                                             config._BATCH_ACCOUNT_KEY)

batch_client = batch.BatchServiceClient(
    credentials,
    batch_url=config._BATCH_ACCOUNT_URL)


jobs = batch_client.job.list()

# print each job id
for job in jobs:
    print("Deleting job: " + job.id)
    batch_client.job.delete(job.id)