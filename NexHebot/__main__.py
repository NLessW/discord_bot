import os
from NexHebot.bot import bot, load_cogs

load_cogs(bot)
bot.run(os.environ["token"])
