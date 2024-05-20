from flask import Flask, request, jsonify
from google.cloud import storage
import os

app = Flask(__name__)

def upload_to_gcs(bucket_name, file_obj, file_name):
    # Initialize a Google Cloud Storage client
    client = storage.Client()
    
    # Get the bucket
    bucket = client.bucket(bucket_name)
    
    # Create a new blob (object) in the bucket with the file name
    blob = bucket.blob(file_name)
    
    # Upload the file to the blob
    blob.upload_from_file(file_obj)
    
    return f"File {file_name} uploaded to {bucket_name}."

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'bucket_name' not in request.form:
        return jsonify({"detail": "Missing file or bucket name"}), 400

    file = request.files['file']
    bucket_name = request.form['bucket_name']

    try:
        print(file.stream)
        response = upload_to_gcs(bucket_name, file.stream, file.filename)
        return jsonify({"message": response}), 200
    except Exception as e:
        return jsonify({"detail": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
