import random
from pyrogram import Client, filters
from pyrogram.types import Message
from UTTAM import UTTAM

# List of reactions
reactions = ["👍", "👎", "❤️", "😂", "🤯", "😮", "🤔", "😢", "🔥", "💩", "❤️‍🔥", "🕊️", "🥰", "🗿", "💯", "😎"]


@UTTAM.on_message(filters.text)
async def react_to_message(client: Client, message: Message):
    emoji = random.choice(reactions)
    await message.react(emoji)
