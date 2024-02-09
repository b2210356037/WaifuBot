import discord
from discord.ext import commands
import os
import random
import aiohttp
from keep_alive9 import keep_alive
import asyncio

#client = discord.Client()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';;', intents=intents)


@bot.slash_command(
  name="waifu",
  description=
  "Tired of boring chats? Add some sassiest waifu pictures right to your Discord."
)
async def waifu(ctx, istek=None):
  try:
    with open(f"waifu{ctx.author}.txt", "r+") as file:
      lines = len(file.readlines())
  except FileNotFoundError:
    with open(f"waifu{ctx.author}.txt", "a+") as file:
      lines = len(file.readlines())
  if (lines >= 50 and ctx.author.id not in prem_users):
    await ctx.respond(
      "You have reached the limit of 50 waifu pictures. Upgrade to a higher tier to enjoy an unlimited supply of sassy waifus!"
    )
  else:
    async with aiohttp.ClientSession() as session:
      if (istek != None):
        if (istek == "raiden"):
          async with aiohttp.ClientSession() as session:
            request = await session.get(
            "https://api.waifu.im/search/?excluded_files=4401" \
          "&excluded_files=3133" \
          "&gif=false" \
          "&included_tags=raiden-shogun" \
          "&is_nsfw=false"
            )
        elif (istek == "marin"):
          async with aiohttp.ClientSession() as session:
            request = await session.get(
            "https://api.waifu.im/search/?excluded_files=4401" \
          "&excluded_files=3133" \
          "&gif=false" \
          "&included_tags=marin-kitagawa" \
          "&is_nsfw=false"
            )
        elif (istek == "mori"):
          async with aiohttp.ClientSession() as session:
            request = await session.get(
            "https://api.waifu.im/search/?excluded_files=4401" \
          "&excluded_files=3133" \
          "&gif=false" \
          "&included_tags=mori-calliope" \
          "&is_nsfw=false"
            )
        elif (istek == "maid"):
          async with aiohttp.ClientSession() as session:
            request = await session.get(
            "https://api.waifu.im/search/?excluded_files=4401" \
          "&excluded_files=3133" \
          "&gif=false" \
          "&included_tags=maid" \
          "&is_nsfw=false"
            )
      else:
        request = await session.get(
            "https://api.waifu.im/search/?excluded_files=4401" \
      "&gif=false" \
      "&is_nsfw=false"\
      "&included_tags = waifu"
        )

    dogjson = await request.json()
    embed = discord.Embed(title="delicious!", color=discord.Color.purple())
    embed.set_image(url=dogjson['images'][0]["url"])

    url = dogjson['images'][0]["url"]
    await asyncio.sleep(0.5)
    await ctx.respond(embed=embed)
    message = await ctx.respond(
      "Would you like to save her? \n :thumbsup: :-1: ")
    thumb_up = "👍"
    thumb_down = "👎"

    async def limit_check(user, reaction):
      try:
        with open(f"waifu{user}.txt", "r+") as file:
          lines = len(file.readlines())
        if (lines >= 50 and user.id not in prem_users):
          file.close()
          await ctx.send(
            f"user {user} has reached limit. Please consider upgrading your tier level."
          )
          return False
        else:
          file.close()
          return True
      except:
        with open("waifuWaifu.bot#2341.txt", "a+") as file:
          file.close()

    await message.add_reaction(thumb_up)
    prevUrl.append(message.id)

    def control(msg, reaction, user):
      if (reaction.msg.id == prevUrl[-1]):
        return True
      else:
        return False

    msgId = message.id

    def check(reaction, user):
      if user != bot and reaction.emoji == thumb_up and reaction.message.id == msgId:
        return True
      else:
        return False

    active = True
    users = ()
    userDict = {}
    while True:
      reaction, user = await bot.wait_for("reaction_add",
                                          check=check,
                                          timeout=360)
      a = await limit_check(user, reaction)
      if (user.id not in userDict.keys() and user.id != 1071756934891446293
          and a):
        userDict[user.id] = 0
      if (reaction.emoji == thumb_up and user.id != 1071756934891446293 and a):
        userDict[user.id] = 1
        fileWrite = open(f"waifu{user}.txt", "a")
        fileWrite.write(f"{url} \n")
        fileWrite.close()
        await asyncio.sleep(0.2)
        await ctx.respond(f"Saved {user}")
    userDict[user.id] = 1


fileWrite = open("waifu.txt", "a")
prevUrl = []


@bot.slash_command(
  name="waifu2",
  description=
  "Tired of boring chats? Add some sassiest waifu pictures right to your Discord."
)
async def waifu2(ctx, istek=None):
  async with aiohttp.ClientSession() as session:
    if (istek != None):
      async with aiohttp.ClientSession() as session:
        request = await session.get(f"https://api.waifu.pics/many/sfw/{istek}")
    if (istek == None):
      async with aiohttp.ClientSession() as session:
        request = await session.get("https://api.waifu.pics/sfw/waifu")

  dogjson = await request.json()
  embed = discord.Embed(title="delicious!", color=discord.Color.purple())
  embed.set_image(url=dogjson["url"])
  url = dogjson["url"]

  await ctx.respond(embed=embed)
  message = await ctx.respond("Would you like to save her? \n :thumbsup: :-1: "
                              )
  thumb_up = "👍"
  thumb_down = "👎"

  await message.add_reaction(thumb_up)

  def control(msg, reaction, user):
    if (reaction.msg.id == prevUrl[-1]):
      return True
    else:
      return False

  msgId = message.id

  def check(reaction, user):
    if user != bot and reaction.emoji == thumb_up and reaction.message.id == msgId:
      return True
    else:
      return False

  userDict = {}
  while True:
    reaction, user = await bot.wait_for("reaction_add",
                                        check=check,
                                        timeout=60)
    if (user.id not in userDict.keys() and user.id != 1071756934891446293):
      userDict[user.id] = 0
    if (reaction.emoji == thumb_up and user.id != 1071756934891446293
        and userDict[user.id] == 0):
      userDict[user.id] = 1
      fileWrite = open(f"waifu{user}.txt", "a")
      fileWrite.write(f"{url} \n")
      fileWrite.close()
      await ctx.respond(f"Saved {user}")
  userDict[user.id] = 1


prem_users = [
  341476571468529664, 959805228138508399, 269158042807959554,
  277423067678900224
]
kelime_dict = {"araba": "tekerliaraç", "merdane": "alet", "uzayyolu": "film"}

@bot.slash_command(name="startgame", description="Starts a new game")
async def startgame(ctx):
    word = random.choice(list(kelime_dict.keys()))
    description = kelime_dict[word]
    await ctx.respond("Game has started!")
    masked_word = '-' * len(word)
    await ctx.send(f"Word description: {description}\n{' '.join(masked_word)}")
    
    points = len(word) * 100
    guessed_letters = set()
    guess_mode = False
    
    message = await ctx.send("Would you like to get a letter? React with 👍")
    await message.add_reaction('👍')
    await message.add_reaction('🅱️')
    
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['👍', '🅱️']

  
    while points > 0 and masked_word != word:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Time's up!")
            return

        if str(reaction.emoji) == '🅱️':
            guess_mode = True
            await message.clear_reactions()
            break
        
        available_indices = [i for i, l in enumerate(word) if masked_word[i] == '-']
        if available_indices:
            index = random.choice(available_indices)
            letter = word[index]
            guessed_letters.add(letter)
            masked_word_list = list(masked_word)
            masked_word_list[index] = letter
            masked_word = ''.join(masked_word_list)
            await message.edit(content=f"Word description: {description}\n{' '.join(masked_word)}")
            points -= 100

    if masked_word == word:
        await ctx.send(f"Congratulations, you guessed the word '{word}'! Your score: {points}")
    elif guess_mode:
        await ctx.send("Enter your guess:")
        while True:
            try:
                guess = await bot.wait_for('message', timeout=30, check=lambda m: m.author == ctx.author)
            except asyncio.TimeoutError:
                await ctx.send("Time's up!")
                return
            
            if guess.content.lower() == word:
                await ctx.send(f"Congratulations, you guessed the word '{word}'! Your score: {points}")
                return
            else:
                await ctx.send("Incorrect guess. Try again:")
    else:
        await ctx.send(f"The word was '{word}'. Better luck next time!")



              
@bot.slash_command(name="hentai", description="Naughty waifus ")
async def hentai(ctx, istek=None):
  channel = ctx.channel
  if (channel.is_nsfw() and ctx.author.id in prem_users):
    async with aiohttp.ClientSession() as session:
      if (istek != None):
        async with aiohttp.ClientSession() as session:
          request = await session.get(
            f"https://api.waifu.im/search/?excluded_files=4401&excluded_files=3133&gif=false&included_tags={istek}&is_nsfw=true"
          )
      elif (istek == None):
        request = await session.get(
          "https://api.waifu.im/search/?excluded_files=4401&excluded_files=3133&gif=false&included_tags=hentai&is_nsfw=true"
        )
    dogjson = await request.json()
    embed = discord.Embed(title="Naughty :hot_face:",
                          color=discord.Color.purple())
    embed.set_image(url=dogjson["images"][0]["url"])
    await ctx.respond(embed=embed)
  else:
    await ctx.respond(
      "Only executed in NSFW channels and by premium users, no responsibility accepted by developer."
    )


@bot.command()
async def fav(ctx, index):
  index = int(index) - 1
  fileWrite = open(f"waifu{ctx.author}.txt", "r")
  lines = fileWrite.readlines()
  url = f"{lines[index]}"
  embed = discord.Embed(title="delicious! :yum: ",
                        color=discord.Color.purple())
  embed.set_image(url=url)
  await ctx.send(embed=embed)
  fileWrite.close()


@bot.command()
async def hentai2(ctx, istek=None):
  async with aiohttp.ClientSession() as session:
    if (istek != None):
      async with aiohttp.ClientSession() as session:
        request = await session.get(f"https://api.waifu.pics/nsfw/{istek}")
    if (istek == None):
      async with aiohttp.ClientSession() as session:
        request = await session.get("https://api.waifu.pics/nsfw/waifu")

  dogjson = await request.json()
  embed = discord.Embed(title="delicious!", color=discord.Color.purple())
  embed.set_image(url=dogjson["url"])
  url = dogjson["url"]

  await ctx.send(embed=embed)
  message = await ctx.send("Would you like to save her? \n :thumbsup: :-1: ")
  thumb_up = "👍"
  thumb_down = "👎"

  await message.add_reaction(thumb_up)

  def control(msg, reaction, user):
    if (reaction.msg.id == prevUrl[-1]):
      return True
    else:
      return False

  msgId = message.id

  def check(reaction, user):
    if user != bot and reaction.emoji == thumb_up and reaction.message.id == msgId:
      return True
    else:
      return False

  userDict = {}
  while True:
    reaction, user = await bot.wait_for("reaction_add",
                                        check=check,
                                        timeout=60)
    if (user.id not in userDict.keys() and user.id != 1071756934891446293):
      userDict[user.id] = 0
    if (reaction.emoji == thumb_up and user.id != 1071756934891446293
        and userDict[user.id] == 0):
      userDict[user.id] = 1
      fileWrite = open(f"waifu{user}.txt", "a")
      fileWrite.write(f"{url} \n")
      fileWrite.close()
      await ctx.send(f"Saved {user}")
  userDict[user.id] = 1


@bot.command()
async def ranfav(ctx):
  fileWrite = open(f"waifu{ctx.author}.txt", "r")
  fileRead = fileWrite.readlines()
  x = len(fileRead)
  url = ""
  y = random.randint(1, x)
  url = fileRead[y]
  embed = discord.Embed(title="delicious! :yum: ",
                        color=discord.Color.purple())
  embed.set_image(url=url)
  await ctx.send(embed=embed)


@bot.slash_command(
  name="genshin",
  description=
  "Tired of boring chats? Add some sassiest genshin waifus right to your Discord."
)
async def genshin(ctx):
  try:
    with open(f"waifu{ctx.author}.txt", "r+") as file:
      lines = len(file.readlines())
  except FileNotFoundError:
    with open(f"waifu{ctx.author}.txt", "a+") as file:
      lines = len(file.readlines())
  if (lines >= 50 and ctx.author.id not in prem_users):
    await ctx.respond(
      "You have reached the limit of 50 waifu pictures. Upgrade to a higher tier to enjoy an unlimited supply of sassy waifus!"
    )
  else:
    async with aiohttp.ClientSession() as session:
      request = await session.get(
        "https://gi-img-api.ak-team.repl.co/api/genshin/character")
    dogjson = await request.json()
    embed = discord.Embed(title="delicious!", color=discord.Color.purple())
    embed.set_image(url=dogjson["url"])
    url = dogjson["url"]
    await asyncio.sleep(0.5)
    await ctx.respond(embed=embed)
    message = await ctx.respond(
      "Would you like to save her? \n :thumbsup: :-1: ")
    thumb_up = "👍"
    thumb_down = "👎"

    async def limit_check(user, reaction):
      try:
        with open(f"waifu{user}.txt", "r+") as file:
          lines = len(file.readlines())
        if (lines >= 50 and user.id not in prem_users):
          file.close()
          await ctx.send(
            f"user {user} has reached limit. Please consider upgrading your tier level."
          )
          return False
        else:
          file.close()
          return True
      except:
        with open("waifuWaifu.bot#2341.txt", "a+") as file:
          file.close()

    await message.add_reaction(thumb_up)

    def control(msg, reaction, user):
      if (reaction.msg.id == prevUrl[-1]):
        return True
      else:
        return False

    msgId = message.id

    def check(reaction, user):
      if user != bot and reaction.emoji == thumb_up and reaction.message.id == message.id:
        return True
      else:
        return False

    active = True
    users = ()
    userDict = {}
    while True:
      reaction, user = await bot.wait_for("reaction_add",
                                          check=check,
                                          timeout=360)
      a = await limit_check(user, reaction)
      if (user.id not in userDict.keys() and user.id != 1071756934891446293
          and a):
        userDict[user.id] = 0
      if (reaction.emoji == thumb_up and user.id != 1071756934891446293 and a):
        userDict[user.id] = 1
        fileWrite = open(f"waifu{user}.txt", "a")
        fileWrite.write(f"{url} \n")
        fileWrite.close()
        await asyncio.sleep(0.2)
        await ctx.respond(f"Saved {user}")
    userDict[user.id] = 1


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await ctx.guild.kick(member)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)


@bot.command()
async def hi(ctx):
  await ctx.send("hello")


while __name__ == '__main__':
  try:
    keep_alive()
    bot.run(os.getenv('TOKEN'))
  except discord.errors.HTTPException as e:
    print(e)
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system('kill 1')

#keep_alive()
#bot.run(os.getenv("TOKEN"))

#dirtbot but human
