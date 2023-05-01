import requests
import json
import os


# Set the client ID, client secret, and tenant ID for your Azure AD app registration
client_id = '3efaa936-055a-46cb-b20f-42f88ad8398b'
client_secret = 'Oke8Q~LnNiPz7Q65qR~FeEOBp4fYNJ0-fFCosb1m'
tenant_id = 'b636e424-e0a8-4fff-81ba-2a126a7ce362'

# Set the path to your local file
file_path = '/home/hanuai/mygithub/py_code/onedrive/demo.csv'

# Set the URL for the OneDrive API upload endpoint
upload_url = 'https://graph.microsoft.com/v1.0/me/drive/root:/personal/pinkal_hanu_ai/Documents/App/demo.csv:/content'

# Construct the data for the Microsoft Graph API access token request
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default'
}

# Construct the URL for the Microsoft Graph API access token endpoint
token_url = 'https://login.microsoftonline.com/{0}/oauth2/v2.0/token'.format(tenant_id)

# Send the Microsoft Graph API access token request and get the access token
response = requests.post(token_url, data=token_data)
print(response.text)
access_token = json.loads(response.text)['access_token']
print(access_token)

# Set the headers for the OneDrive API upload request
upload_headers = {
    'Authorization': 'Bearer {0}'.format(access_token),
    'Content-Type': 'application/octet-stream'
}
print(upload_headers,'vdhshfdfgdhg')

# Open the local file and read its contents
with open(file_path, 'rb') as f:
    file_contents = f.read()

# Send the OneDrive API upload request and upload the file
response = requests.put(upload_url, headers=upload_headers, data=file_contents)

# Check the response to see if the upload was successful
if response.status_code == 201:
    print('The upload was successful')
else:
    print(response.status_code)
    print('The upload failed')
