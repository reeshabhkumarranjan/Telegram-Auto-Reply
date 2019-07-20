from telethon import TelegramClient, events
import os
import time

session_file = "_session_"

# for key in os.environ.keys():
    # print(key)

friendsId = int(os.environ.get('telethon_friends_id'))
selfId = int(os.environ.get('telethon_self_id'))
api_id = os.environ.get('telethon_api_id', default = None)
api_hash = os.environ.get('telethon_api_hash', default = None)
phone = os.environ.get('telethon_phone_number', default = None)

print("extracted values from system variables")
time.sleep(1)

if None in [api_id, api_hash, phone]:
    print("Your environment variables not right")
    exit(1)

reply_message = "H3H3 (Telethon API)"

if __name__ == "__main__":

    client = TelegramClient(session_file, api_id, api_hash)

    @client.on(events.NewMessage(incoming = True))
    async def handle_new_message(event):
        from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
        print(time.asctime(), '-', event.message, event.message.from_id)  # optionally log time and message
        print("user_id:", event.message.from_id)
        time.sleep(1)  # pause for 1 second to rate-limit automatic replies
        
        # doing the reply stuff
        userId = event.message.from_id
        msg = event.message
        print("hehe_count:", str(msg).lower().count("hehe"))
        if userId == friendsId and str(msg).lower().count("hehe") > 0:
            # pass
            await msg.reply(reply_message)
    print("starting the service")
    client.start(phone)
    print("listening...")
    client.run_until_disconnected()
    print(time.asctime(), '-', "Stopped!")

