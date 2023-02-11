from vkbottle import Bot
from handlers import labelers

TOKEN = "vk1.a.wPRq7JIWA608ZdNPzMwWSQNBiKsVu4ld7OJiXXQ0KLb1lMgZU43SZ2GJxG15H__NWIQumL49hCUnlgTnmcztyNu2r2sA5DqTT6HwoqD1nYJcVxHxREU5JpjyEK6I1zTvsPUfLZ2yvUSyO66BS1cVVkTWcGuKc1Tp2bZlLhSU3zunSEU6RD4c8merDFqZr9caZ69ZE_u44bWu_ZrnvRwsaw"

bot = Bot(TOKEN)

for labeler in labelers:
    bot.labeler.load(labeler)

bot.run_forever()