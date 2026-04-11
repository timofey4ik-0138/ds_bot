import dotenv
import os
import disnake  # подключаем библиотеку
from disnake.ext import commands
from disnake.message import Message
dotenv.load_dotenv(".env")
intents = disnake.Intents.all()    # подключаем разрешения
intents.message_content = True
# задаем префикс у команд`
bot = commands.Bot(intents=intents)



@bot.event
async def on_ready():
    print(f"бот запустился. Привет {bot.user}")


@bot.event
async def on_message(message: Message):
    if message.author == bot.user:   # проверяем написал человек или бот (чтобы бот не отвечал самому себе)
        return
    await message.channel.send("hello world!")

bot.run(os.getenv("TG_API_TOKEN"))
