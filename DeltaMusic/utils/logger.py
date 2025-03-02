# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

from pyrogram.enums import ParseMode

from config import LOG_GROUP_ID
from DeltaMusic.utils.database import is_on_off
from DeltaMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} 𝖫𝗈𝗀 𝖯𝖾𝗋𝗆𝖺𝗂𝗇𝖺𝗇</b>

<b>𝖨𝖣 𝖢𝗁𝖺𝗍 :</b> <code>{message.chat.id}</code>
<b>𝖭𝖺𝗆𝖺 𝖢𝗁𝖺𝗍 :</b> {message.chat.title}
<b>𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝖢𝗁𝖺𝗍 :</b> @{message.chat.username}

<b>𝖨𝖣 𝖯𝖾𝗇𝗀𝗀𝗎𝗇𝖺 :</b> <code>{message.from_user.id}</code>
<b>𝖭𝖺𝗆𝖺 𝖯𝖾𝗇𝗀𝗀𝗎𝗇𝖺 :</b> {message.from_user.mention}
<b>𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝖯𝖾𝗇𝗀𝗀𝗎𝗇𝖺 :</b> @{message.from_user.username}

<b>𝖯𝖾𝗋𝗍𝖺𝗇𝗒𝖺𝖺𝗇 :</b> {message.text.split(None, 1)[1]}
<b>𝖩𝖾𝗇𝗂𝗌 𝖲𝗍𝗋𝖾𝖺𝗆 :</b> {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
