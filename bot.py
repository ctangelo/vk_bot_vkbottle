from vkbottle import Bot
from handlers import labelers
from config import TOKEN


bot = Bot(TOKEN)

for labeler in labelers:
    bot.labeler.load(labeler)

bot.run_forever()