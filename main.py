from pyrogram import Client, filters 

API_ID = "10460140" 
API_HASH = "e6618cb334078f32d38cf25ded6f4839" 
BOT_TOKEN = "5494600954:AAGyAqUnMvOuy5JloCfhJa6ph6nzn2-OCfM"

CINEMALOKHAM = Client(
    name="cinemalokham",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@CINEMALOKHAM.on_message(filters.command("start"))
async def start_cmd(client,message):
    await message.reply_video(   
        video="https://telegra.ph/file/dd18bd700f5ff70381320.mp4",
        caption="ON DEVELPOING PLZ WAIt "
    )
        
    print("START Command")                    
                         
print("BOT RUNNING")

CINEMALOKHAM.run()
