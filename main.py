from datetime import datetime
import random
import dotenv
import os
import disnake  # подключаем библиотеку
from disnake.ext import commands
from disnake.message import Message

dotenv.load_dotenv(".env")
intents = disnake.Intents.all()  # подключаем разрешения
intents.message_content = True
intents.reactions = True
# задаем префикс у команд
bot = commands.Bot(intents=intents)
TIME_FORMAT = "%x %X"
user_balance = {}
last_use_balance = {}
zarabotok_per_sek = {}
zarabotok_lvl = {}


def has_role_by_id(roles, role_id):
    for role in roles:
        if role_id == role.id:
            return True

    return False


@bot.event
async def on_ready():
    print(f"бот запустился. Привет {bot.user} ")


@bot.event
async def on_raw_reaction_add(payload: disnake.RawReactionActionEvent):
    message_id = payload.message_id
    guild = bot.get_guild(payload.guild_id)
    if message_id == 1497598491793555639:
        if payload.emoji.name == "✅":
            role = guild.get_role(1497604495654387803)
            await payload.member.add_roles(role)
            print(
                f"{datetime.now().strftime(TIME_FORMAT)} - INFO - add role({1497604495654387803}) to user({payload.user_id})")
        return
    role = guild.get_role(1497604495654387803)
    if role in payload.member.roles:
        if message_id == 1501644881733619712:
            if payload.emoji.name == "🟦":
                role = guild.get_role(1497600723917996072)
                await payload.member.add_roles(role)
                print(
                    f"{datetime.now().strftime(TIME_FORMAT)} - INFO - add role({1497600723917996072}) to user({payload.user_id})")

            if payload.emoji.name == "🟩":
                role = guild.get_role(1497603202936340651)
                await payload.member.add_roles(role)
                print(
                    f"{datetime.now().strftime(TIME_FORMAT)} - INFO - add role({1497603202936340651}) to user({payload.user_id})")

            if payload.emoji.name == "🟫":
                role = guild.get_role(1497607613322629130)
                await payload.member.add_roles(role)
                print(
                    f"{datetime.now().strftime(TIME_FORMAT)} - INFO - add role({1497607613322629130}) to user({payload.user_id})")

            if payload.emoji.name == "🟨":
                role = guild.get_role(1497608508902871100)
                await payload.member.add_roles(role)
                print(
                    f"{datetime.now().strftime(TIME_FORMAT)} - INFO - add role({1497608508902871100}) to user({payload.user_id})")
    else:
        await payload.member.send(
            f"Здраствуйте. Перед тем как получить роль поставьте галочку, то что вы прочитали правила сервера.")


@bot.event
async def on_raw_reaction_remove(payload: disnake.RawReactionActionEvent):
    message_id = payload.message_id
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if message_id == 1497598491793555639:
        if payload.emoji.name == "✅":
            role = guild.get_role(1497604495654387803)
            await member.remove_roles(role)
            print(
                f"{datetime.now().strftime(TIME_FORMAT)} - INFO - remove role({1497604495654387803}) from user({payload.user_id})")

    if message_id == 1501644881733619712:
        if payload.emoji.name == "🟦":
            role = guild.get_role(1497600723917996072)
            await member.remove_roles(role)
            print(
                f"{datetime.now().strftime(TIME_FORMAT)} - INFO - remove role({1497600723917996072}) from user({payload.user_id})")

        if payload.emoji.name == "🟩":
            role = guild.get_role(1497603202936340651)
            await member.remove_roles(role)
            print(
                f"{datetime.now().strftime(TIME_FORMAT)} - INFO - remove role({1497603202936340651}) from user({payload.user_id})")

        if payload.emoji.name == "🟫":
            role = guild.get_role(1497607613322629130)
            await member.remove_roles(role)
            print(
                f"{datetime.now().strftime(TIME_FORMAT)} - INFO - remove role({1497607613322629130}) from user({payload.user_id})")

        if payload.emoji.name == "🟨":
            role = guild.get_role(1497608508902871100)
            await member.remove_roles(role)
            print(
                f"{datetime.now().strftime(TIME_FORMAT)} - INFO - remove role({1497608508902871100}) from user({payload.user_id})")


@bot.event
async def on_message(message: Message):
    if message.author == bot.user:  # проверяем написал человек или бот (чтобы бот не отвечал самому себе)
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
        if user_balance.get(message.author.id, 250) < ckolko_tcoinov:
            await message.channel.send("у вас нехватает ткойнов")
            return
        user_balance[message.author.id] = user_balance.get(message.author.id, 250) - ckolko_tcoinov
        user_balance[perevod_comy] = user_balance.get(perevod_comy, 250) + ckolko_tcoinov
        await message.channel.send("Успешно!")
        return

    jokes = ["Блин! сказал слон наступив на колобка", "колобок повесился", "живой уголок на кладбище будка охраника",
             "у пулемётчика нет цели. Есть только ратататата!"]
    if message.content == "joke":
        joke = random.choice(jokes)
        await message.channel.send(joke)
        return

    if message.content == "work":
        zp = random.randint(20, 40)
        user_balance[message.author.id] = user_balance.get(message.author.id, 250) + zp
        await message.channel.send(f"вам начислено {zp} ткойнов")
        return

    if message.content.startswith("buy"):
        if message.content.endswith("vip"):
            if has_role_by_id(message.author.roles, 1515269161184661644):
                await message.channel.send("У вас уже есть vip")
                return
            if user_balance.get(message.author.id, 250) < 2999:
                await message.channel.send(f"Вам не хватает {2999 - user_balance.get(message.author.id, 250)}")
                return

            user_balance[message.author.id] = user_balance.get(message.author.id, 250) - 2999
            guild = message.guild
            role = guild.get_role(1515269161184661644)
            await message.author.add_roles(role)
            await message.channel.send("Вы успешно приобрели vip!")
            return
        if message.content.endswith("upgrade"):
            if user_balance.get(message.author.id, 250) < 100 * (zarabotok_lvl.get(message.author.id,1) ** 1.5):
                await message.channel.send(f"вам не хватает {100 * (zarabotok_lvl.get(message.author.id,1) ** 1.5) - user_balance.get(message.author.id, 250)}")
                return
            user_balance[message.author.id] = user_balance.get(message.author.id, 250) - 100 * (zarabotok_lvl.get(message.author.id,1) ** 1.5)
            zarabotok_lvl[message.author.id] = zarabotok_lvl.get(message.author.id,1) + 1
            zarabotok_per_sek[message.author.id] = zarabotok_per_sek.get(message.author.id, 1) + 1
            await message.channel.send(f"Вы успешно купили upgrade ваш заработок увеличился и теперь составляет {zarabotok_per_sek.get(message.author.id, 1)}")
            return
        return

    if message.content == 'balance':  # команда что бы показввала баланс
        last_use:str = last_use_balance.get(message.author.id,datetime.now().strftime(TIME_FORMAT))
        last_use_balance[message.author.id] = datetime.now().strftime(TIME_FORMAT)
        raznica = datetime.now() - datetime.strptime(last_use,TIME_FORMAT)
        money_offlaine = raznica.total_seconds() * zarabotok_per_sek.get(message.author.id,1)
        user_balance[message.author.id] = user_balance.get(message.author.id,250) + money_offlaine
        print(raznica.total_seconds())
        await message.channel.send(f"Ваш баланс : {user_balance.get(message.author.id, 250)}")
        return

    cost = len(message.content) * 10  # получили буквы скоко их
    if user_balance.get(message.author.id, 250) <= cost:
        await message.delete()
        return
    user_balance[message.author.id] = user_balance.get(message.author.id, 250) - cost


bot.run(os.getenv("TG_API_TOKEN"))
