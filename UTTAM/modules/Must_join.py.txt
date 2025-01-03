from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from UTTAM import UTTAM as app
from config import UPDATE_CHNL as MUST_JOIN

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://files.catbox.moe/6f9rgp.jpg",
                    caption=(f"**𝐇ᴇʟʟᴏ 𝐁ᴀʙʏ...{msg.from_user.mention},**\n\n**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ]({link}) ᴛᴏ ᴄʜᴇᴀᴋ ᴍʏ ғᴇᴀᴛᴜʀᴇs.**\n\n**ᴀғᴛᴇʀ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ɢᴏ ʙᴀᴄᴋ ᴛᴏ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴛʏᴘᴇ /start ᴀɢᴀɪɴ**"),
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⌯ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ⌯", url=link)]]))
        
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"⌯ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ MUST_JOIN ᴄʜᴀᴛ ⌯: {MUST_JOIN} !")
