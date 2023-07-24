import requests
import tkinter as tk
import urllib.request
from bs4 import BeautifulSoup
import json


def update_labels():
    web_server_url = "http://192.168.123.102:80"

    response = requests.get(web_server_url)
    data = response.text

    response_dict = json.loads(data)
    ip_address = response_dict.get('ip_address', '')
    lbl_ip.config(text=f"IP address: {ip_address}")
    lbl_temperature.config(text=f"Temperature : {round(response_dict.get('temperature_celsius', ''), 2)}C ({round(response_dict.get('temperature_fahrenheit', ''), 2)}F)")

# create gui component
current_temperature_condition = tk.Tk()
current_temperature_condition.title("Inha Smart Factory!")
current_temperature_condition.geometry("400x200")
lbl_ip = tk.Label(current_temperature_condition, text="IP address: ")
lbl_temperature = tk.Label(current_temperature_condition, text="")
btn_check_temperature = tk.Button(current_temperature_condition, text="Check Temperature!", command=update_labels)

# layout
lbl_ip.grid(row=0, column=0)
lbl_temperature.grid(row=0, column=1)
btn_check_temperature.grid(row=2, column=0, columnspan=2, sticky=tk.EW)

current_temperature_condition.mainloop()