import requests
import json
import os
from dotenv import load_dotenv, dotenv_values 

def send_bot_message(battery_status,power_input, battery_temp):

    load_dotenv() 
    
    telegram_token =  os.getenv("telegram_token")
    chat_id =  os.getenv("chat_id")
    
        
        
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"

    payload = json.dumps({
          "text": f'''
⚠️ Power input: {power_input}
⚠️ Battery stat: {battery_statuus}
⚠️ Battery temp: {battery_temp}
''',
          "chat_id": chat_id
        })
    headers = {
          'Content-Type': 'application/json'
        }
        
    response = requests.request("POST", url, headers=headers, data=payload) 

    print(response.text)
