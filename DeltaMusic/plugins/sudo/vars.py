# Copyright (C) 2025 by Delta_Help @ Github, < https://github.com/TheTeamDelta >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Delta © Yukki.

""""
TheTeamDelta is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Delta <https://github.com/TheTeamDelta>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio

from pyrogram import filters

import config
from strings import get_command
from DeltaMusic import app
from DeltaMusic.misc import SUDOERS
from DeltaMusic.utils.database.memorydatabase import get_video_limit
from DeltaMusic.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text("Silakan tunggu... Mendapatkan variabel konfigurasi Anda...")
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[repo]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "ya"
    else:
        ass = "tidak"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "ya"
    else:
        pvt = "tidak"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "ya"
    else:
        a_sug = "tidak"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "ya"
    else:
        down = "tidak"

    if not config.GITHUB_REPO:
        git = "tidak"
    else:
        git = f"[repo]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "tidak"
    else:
        start = f"[gambar]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "tidak"
    else:
        s_c = f"[channel]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "tidak"
    else:
        s_g = f"[dukungan]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "tidak"
    else:
        token = "ya"
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        sotify = "tidak"
    else:
        sotify = "ya"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**Variabel Konfigurasi Bot Musik:**

**<u>Variabel Dasar:</u>**
**Nama_Bot_Musik** : `{bot_name}`
**Batas_Durasi** : `{play_duration} menit`
**Batas_Durasi_Unduh_Lagu** :` {song} menit`
**ID_Pemilik** : `{owner_id}`
    
**<u>Variabel Repositori:</u>**
**Repo_Utama** : `{up_r}`
**Cabang_Utama** : `{up_b}`
**Repo_GitHub** :` {git}`
**Token_Git**:` {token}`


**<u>Variabel Bot:</u>**
**Asisten_Keluar_Otomatis** : `{ass}`
**Waktu_Asisten_Keluar** : `{auto_leave} detik`
**Mode_Saran_Otomatis** :` {a_sug}`
**Waktu_Saran_Otomatis** : `{auto_sug} detik`
**Pembersihan_Unduhan_Otomatis** : `{down}`
**Mode_Bot_Pribadi** : `{pvt}`
**Tidur_Edit_YouTube** : `{yt_sleep} detik`
**Tidur_Edit_Telegram** :` {tg_sleep} detik`
**Mode_Pembersihan** : `{cm} menit`
**Batas_Stream_Video** : `{v_limit} obrolan`
**Batas_Playlist_Server** :` {playlist_limit}`
**Batas_Ambil_Playlist** :` {fetch_playlist}`

**<u>Variabel Spotify:</u>**
**ID_Klien_Spotify** :` {sotify}`
**Rahasia_Klien_Spotify** : `{sotify}`

**<u>Variabel Ukuran Putar:</u>**
**Batas_Ukuran_File_Audio_TG** :` {tg_aud}`
**Batas_Ukuran_File_Video_TG** :` {tg_vid}`

**<u>Variabel Tambahan:</u>**
**Channel_Dukungan** : `{s_c}`
**Grup_Dukungan** : ` {s_g}`
**URL_Gambar_Mulai** : ` {start}`
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
