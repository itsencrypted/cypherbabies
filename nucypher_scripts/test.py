from base64 import b64decode, b64encode                                 
import json
import requests
gisalice = "http://localhost:8151"
gavk = "021fdbce49bbdbaa061fe0a9228de10cf2f4eaedca39889fb5914b72379486e4c6"
derivation_response = requests.post(f"{http://localhost:8151}/derive_policy_pubkeys/lab_exams")
derivation_response.content

