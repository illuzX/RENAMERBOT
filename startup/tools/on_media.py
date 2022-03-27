# (c) illuzX 
##1ea4c6

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
