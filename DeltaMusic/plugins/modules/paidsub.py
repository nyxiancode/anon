# Copyright (C) 2025 by Delta_Help @ Github, < https://github.com/TheTeamDelta >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Delta © Yukki.

""""
TheTeamDelta is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Delta <https://github.com/TheTeamDelta>

This program is free software: you can redistribute it and can modify
as you want atau you can collabe if you have new ideas.
"""


import asyncio
from DeltaMusic import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait
from DeltaMusic.core.mongo import db as delta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DeltaMusic.utils.database import get_served_users, get_served_chats


OWNER_ID = 1025855210
