import discord
client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity = discord.Game(name = "Logging whatever you say"))
@client.event
async def on_message(message):
    channel = client.get_channel("Replace this with the ID of the Audit channel")
    sender_id = message.author.id
    message_content = message.content
    if message.author == client.user:
        return
    else:  
        try:  
            await channel.send("<@" + str(sender_id) + "> said " + message_content)
        except AttributeError:
            await message.channel.sent("I was unable to log the comment")
    
client.run("Token here, because mine isn't for your eyes")
    
