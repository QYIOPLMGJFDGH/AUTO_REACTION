import asyncio
import logging
import random
import time
import psutil
import config
import os
from UTTAM import _boot_
from UTTAM import get_readable_time
from UTTAM import UTTAM
from datetime import datetime
from pymongo import MongoClient
from pyrogram.enums import ChatType
from pyrogram import Client, filters
from UTTAM import db
from config import OWNER_ID, MONGO_URL, OWNER_USERNAME
from pyrogram.errors import FloodWait, ChatAdminRequired
from UTTAM.database.chats import get_served_chats, add_served_chat
from UTTAM.database.users import get_served_users, add_served_user
from UTTAM.database.clonestats import get_served_cchats, get_served_cusers, add_served_cuser, add_served_cchat
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from UTTAM import OWNER, UTTAM



PNG_BTN = [
    [
        InlineKeyboardButton(text="⌯ ❍ᴘᴇɴ 𝖢ᴏϻϻᴧηᴅs ⌯", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(
            text="⌯ ᴄʟσsє ⌯",
            callback_data="CLOSE",
        ),
    ],
]




IMG = [
    "https://files.catbox.moe/qej5mx.jpg",
    "https://files.catbox.moe/3u8g3w.jpg",
    "https://files.catbox.moe/e7q55f.jpg",
    "https://files.catbox.moe/ezpnd2.jpg",
    "https://files.catbox.moe/99wj12.jpg",
]


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    UP = f"{get_readable_time((bot_uptime))}"
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"
    return UP, CPU, RAM, DISK


@UTTAM.on_message(filters.command("ping"))
async def ping(client: Client, message: Message):
    bot_id = client.me.id
    start = datetime.now()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"✦ » ʜᴇʟʟᴏ вᴀвʏ !!\n{(await client.get_me()).mention}  ɪs ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ ᴡɪᴛʜ ᴀ ᴘɪɴɢ oғ\n\n**➥** `{ms}` ms\n**➲ ᴄᴘᴜ:** {CPU}\n**➲ ʀᴀᴍ:** {RAM}\n**➲ ᴅɪsᴋ:** {DISK}\n**➲ ᴜᴘᴛɪᴍᴇ »** {UP}\n\n<b>✦ » 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [𝖯ᴜʀᴠɪ 𝖡ᴏᴛs](t.me/PURVI_SUPPORT)</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_cuser(bot_id, message.from_user.id)
        await add_served_user(message.from_user.id)
    else:
        await add_served_cchat(bot_id, message.chat.id)
        await add_served_chat(message.chat.id)
