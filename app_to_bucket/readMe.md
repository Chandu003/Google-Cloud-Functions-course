# Send Data from APP to Google Storage Bucket
Install libararies in requirement.txt using 
```pip install -r requirement.txt```

Then to have the server running, run Flask app using,
```
python flask_app.py
```

## Step-by-Step Guide to Set Up Google Cloud Application Default Credentials
1. Create a Service Account:
    Go to the Google Cloud Console.
    Navigate to IAM & Admin > Service accounts.
    Click Create Service Account.
    Provide a name and description for the service account.
    Click Create and then Continue.
    Grant the necessary permissions (e.g., "Storage Admin") to the service account.
    Click Done.
2. Download the Service Account Key:
    In the service accounts list, find the newly created service account.
    Click the three dots on the right and select Manage keys.
    Click Add key > Create new key.
    Choose JSON and click Create.
    A JSON file containing your key will be downloaded to your computer.
3. Set the GOOGLE_APPLICATION_CREDENTIALS Environment Variable:

    Move the downloaded JSON file to a secure location on your server or development machine.
    Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of this JSON file.
```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account-file.json"
```

4. Verify your script:
```
from google.cloud import storage

def list_buckets():
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)

if __name__ == "__main__":
    list_buckets()
```
If your credentials are set up correctly, you should see a list of your Google Cloud Storage buckets.

Then run `streamlit run app.py` to have the front-end UI to upload file.
To have the view of the how the UI looks check-out `file_upload_app.pdf`

After successfully uploading the file, in order to upload the file to GCP Bucket, we have to specify the bucket name to which we want to send the file and click on `Upload to GCP`.

Once the file is uploaded to source-bucket-bre, `process_file` cloud function is invoked to extract business rules for that file and place it in destination-bucket-bre.

