import importlib
import eco_values
import telegram_api
importlib.reload(eco_values) 
importlib.reload(telegram_api) 

if __name__ == '__main__':
    
    [battery_status, power_input] = eco_values.get_ecoflow_values()
    
    if battery_status < 75 or power_input < 200 :
        telegram_api.send_bot_message(battery_status, power_input)
    else:
        print('Healthy system')
