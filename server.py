from bot import telegram_chatbot
from mukbanggenerator import getMukbangURL, outputURL

update_id = None
bot = telegram_chatbot("config.cfg")
from_ = None
message = None

def make_reply(msg):
    if msg != '/start':
        bot.send_document(outputURL(getMukbangURL(msg)),from_)
    
while True:
    print("...")
    updates = bot.get_updates(offset=update_id)
    try:
        updates = updates["result"]
    except:
        continue
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            name = item["message"]["from"]["first_name"]
            print(f'{name}: {message}')
            make_reply(message)
            bot.send_message("what ingredient would you like?", from_)
            
