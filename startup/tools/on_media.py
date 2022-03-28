# (c) illuzX 
##1ea4c6
import time
import mimetypes
import traceback
from startup.client import (
    Client
)
from pyrogram import filters
from pyrogram.file_id import FileId
from pyrogram.types import Message
from startup.core.file_info import (
    get_media_file_id,
    get_media_file_size,
    get_media_file_name,
    get_file_type,
    get_file_attr
)
from configs import Config
from startup.core.display import progress_for_pyrogram
from startup.core.db.database import db
from startup.core.db.add import add_user_to_database
from startup.core.handlers.not_big import handle_not_big
from startup.core.handlers.time_gap import check_time_gap
from startup.core.handlers.big_rename import handle_big_rename
import asyncio
from startup.client import Client
from startup.core.db.add import (
    add_user_to_database
)
from pyrogram import (
    filters,
    types
)


@Client.on_message((filters.video | filters.audio | filters.document) & ~filters.channel & ~filters.edited)
async def on_media_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sir :(")
    await add_user_to_database(c, m)
    await asyncio.sleep(3)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="**did u want do Rename This file ?**",
        reply_markup=types.InlineKeyboardMarkup(
            [[types.InlineKeyboardButton("Yes", callback_data="r"),
              types.InlineKeyboardButton("No", callback_data="closeMessage")]]
        ),
        disable_web_page_preview=True,
        reply_to_message_id=m.message_id
    )
