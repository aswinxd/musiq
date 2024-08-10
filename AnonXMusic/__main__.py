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

    API_ID= "7980140"
    API_HASH= "db84e318c6894f560a4087c20c33ce0a"
    LOG_GROUP_ID= "-1001535538162"
    MONGO_DB_URI= "mongodb+srv://bot:bot@cluster0.8vepzds.mongodb.net/?retryWrites=true&w=mmajority"
    OWNER_ID= "1137799257"
    LOGGER_ID= "-1001535538162"
    STRING_SESSION="BQGCzhoAKeE4RWl9YaPkNcMeHQEDQQq-ivci5xNDlNMdybqSC7BaaWli0nEU1whOzGh9eQ2rI8Ky8s0nYR6dm7KL48ETsYUucRDWC-lK8YzfSGTabYnO9TtPKqQF25LVxPwhfRoNyomq-zXgiPmqbVnRwRCyojGzQNIhCC-KpKro-CjX5kg7EZtenX-GHSBiQjhy8G6__4DfO7yPDLZv8ZwgZ0jWRHuYcs_f_s05e1p1FwQLI9yDRqty1vMw8yzJDnmJNvzruA8X1zPGYYtgIJn3VCZzeob7EQD6M-GHdetrK1x3la5IzQoILy1lrEXNiaJz-d8i2_KMaGXSRYlTq0gBFvwcDAAAAAFvEOseAA"
 #STRING_SESSION2=BQFaif8AODOl3hH1-74AXivQDlNiw23bCkkALragNPxHYXBwwOOGM5Bv6aj1oyp0ngk8MnYtZdYZJiBdFgrEzpSnJKiKSXg3hsj8MS6RFYafqFoT-grIKnOf9kWALFib8fpAnheRHnAON0DfioaX_GZo_n64OMGUK7-Z4bPKbBca70VS_GQv4Bwk8xE-WUZX0IideiJi0Id6EM-If0MvhMZo27Yro4WPxzxJeNn3rR7D01x7nrp3JAK7hPi7AGr9lfl_OsMyfIcGWq4jnu5xpUPxQjpf1QvrJXd9BKMUBcjSPJG1fco2gIyJBeIXFd1pOMFu7RlyqURJGcFq2h9VIamXvd5r5wAAAAGT0MqPAA
    bot_token = input("Please provide your bot token: ")
    asyncio.get_event_loop().run_until_complete(init(bot_token))
