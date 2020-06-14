import discord
client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity = discord.Game(name = "*help|Logging whatever you say"))
@client.event
async def on_message(message):
    channel = client.get_channel(721085548868927560)
    sender_id = message.author.id
    message_content = message.content
    if message.author == client.user:
        return
    else:  
        try:  
            await channel.send("<@" + str(sender_id) + "> said " + message_content)
        except AttributeError:
            await message.channel.sent("I was unable to log the comment")
    
client.run("NzIxMDg0MTEzODM0MDgyMzU2.XuPX7w.7kVNxWxfTjaM-4Xi_tymHmy56wY")
    