import dotenv
import os
import disnake  # подключаем библиотеку
from disnake.ext import commands
from disnake.message import Message
dotenv.load_dotenv(".env")
intents = disnake.Intents.all()    # подключаем разрешения
intents.message_content = True
# задаем префикс у команд
bot = commands.Bot(intents=intents)

user_balance = {}

@bot.event
async def on_ready():
    print(f"бот запустился. Привет {bot.user}")


@bot.event
async def on_message(message: Message):
    if message.author == bot.user:   # проверяем написал человек или бот (чтобы бот не отвечал самому себе)
        return
    await message.channel.send("hello world!")
    cost = len(message.content) * 10 #получили буквы скоко их
    if user_balance.get(message.author.id,250) <= cost:
        await message.delete()
        return
    user_balance[message.author.id] = user_balance.get(message.author.id,250) - cost

bot.run(os.getenv("TG_API_TOKEN"))
