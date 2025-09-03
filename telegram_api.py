import requests
import json
import os
from dotenv import load_dotenv, dotenv_values 

def send_bot_message(battery_status,power_input):

    load_dotenv() 
    
    telegram_token =  os.getenv("telegram_token")
    chat_id =  os.getenv("chat_id")
    
        
        
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"

    payload = json.dumps({
          "text": f"⚠️ Power input: {power_input}",
          "chat_id": chat_id
        })
    headers = {
          'Content-Type': 'application/json'
        }
        
    response = requests.request("POST", url, headers=headers, data=payload) 

    print(response.text)
        
    payload = json.dumps({
          "text": f"⚠️ Battery stat: {battery_status}",
          "chat_id": chat_id
        })
    headers = {
          'Content-Type': 'application/json'
        }
        
    response = requests.request("POST", url, headers=headers, data=payload)
        
    print(response.text)
