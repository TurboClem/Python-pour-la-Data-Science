"""
Run this file if you want to get the access token and the headers.
"""
from functions import access_token


# Access to the API
token = access_token()

# Request with the access token :
headers = {
    'Authorization': f'Bearer {token}',
}

