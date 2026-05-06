import random
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
    print(f"бот запустился. Привет {bot.user} ")
 # random.choice(список шуток) - достает рандомную шутку из списка шуток список шуток надо сделать!!!!!

@bot.event
async def on_message(message: Message):
    if message.author == bot.user:   # проверяем написал человек или бот (чтобы бот не отвечал самому себе)
        return

    if message.content.startswith("perevod"):
        args = message.content.split(" ")
        if len(args) != 3:
            await message.channel.send("Неправильное количество аргрументов")
            return
        perevod_comy = int(args[1])
        ckolko_tcoinov = int(args[2])
        if ckolko_tcoinov < 0:
            await message.channel.send("братан ну не надо дюпать")
            return
        if user_balance.get(message.author.id,250) < ckolko_tcoinov:
            await message.channel.send("у вас нехватает ткойнов")
            return
        user_balance[message.author.id] = user_balance.get(message.author.id,250) - ckolko_tcoinov
        user_balance[perevod_comy] = user_balance.get(perevod_comy,250) + ckolko_tcoinov
        await message.channel.send("Успешно!")
        return


    jokes = ["Блин! сказал слон наступив на колобка", "колобок повесился", "живой уголок на кладбище будка охраника",
             "у пулемётчика нет цели. Есть только ратататата!"]
    if message.content == "joke":
        joke = random.choice(jokes)
        await message.channel.send(joke)
        return

    if message.content == "work":
        zp = random.randint(20,40)
        user_balance[message.author.id] = user_balance.get(message.author.id,250) + zp
        await message.channel.send(f"вам начислено {zp} ткойнов")
        return

    if message.content == 'balance':  # команда что бы показввала баланс
        await message.channel.send(f"Ваш баланс : {user_balance.get(message.author.id, 250)}")
        return

    cost = len(message.content) * 10 #получили буквы скоко их
    if user_balance.get(message.author.id,250) <= cost:
        await message.delete()
        return
    user_balance[message.author.id] = user_balance.get(message.author.id,250) - cost



bot.run(os.getenv("TG_API_TOKEN"))
