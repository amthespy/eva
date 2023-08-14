import logging
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from info import SESSION, API_ID, API_HASH, BOT_TOKEN

logging.getLogger().setLevel(logging.INFO)


class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name=SESSION,
            api_id=24490919,
            api_hash="d1b3b15126c47dd4cb491553ee1db910",
            bot_token="6482267322:AAHANKv8d7kIzjAM5ICDZE4eP68FoACk4S8",
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )
        
    async def start(self):
         await super().start()
         me = await self.get_me()
         self.username = me.username
         logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
       

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot Restarting.......")


app = Bot()
app.run()
