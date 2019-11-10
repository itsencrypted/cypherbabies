from base64 import b64decode, b64encode                                 
import json
import requests
gisalice = "http://localhost:8151"
gisalice_keys = requests.get(f"{gisalice}/public_keys")
print(gisalice_keys)

data = json.loads(gisalice_keys.content)
print(data)  

data["result"]

data["result"]["alice_verifying_key"]

derived_label_json = requests.post(f"{gisalice}/derive_policy_encrypting_key/cholest_data_2019_10_08")

derived_label_json.content

derived_label_data = json.loads(derived_label_json.content)

prk = derived_label_data['result']['policy_encrypting_key']



print(prk)

# derived_response = requests.post(f"{gisalice}/derive_policy_encrypting_key/cholest_data_2019_10_08")
# print(derived_response)


# derived_label_json = requests.post(f"{gisalice}/derive_policy_encrypting_key/nameofthepdffile
