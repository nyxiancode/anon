# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Menghubungkan ke Database Mongo Anda...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Alexa
    LOGGER(__name__).info("Terhubung ke Database Mongo Anda.")
except:
    LOGGER(__name__).error("Gagal terhubung ke Database Mongo Anda.")
    exit()

## Database For Broadcast Subscription By Team Alexa
MONGODB_CLI = AsyncIOMotorClient(MONGO_DB_URI)
db = MONGODB_CLI["subscriptions"]
