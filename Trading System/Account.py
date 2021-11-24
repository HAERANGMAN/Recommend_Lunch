import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

Access_K="h41r61kSRYM0smux5KUocKinpYT9LPiYCJ7iJnSW"
Secret_K="4epSf7zXGKjT9phzF1zalpEwoSQTqGMPHuikuQdq"

payload = {
    'access_key': Access_K,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, Secret_K)
authorization_token = 'Bearer {}'.format(jwt_token)

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/accounts", headers=headers)

print(res.json())

