import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="say", description="Send a message as the bot")
@app_commands.describe(message="What the bot should say")
async def say(interaction: discord.Interaction, message: str):
    if interaction.user.id != ,<the user id you want the bot to be able to be used by>:
        await interaction.response.send_message("You don't have permission to use this.", ephemeral=True)
        return
    await interaction.response.send_message("Got it!", ephemeral=True, delete_after=1)
    await interaction.channel.send(message)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")

client.run("<bot token>")
