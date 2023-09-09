## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID", "20165529"))
API_HASH = getenv("API_HASH", "8df6f871b51473c90c6ada8df53239af")
OWNER_NAME = getenv("OWNER_NAME", "G_7_Rr")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
BOT_IMG = getenv("BOT_IMG")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "CI1ICI")
BOT_USERNAME = getenv("BOT_USERNAME", "N7TTbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "null")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "T7_AU")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "T7_AU")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg")
