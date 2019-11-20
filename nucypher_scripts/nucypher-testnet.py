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

import file

f = open("/Users/juliana/Documents/repos-hackathon/cypherbabies/lab_exams/Lab.Chol.2019.08.10.pdf", 'rb')
data = f.read()


print("Step 1: Deriving Policy Key")

derived_label_json = requests.get(f"{gisalice}/derive_policy_encrypting_key/lab_chol_2019_08_10_pdf")