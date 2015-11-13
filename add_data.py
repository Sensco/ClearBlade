import requests  # pip install requests
import json
import random
import uuid

data = { 'email': 'user@somewhere.com', 'password': 'Password1$' };
headers = { 'Clearblade-Systemkey': <SYSTEM_ID>, 'Clearblade-Systemsecret': <SYSTEM_SECRET> };

# generate some fake wave data
waveData = []
timestamp = 0.0
iteration = str(uuid.uuid4())
for i in range(0,100):
    timestamp = timestamp + random.random()
    waveData.append({'iteration': iteration, 'amplitude': random.uniform(-10,10), 'timestamp': timestamp})

# authenticate
r = requests.post('https://platform.clearblade.com:443/api/v/1/user/auth', data=json.dumps(data), headers=headers);
print r.status_code
print r.text
if r.status_code == 200:
    user_token = r.json()['user_token'];

    headers = { 'ClearBlade-UserToken': user_token };

    # upload the wave data
    data = waveData[0]
    print data

    #r = requests.post('https://platform.clearblade.com:443/api/v/1/code/f8c595e40aba839dc2bea3fbe8a001/AddWaveData', data=json.dumps(data), headers=headers);
    #print r.status_code
    #print r.text

    for i in range(0,100):
        r = requests.post('https://platform.clearblade.com:443/api/v/1/code/f8c595e40aba839dc2bea3fbe8a001/AddWaveData', data=json.dumps(waveData[i]), headers=headers);
        if r.status_code != 200:
            print r.status_code
