import yaml
import logging
import asyncio
from sys import exit
from os import path, mkdir

import discord
from discord.ext import commands

# load configuration file to dictionary
try:
    with open("../config.yaml", "r") as configFile:
        config = yaml.load(configFile, Loader=yaml.SafeLoader)
except FileNotFoundError:
    print("Configuration file 'config.yaml' not found in root directory. Did you run the setup script?")
    exit(1)


# setup logging
botLogger = logging.getLogger("discord")
if (config["debug_mode"]):
    botLogger.setLevel(logging.DEBUG)
else:
    botLogger.setLevel(logging.INFO)

if (not path.exists("../logs/")):
    mkdir("../logs/")

fileHandler = logging.FileHandler(filename="../logs/EduBot.log", encoding="utf-8", mode="a+")
fileHandler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
botLogger.addHandler(fileHandler)


# initialize bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.start(config["api_token"]))
except KeyboardInterrupt:
    loop.run_until_complete(bot.close())
finally:
    loop.stop()