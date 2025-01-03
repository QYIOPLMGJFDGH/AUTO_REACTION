from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from pyrogram.types import Message
from UTTAM import UTTAM

@UTTAM.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    reaction_bot = await client.get_me()
    buttons = [
        [InlineKeyboardButton("Join 👋", url="https://t.me/BABY09_WORLD")],
    ]
    await client.send_message(
        chat_id=message.chat.id,
        text="""𝐇𝐞𝐲, 𝐈 𝐚𝐦 𝐚 𝐚𝐮𝐭𝐨 𝐫𝐞𝐚𝐜𝐭𝐢𝐨𝐧 𝐛𝐨𝐭!

Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢᴇᴛ ᴇᴍᴏᴊɪ ʀᴇᴀᴄᴛɪᴏɴs!
Tᴏ jᴏɪɴ, clɪcᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ:

𝐔𝐒𝐄𝐅𝐔𝐋 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒:
/start - Sᴛᴀʀᴛ ʏᴏᴜʀ ʙᴏᴛ ᴀɴᴅ ɢᴇᴛ ʜᴇʟᴘ ɪɴғᴏ
/mybot - Lɪsᴛ ᴏғ ʏᴏᴜʀ ᴄʟᴏɴᴇᴅ ʙᴏᴛ
/clone {bot_token} - Clᴏɴᴇ ᴀ boᴛ ᴡɪᴛʜ ᴛʜᴇ ᴛᴏᴋᴇɴ @BotFather

𝐎𝐖𝐍𝐄𝐑 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒:
/cloned - Lɪsᴛ ᴏғ ᴀʟʟ cloɴᴇᴅ ʙᴏᴛ ɪɴ ᴛʜᴇ sʏsᴛᴇᴍ
/del {username} - Dᴇʟᴇᴛᴇ ᴀ ᴄʟᴏɴᴇᴅ ʙᴏᴛ ɪɴ ᴛʜᴇ sʏsᴛᴇᴍ

𝐍ᴏᴛᴇ: Tʜɪs ʙᴏᴛ ɪs ᴄᴏsᴛ-ғʀᴇᴇ ᴛᴏ ᴜsᴇ!

Tᴏ jᴏɪɴ, clɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ:""",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    
