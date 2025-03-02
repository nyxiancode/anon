# Copyright (C) 2025 by Delta_Help @ Github, < https://github.com/TheTeamDelta >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Delta © Yukki.

""""
TheTeamDelta is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Delta <https://github.com/TheTeamDelta>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import speedtest
from pyrogram import filters
from pyrogram.types import Message
from strings import get_command
from DeltaMusic import app
from DeltaMusic.misc import SUDOERS
from DeltaMusic.utils.decorators.language import language

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m, _):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit_text("<b>⬇️ Menjalankan Tes Kecepatan Unduh ...</b>")
        test.download()
        m = m.edit_text("<b>⬆️ Menjalankan Tes Kecepatan Unggah ...</b>")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit_text("<b>📤 Membagikan Hasil SpeedTest ...</b>")
    except Exception as e:
        return m.edit_text(f"<code>{e}</code>")
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
@language
async def speedtest_function(client, message: Message, _):
    m = await message.reply_text("🚀 Menjalankan Tes Kecepatan ...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m, _)
    output = _["server_1"].format(
        result["client"]["isp"],
        result["client"]["country"],
        result["server"]["name"],
        result["server"]["country"],
        result["server"]["cc"],
        result["server"]["sponsor"],
        result["server"]["latency"],
        result["ping"],
    )
    msg = await message.reply_photo(photo=result["share"], caption=output)
    await m.delete()
