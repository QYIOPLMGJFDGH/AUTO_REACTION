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







@UTTAM.on_message(filters.command("stats"))
async def stats(cli: Client, message: Message):
    bot_id = (await cli.get_me()).id
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    
    await message.reply_text(
        f"""{(await cli.get_me()).mention} Reaction Bot Stats:

➻ **❍ 𝖢ʜᴀᴛs :** {chats}
➻ **❍ 𝖴sᴇʀs :** {users}"""
    )


from pyrogram.enums import ParseMode

from UTTAM import UTTAM


@UTTAM.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[ᴍᴇssᴀɢᴇ ɪᴅ:]({message.link})** `{message_id}`\n"
    text += f"**[ʏᴏᴜʀ ɪᴅ:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ᴜsᴇʀ ɪᴅ:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴅᴏᴇsɴ'ᴛ ᴇxɪsᴛ.", quote=True)

    text += f"**[ᴄʜᴀᴛ ɪᴅ:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:]({reply.link})** `{reply.id}`\n"
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, ɪs `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
