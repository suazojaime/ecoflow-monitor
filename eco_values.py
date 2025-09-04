import time
import random
import hmac
import hashlib
import requests
import os
from dotenv import load_dotenv, dotenv_values 

def get_ecoflow_values():

    load_dotenv() 
    
    access_key = os.getenv("access_key")
    secret_key =  os.getenv("secret_key")
    device_sn =  os.getenv("device_sn")
    
    
    # === Generate timestamp and nonce ===
    timestamp = str(int(time.time() * 1000))  # milliseconds since epoch
    nonce = str(random.randint(100000, 999999))  # 6-digit random number
    
    # === Build the signature string (order is critical!) ===
    signing_string = f"sn={device_sn}&accessKey={access_key}&nonce={nonce}&timestamp={timestamp}"
    
    # === Generate HMAC-SHA256 signature (hex format) ===
    signature = hmac.new(secret_key.encode('utf-8'), signing_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    # === Headers (auth only) ===
    headers = {
        'accessKey': access_key,
        'timestamp': timestamp,
        'nonce': nonce,
        'sign': signature
    }
    
    # === Make the GET request with sn in query ===
    url = f'https://api.ecoflow.com/iot-open/sign/device/quota/all?sn={device_sn}'
    
    response = requests.get(url, headers=headers)
    
    # === Print response ===
    #print("Status:", response.status_code)
    #print("Response:", response.json())

    battery_status = response.json()['data']['bmsBattSoc']
    power_input = response.json()['data']['powGetAcIn']
    battery_temp = response.json()['data']['bmsMinCellTemp']

    return [battery_status, power_input, battery_temp]
