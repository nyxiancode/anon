# Copyright (C) 2025 by Delta_Help @ Github, < https://github.com/TheTeamDelta >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Delta © Yukki.

""""
TheTeamDelta is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Delta <https://github.com/TheTeamDelta>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import importlib
from typing import Any

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall, GroupCallNotFound

import config
from config import BANNED_USERS
from DeltaMusic import LOGGER, app, userbot
from DeltaMusic.core.call import Delta
from DeltaMusic.misc import sudo
from DeltaMusic.plugins import ALL_MODULES
from DeltaMusic.utils.database import get_banned_users, get_gbanned


async def init() -> None:
    # Check for at least one valid Pyrogram string session
    if all(not getattr(config, f"STRING{i}") for i in range(1, 6)):
        LOGGER("DeltaMusic").error("Tambahkan sesi string Pyrogram dan coba lagi...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for module in ALL_MODULES:
        importlib.import_module("DeltaMusic.plugins" + module)
    LOGGER("DeltaMusic.plugins").info("Modul yang Diperlukan Berhasil Diimpor.")
    await userbot.start()
    await Delta.start()
    try:
        await Delta.stream_call("https://telegra.ph/file/b60b80ccb06f7a48f68b5.mp4")
    except (NoActiveGroupCall, GroupCallNotFound):
        LOGGER("DeltaMusic").error(
            "[ERROR] - \n\nNyalakan obrolan suara grup dan jangan matikan, jika tidak, saya akan berhenti bekerja. Terima kasih."
        )
        exit()
    except:
        pass
    await Delta.decorators()
    LOGGER("DeltaMusic").info("Bot Musik Delta Berhasil Dimulai")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("DeltaMusic").info("Menghentikan Bot Musik Delta...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    LOGGER("DeltaMusic").info("Menghentikan Bot Musik")
