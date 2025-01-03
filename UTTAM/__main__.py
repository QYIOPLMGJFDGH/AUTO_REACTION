import sys
import asyncio
import importlib
from pyrogram import idle
from pyrogram.types import BotCommand
from config import OWNER_ID
from UTTAM import LOGGER, UTTAM, load_clone_owners
from UTTAM.modules import ALL_MODULES
from UTTAM.modules.Clone import restart_bots


async def anony_boot():
    try:
        await nexichat.start()
        try:
            await nexichat.send_message(int(OWNER_ID), f"**{nexichat.mention} Is started✅**")
        except Exception as ex:
            LOGGER.info(f"@{nexichat.username} Started, please start the bot from owner id.")
    
        asyncio.create_task(restart_bots())
        
        await load_clone_owners()
        
    except Exception as ex:
        LOGGER.error(ex)

    for all_module in ALL_MODULES:
        importlib.import_module("nexichat.modules." + all_module)
        LOGGER.info(f"Successfully imported : {all_module}")

    
    try:
        await nexichat.set_bot_commands(
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
    
    LOGGER.info(f"Bot Started.")
    
    await idle()

    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping UTTAM Bot...")
