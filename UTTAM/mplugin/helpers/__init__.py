from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

from UTTAM import OWNER, UTTAM


def is_admins(func: Callable) -> Callable:
    async def non_admin(c: UTTAM, m: Message):
        if m.from_user.id == OWNER:
            return await func(c, m)

        admin = await c.get_chat_member(m.chat.id, m.from_user.id)
        if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await func(c, m)

    return non_admin



from .read import *
from .cowner import *
from .inline import *
