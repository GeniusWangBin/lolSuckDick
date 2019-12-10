from wxpy import *
import json
import requests


bot = Bot()
bot = Bot(cache_path = True)

def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "87f4c0f17b2345febf740b9048c14b34"
    payload = {
        "key": api_key,
        "info": text,
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[来自,,,,] " + result["text"]
    
@bot.register()
def forward_message(msg):
    return auto_reply(msg.text)

embed()
