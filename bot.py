from vkbottle import Bot
from handlers import labelers

TOKEN = token

bot = Bot(TOKEN)

for labeler in labelers:
    bot.labeler.load(labeler)

bot.run_forever()
