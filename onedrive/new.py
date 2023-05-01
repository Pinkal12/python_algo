import requests
import json

# Set the parameters
access_token = ""
file_name = "demo.csv"
file_path = "/home/hanuai/mygithub/py_code/onedrive/demo.csv"
upload_url = "https://graph.microsoft.com/v1.0/me/drive/root:/" + file_name + ":/createUploadSession"

# Get the upload session URL
headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}
response = requests.post(upload_url, headers=headers)
response_data = json.loads(response.text)
upload_url = response_data["uploadUrl"]

# Upload the file
with open(file_path, "rb") as f:
    file_data = f.read()
    headers = {
        "Content-Range": "bytes 0-" + str(len(file_data) - 1) + "/" + str(len(file_data)),
        "Content-Type": "application/octet-stream"
    }
    response = requests.put(upload_url, headers=headers, data=file_data)

# Check the upload status
if response.status_code == 200:
    print("File uploaded successfully!")
else:
    print("Upload failed with status code " + str(response.status_code))
