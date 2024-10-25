import discord
from discord.ext import commands
from discord import app_commands
import asyncio
# Enable intents (necessary for receiving messages)
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
# A dictionary to store the data
data_storage = {}
# Event: The bot is ready and synchronizes the slash commands
@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready!')
    await bot.tree.sync()
# /import command to save a name and associated data
@bot.tree.command(name="import")
async def import_data(interaction: discord.Interaction, name: str, data: str):
    """
      Imports data under a specific name.
    """
    # Save data under the entered name
    data_storage[name] = data
    await interaction.response.send_message(f'Data saved under the name "{name}"!')
# /list command to display all stored names
@bot.tree.command(name="list")
async def list_data(interaction: discord.Interaction):
    """
    Displays all saved names.
    """
    if data_storage:
        name_list = "\n".join(data_storage.keys())
        await interaction.response.send_message(f'Stored names:\n{name_list}')
    else:
        await interaction.response.send_message('No data available!')
# /export command to export the stored data for a specific name
@bot.tree.command(name="export")
async def export_data(interaction: discord.Interaction, name: str):
    """
    Returns the data for the entered name.
    """
    if name in data_storage:
        await interaction.response.send_message(f'Datas for "{name}": {data_storage[name]}')
    else:
        await interaction.response.send_message(f'No datas for "{name}" found!')
# /delete command to delete data under a specific name
@bot.tree.command(name="delete")
async def delete_data(interaction: discord.Interaction, name: str):
    """
    Deletes the data for the specified name.
    """
    if name in data_storage:
        del data_storage[name]
        await interaction.response.send_message(f'Data for "{name}" has been deleted!')
    else:
        await interaction.response.send_message(f'No Datas for "{name}" found!')
# /help command to display a list of available commands
@bot.tree.command(name="help")
async def help_command(interaction: discord.Interaction):
    """
    Shows an overview of the available commands.
    """
    help_text = """
    **Verfügbare Befehle:**
    `/import <name> <data>` - Stores data under a specific name.
    `/list` - Shows a list of all saved names.
    `/export <name>` - Outputs the stored data for the specified name.
    `/delete <name>` - Deletes the data for the specified name.
    `/help` - shows you the instructions
    """
    await interaction.response.send_message(help_text)
# Starts the bot with the specified token
bot.run(" Bot-token")
