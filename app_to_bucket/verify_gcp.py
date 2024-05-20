from google.cloud import storage

def list_buckets():
    storage_client = storage.Client(project='cloud-functions-prac-07')
    buckets = list(storage_client.list_buckets())
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)

if __name__ == "__main__":
    list_buckets()