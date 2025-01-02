from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from UTTAM import OWNER, UTTAM


START_BOT = [
    
    [
        InlineKeyboardButton(text="⌯ ❍ᴘᴇɴ 𝖢ᴏϻϻᴧηᴅs ⌯", callback_data="HELP"),
    ],
]


DEV_OP = [
        [InlineKeyboardButton("✙ ʌᴅᴅ ϻє ʙᴀʙу ✙", url=f"http://t.me/{UTTAM.username}?startgroup=botstart")],
        [InlineKeyboardButton("⌯ 𝛅ᴜᴘᴘᴏʀᴛ ⌯", url="https://t.me/PURVI_SUPPORT"),
         InlineKeyboardButton("⌯ 𝖴ᴘᴅᴀᴛᴇs ⌯", url="https://t.me/PURVI_UPDATES")],
        [InlineKeyboardButton("⌯ 𝖧ᴇʟᴘ ᴧηᴅ 𝖢ᴏϻϻᴧηᴅs ⌯", callback_data="HELP")]
]

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


BACK = [
    [
        InlineKeyboardButton(text="⌯ 𝖡ᴧᴄᴋ ⌯", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="⌯ 𝖢ʟᴏɴᴇ ʙᴏᴛ ⌯", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="⌯ 𝖱ᴇᴀᴄᴛɪᴏɴ ʙᴏᴛ ⌯", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="⌯ 𝖡ᴧᴄᴋ ⌯", callback_data="BACK"),
        InlineKeyboardButton(text="⌯ 𝖠ʙᴏᴜᴛ ⌯", callback_data="ABOUT"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="disable_chatbot"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="⌯ 𝛅ᴏᴏɴ ⌯", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="⌯ 𝖡ᴧᴄᴋ ⌯", callback_data="SBACK"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⌯ 𝖡ᴧᴄᴋ ⌯", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="⌯ 𝖧ᴇʟᴘ ᴧηᴅ 𝖢ᴏϻϻᴧηᴅs ⌯", callback_data="HELP"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(text="⌯ ғᴇᴀᴛᴜʀᴇs ⌯", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="⌯ 𝛅ᴜᴘᴘᴏʀᴛ ⌯", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="⌯ 𝖴ᴘᴅᴀᴛᴇs ⌯", url=f"https://t.me/{UPDATE_CHNL}"),
    ],
    [
        InlineKeyboardButton(text="⌯ ❍ᴡɴᴇʀ ⌯", user_id=OWNER),
        InlineKeyboardButton(text="⌯ 𝖧ᴇʟᴘ ᴧηᴅ 𝖢ᴏϻϻᴧηᴅs ⌯", callback_data="HELP")
    ],
]
