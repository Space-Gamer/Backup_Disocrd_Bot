from os import getenv
from datetime import datetime

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')
channel_link = getenv('CHANNEL_LINK')
file_name = getenv('FILE_NAME')

guild, channel = channel_link.split('/')[-2:]

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

    active_channel = client.get_guild(int(guild)).get_channel(int(channel))

    # Upload a file
    try:
        with open(file_name, 'rb') as f:
            await active_channel.send(f"Backup on {datetime.utcnow().strftime('%A : %d-%m-%Y %H:%M:%S UTC')}",
                                      file=discord.File(f))
    except FileNotFoundError:
        await active_channel.send(f'File "{file_name}" not found')
    await client.close()

client.run(TOKEN)
