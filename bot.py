import json
import requests
import configparser as cfg
from mukbanggenerator import getMukbangURL, outputURL

class telegram_chatbot():
    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = f"https://api.telegram.org/bot{self.token}"

    def get_updates(self, offset=None):
        url = self.base + "/getUpdates?timeout=100"
        if offset:
            url = f"{url}&offset={offset + 1}"
        print(url)
        r = requests.get(url)
        return json.loads(r.content)
    
    def send_message(self,msg,chat_id):
        url = f"{self.base}/sendMessage?chat_id={chat_id}&text={msg}"
        if msg is not None:
            requests.get(url)
    
    def read_token_from_config_file(self,config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds','token')

    def send_document(self,url,chat_id):
        url = f"{self.base}/sendDocument?chat_id={chat_id}&document={url}"
        if url is not None:
            requests.get(url)