import functions_framework
from google.cloud import storage
import google.generativeai as genai

@functions_framework.cloud_event
def process_file(cloud_event):
    data = cloud_event.data
    bucket_name = data['bucket']
    file_name = data['name']

    if not file_name.endswith('.cpp'):
        print(f"Ignoring non-CPP file: {file_name}")
        return

    # Initialize the storage client
    storage_client = storage.Client()

    # Read the file from the source bucket
    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(file_name)
    file_contents = source_blob.download_as_text()

    # Process the file (this is where your custom logic goes)
    processed_contents = process_cpp(file_contents)

    # Write the processed file to the destination bucket
    destination_bucket = storage_client.bucket('destination-bucket-bre')
    destination_blob = destination_bucket.blob('output.txt')
    destination_blob.upload_from_string(processed_contents)

    print(f"Processed file {file_name} and stored to {destination_bucket.name}/output.txt")

def process_cpp(file_contents):
    # Placeholder for actual processing logic
    # Example: Convert content to uppercase (replace with your actual logic)
    # return file_contents.upper()
    genai.configure(api_key="API-GOES-HERE")
    model = genai.GenerativeModel('gemini-pro')
    prompt_template = """
    Context:
    You are a highly intelligent AI specialized in understanding and analyzing C++ code. Your task is to read through a .cpp file and extract any business rules implemented in the code. Business rules are the logical statements that define or constrain some aspects of the business, often involving conditions and actions.

    Instructions:
    Carefully analyze the provided C++ code.
    Identify and extract any business rules within the code. Business rules typically involve conditional statements (like if, else if, switch), loops with business logic, or any specific calculations or constraints that impact business decisions or operations.
    For each business rule identified, provide a clear and concise description of the rule in plain English.
    """
    prompt = prompt_template + file_contents
    response = model.generate_content(prompt)
    return response.text

