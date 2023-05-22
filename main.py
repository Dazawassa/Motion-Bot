import discord #imports the library for Discord. If this is removed the bot is no longer a bot.

TOKEN = "" #Token for the Discord bot. Should be hidden but honestly it's too much work.

Client = discord.Client() #Sets up the client.

#This just prints out a message stating that the bot is running. Can be removed and won't kill the program but it helps with debugging.
@Client.event
async def on_ready():
    print("{0.user} is online".format(Client))

#This is the code that checks if motion is typing. Took me an hour to even find documentation on how this function worked because Discord changed it and never told anyone because they are assholes.
@Client.event #Discord staff weigh 450KG and dance around a water bottle to 2010s rap music.
async def on_typing(channel, user, when):
    if user.id == 964464586923311124: #Motions user ID. Again should be obfuscated but can't be asked. change this to any user ID and it will work for different people.
        await channel.send(f"<@{user.id}> https://cdn.discordapp.com/attachments/130528833731428353/964404034947674132/caption.gif") #Pings Motion with the gif

Client.run(TOKEN)