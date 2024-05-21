import streamlit as st
import requests
import os

def main():
    st.set_page_config(page_title="File Upload App", page_icon="📂", layout="wide")

    st.title("📂 File Upload App")
    st.write("Upload your file below:")

    uploaded_file = st.file_uploader("Choose a file", type=["cpp", "txt", "png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        st.write(f"**Filename:** {uploaded_file.name}")
        st.write(f"**File type:** {uploaded_file.type}")
        st.write(f"**File size:** {uploaded_file.size} bytes")
        st.write(uploaded_file)
        # st.write(os.path.splitext(uploaded_file.name)) # for debug
        # Display file content if it's a text file
        st.header('File content')
        with st.expander('expand/minimize'):
            if os.path.splitext(uploaded_file.name)[1] == ".txt":
                st.text_area("File content", uploaded_file.getvalue().decode("utf-8"))
            elif os.path.splitext(uploaded_file.name)[1] in [".jpg",".jpeg","png"]:
                st.image(uploaded_file)
            elif os.path.splitext(uploaded_file.name)[1] == '.cpp':
                st.text_area("File content", uploaded_file.getvalue().decode("utf-8"))

        st.write("## Upload to Google Cloud Storage")
        bucket_name = st.text_input("Enter your Google Cloud Storage bucket name:")

        if st.button("Upload to GCS"):
            if bucket_name:
                try:
                    # Send file to Flask endpoint
                    files = {'file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    response = requests.post(
                        "http://localhost:5000/upload",
                        files=files,
                        data={'bucket_name': bucket_name}
                    )

                    if response.status_code == 200:
                        st.success(response.json()["message"])
                        with st.expander('Expand to see BRE'):                           
                            response.json()["file_content"]
                    else:
                        st.error(f"Error: {response.json()['detail']}")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please enter a bucket name.")

if __name__ == "__main__":
    main()
