import importlib
import eco_values
import telegram_api
importlib.reload(eco_values)
importlib.reload(telegram_api)

if __name__ == '__main__':

    [battery_status, power_input, battery_temp] = eco_values.get_ecoflow_values()

    telegram_api.send_bot_message(battery_status, power_input, battery_temp, False)
