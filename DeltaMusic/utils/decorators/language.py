# Copyright (C) 2025 by Delta_Help @ Github, < https://github.com/TheTeamDelta >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Delta © Yukki.

""""
TheTeamDelta is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Delta <https://github.com/TheTeamDelta>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from strings import get_string
from DeltaMusic.misc import SUDOERS
from DeltaMusic.utils.database import get_lang, is_commanddelete_on, is_maintenance
from DeltaMusic import app
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message


def language(mystic):
    async def wrapper(_, message: Message, **kwargs):
        if await is_maintenance() is False:
            if message.from_user and message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    "» Bot sedang dalam pemeliharaan untuk sementara waktu, silakan kunjungi obrolan dukungan untuk mengetahui alasannya."
                )
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("id")
        
        # Check if the user is an anonymous admin
        if message.from_user:
            member = await app.get_chat_member(message.chat.id, message.from_user.id)
            if member.status == ChatMemberStatus.ADMINISTRATOR and member.user.is_anonymous:
                return await message.reply_text("Anda terdeteksi sebagai admin anonim, silakan gunakan akun biasa.")
        
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    "» Bot sedang dalam pemeliharaan untuk sementara waktu, silakan kunjungi obrolan dukungan untuk mengetahui alasannya.",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("id")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("id")
        return await mystic(_, message, language)

    return wrapper
