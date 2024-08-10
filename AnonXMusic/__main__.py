import asyncio
import importlib

from pyrogram import idle, Client, filters
from pyrogram.types import Message
from pyrogram.errors import BadRequest

import config
from AnonXMusic import LOGGER, app, userbot
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import sudo
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

# Dictionary to store cloned bot data
cloned_bots = {}

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
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
    await app.start()
    
    # Import all modules
    for all_module in ALL_MODULES:
        importlib.import_module("AnonXMusic.plugins" + all_module)
    LOGGER("AnonXMusic.plugins").info("Successfully Imported Modules...")
    
    await userbot.start()
    await Anony.start()
    
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except:
        pass
    
    await Anony.decorators()
    
    LOGGER("AnonXMusic").info(
        "\x41\x6e\x6f\x6e\x58\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\n\n\x44\x6f\x6e'\x74\x20\x66\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x76\x69\x73\x69\x74\x20\x40\x46\x61\x6c\x6c\x65\x6e\x41\x73\x73\x6f\x63\x69\x61\x74\x69\x6f\x6e"
    )
    
    await idle()
    await app.stop()
    await userbot.stop()
    
    LOGGER("AnonXMusic").info("Stopping AnonX Music Bot...")

# Add /clone command handler
@app.on_message(filters.command("clone") & filters.private)
async def clone_bot(client, message: Message):
    await message.reply("Please send me the bot token of the bot you want to clone.")

# Handle the received bot token directly
@app.on_message(filters.private & filters.text)
async def receive_token(client, message: Message):
    token = message.text.strip()
    
    # Simple token validation
    if len(token) < 46 or not token.startswith(""):
        await message.reply("Invalid token. Please try again.")
        return

    # Create a new Client instance with the received token
    new_bot = Client("NewClonedBot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=token)

    try:
        await new_bot.start()

        # Import all modules into the new bot instance to replicate the main bot's functionality
        for all_module in ALL_MODULES:
            importlib.import_module("AnonXMusic.plugins" + all_module)

        # Store the new bot instance in the dictionary
        cloned_bots[token] = {
            "client": new_bot,
            # Additional settings/features to be cloned
        }

        await message.reply("Bot successfully cloned! The new bot is now running.")
        
        # Start the cloned bot's event loop
        asyncio.create_task(new_bot.idle())
        
    except BadRequest as e:
        await message.reply(f"Failed to start the bot with the provided token: {e}")

# Optional: Add a command to stop cloned bots
@app.on_message(filters.command("stop_clone") & filters.private)
async def stop_clone(client, message: Message):
    token = message.text.split(' ', 1)[1].strip()

    if token in cloned_bots:
        await cloned_bots[token]["client"].stop()
        del cloned_bots[token]
        await message.reply("The cloned bot has been stopped and deleted.")
    else:
        await message.reply("No such bot found.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
