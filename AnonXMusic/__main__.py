import asyncio
import importlib
from pyrogram import Client, idle
import config
from AnonXMusic import LOGGER
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import sudo
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init(token):
    app = Client("anon", bot_token=token)
    await app.start()

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    for all_module in ALL_MODULES:
        importlib.import_module("AnonXMusic.plugins." + all_module)

    LOGGER("AnonXMusic.plugins").info("Successfully Imported Modules...")

    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except:
        pass
    await Anony.decorators()
    LOGGER("AnonXMusic").info(
        "AnonX Music Bot Started Successfully."
    )

    await idle()
    await app.stop()
    LOGGER("AnonXMusic").info("Stopping AnonX Music Bot...")


if __name__ == "__main__":
    bot_token = input("Please provide your bot token: ")
    asyncio.get_event_loop().run_until_complete(init(bot_token))
