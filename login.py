import requests  # pip install requests
import json

data = { 'email': 'user@somewhere.com', 'password': 'Password1$' };
headers = { 'Clearblade-Systemkey': <SYSTEM_ID>, 'Clearblade-Systemsecret': <SYSTEM_SECRET> };

# authenticate
r = requests.post('https://platform.clearblade.com:443/api/v/1/user/auth', data=json.dumps(data), headers=headers);
print r.status_code
print r.text
