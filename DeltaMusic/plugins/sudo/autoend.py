# Copyright (C) 2025 by Delta_Help @ Github, < https://github.com/TheTeamDelta >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Delta © Yukki.

""""
TheTeamDelta is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Delta <https://github.com/TheTeamDelta>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram import filters

import config
from strings import get_command
from DeltaMusic import app
from DeltaMusic.misc import SUDOERS
from DeltaMusic.utils.database import autoend_off, autoend_on
from DeltaMusic.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**Penggunaan:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Auto end stream diaktifkan.\n\nAsisten akan secara otomatis meninggalkan video chat setelah beberapa menit ketika tidak ada yang mendengarkan dengan pesan peringatan."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Auto end stream dinonaktifkan.")
    else:
        await message.reply_text(usage)
