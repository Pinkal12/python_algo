# Build the POST parameters
params = {
          'grant_type': 'refresh_token', 
          'client_id': your_app_client_id,
          'refresh_token': refresh_token_that_you_got_in_the_previous_step
         }

response = requests.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=params)

access_token = response.json()['access_token']
new_refresh_token = response.json()['refresh_token']

# ^ Save somewhere the new refresh token. 
# I just overwrite the file with the new one. 
# This new one will be used next time.

header = {'Authorization': 'Bearer ' + access_token}

# Download the file
response = requests.get('https://graph.microsoft.com/v1.0/me/drive/root:' +
                        PATH_TO_FILE + '/' + FILE_NAME + ':/content', headers=header)

# Save the file in the disk 
with open(file_name, 'wb') as file:
    file.write(response.content)