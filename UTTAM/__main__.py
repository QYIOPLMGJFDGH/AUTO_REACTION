import sys
import asyncio
import logging
import importlib
from pyrogram import idle
from config import API_ID, API_HASH
from pyrogram.types import BotCommand
from config import OWNER_ID
from pyrogram import Client
from UTTAM import db as mongodb
from UTTAM import LOGGER, UTTAM, load_clone_owners
from UTTAM.modules import ALL_MODULES

CLONES = set()
cloneownerdb = mongodb.cloneownerdb
clonebotdb = mongodb.clonebotdb

# Function to restart all cloned bots
async def restart_bots():
    global CLONES
    try:
        logging.info("Restarting all cloned bots...")
        bots = [bot async for bot in clonebotdb.find()]
        
        async def restart_bot(bot):
            bot_token = bot["token"]
            ai = Client(bot_token, API_ID, API_HASH, bot_token=bot_token, plugins=dict(root="UTTAM/mplugin"))
            try:
                await ai.start()
                bot_info = await ai.get_me()
                await ai.set_bot_commands([
                    BotCommand("start", "Start the bot"),
                    BotCommand("clone", "Make your own reaction bot"),
                    BotCommand("ping", "Check if the bot is alive or dead"),
                    BotCommand("id", "Get users user_id"),
                    BotCommand("stats", "Check bot stats"),
                    BotCommand("gcast", "Broadcast any message to groups/users"),
                ])

                if bot_info.id not in CLONES:
                    CLONES.add(bot_info.id)
                    
            except (AccessTokenExpired, AccessTokenInvalid):
                await clonebotdb.delete_one({"token": bot_token})
                logging.info(f"Removed expired or invalid token for bot ID: {bot['bot_id']}")
            except Exception as e:
                logging.exception(f"Error while restarting bot with token {bot_token}: {e}")
            
        await asyncio.gather(*(restart_bot(bot) for bot in bots))
        
    except Exception as e:
        logging.exception("Error while restarting bots.")

# Function to restart the main bot (stop and start again)
async def restart_mainbot():
    try:
        logging.info("Stopping the main bot...")
        await UTTAM.stop()  # Stop the main bot
        logging.info("Main bot stopped.")
        
        logging.info("Restarting the main bot...")
        await UTTAM.start()  # Start the main bot again
        logging.info("Main bot restarted successfully.")
        
    except Exception as e:
        logging.error(f"Error during main bot restart: {e}")

# Function to start the anonymous bot
async def anony_boot():
    try:
        await UTTAM.start()
        try:
            await UTTAM.send_message(int(OWNER_ID), f"**{UTTAM.mention} Is started✅**")
        except Exception as ex:
            LOGGER.info(f"@{UTTAM.username} Started, please start the bot from owner id.")
    
        asyncio.create_task(restart_bots())
        
        await load_clone_owners()
        
    except Exception as ex:
        LOGGER.error(ex)

    for all_module in ALL_MODULES:
        importlib.import_module("UTTAM.modules." + all_module)
        LOGGER.info(f"Successfully imported : {all_module}")

    
    try:
        await UTTAM.set_bot_commands(
            commands=[
                BotCommand("start", "Start the bot"),
                BotCommand("clone", "Make your own reaction bot"),
                BotCommand("cloned", "Get List of all cloned bot"),
                BotCommand("ping", "Check if the bot is alive or dead"),
                BotCommand("id", "Get users user_id"),
                BotCommand("stats", "Check bot stats"),
                BotCommand("gcast", "Broadcast any message to groups/users"),
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")
    
    LOGGER.info(f"@{UTTAM.username} Started.")
    
    await idle()
# This is where we create a task for restarting the main bot asynchronously
async def main():
    # Run the anony_boot function
    await anony_boot()

if __name__ == "__main__":
    try:
        asyncio.run(main())  # Using asyncio.run() for cleaner event loop management
        LOGGER.info("Stopping UTTAM Bot...")
    except Exception as e:
        LOGGER.error(f"Error during bot startup: {e}")
