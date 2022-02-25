import discord
from keepAlive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))


keep_alive() 
client.run("OTQ2ODU3MjQ0MTU3NDE1NDU1.Yhkzhg.QQS0749PgO46Un2sOQ9ikeb3jrw")