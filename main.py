import discord
from keepAlive import keep_alive
codeFile = open("botCode.txt", "r", 59)
code = codeFile.read(59)
codeFile.close()

client = discord.Client()

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))


keep_alive() 
client.run(code)