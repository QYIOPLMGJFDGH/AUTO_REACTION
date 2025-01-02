from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from pyrogram.types import Message
from UTTAM import UTTAM
from UTTAM.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)

@Client.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    reaction_bot = await client.get_me()
    buttons = [
        [InlineKeyboardButton("✙ ʌᴅᴅ ϻє ʙᴀʙу ✙", url=f"http://t.me/{reaction_bot.username}?startgroup=botstart")],
    ]
    photo_url = "https://files.catbox.moe/rdfi4z.jpg"
    await client.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=f"**✦ʜᴇʏ {message.from_user.mention}!!**\n**◆ ɪ'ᴍ ʏᴏᴜʀ ᴄʟᴏɴᴇᴅ ᴀᴜᴛᴏ ʀᴇᴀᴄᴛɪᴏɴ ʙᴏᴛ !!**\n\n**◆ ɪ'ᴍ ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘs, ᴄʜᴀɴɴᴇʟs, ᴀɴᴅ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs ᴡɪᴛʜ ᴀ ʀᴀɴᴅᴏᴍ ᴇᴍᴏᴊɪ..!!**\n\n**◆ 𝖦ᴏ & 𝖢ʟᴏɴᴇ 𝖸ᴏᴜʀ 𝖮ᴡɴ 𝖡ᴏᴛ :-\n     @TPB_REACTION_BOT**",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    
