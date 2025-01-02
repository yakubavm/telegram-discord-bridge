import asyncio
from telethon import TelegramClient, events
import discord
from discord.ext import commands

# Telegram settings
TELEGRAM_API_ID = 'your_telegram_api_id'
TELEGRAM_API_HASH = 'your_telegram_api_hash'
TELEGRAM_CHANNEL = 'your_channel_or_chat_username'

# Discord settings
DISCORD_TOKEN = 'your_discord_bot_token'
DISCORD_CHANNEL_ID = 123456789012345678  # Discord channel ID

# Initialize Telegram client
telegram_client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)

# Initialize Discord bot
intents = discord.Intents.default()
intents.messages = True
discord_bot = commands.Bot(command_prefix='!', intents=intents)

@telegram_client.on(events.NewMessage(chats=TELEGRAM_CHANNEL))
async def telegram_to_discord(event):
    """Transfer messages from Telegram to Discord"""
    discord_channel = discord_bot.get_channel(DISCORD_CHANNEL_ID)

    if not discord_channel:
        print("Failed to find Discord channel.")
        return

    # Transfer text (if any)
    if event.message.message:
        await discord_channel.send(f"**Message from Telegram:**\n{event.message.message}")

    # Transfer media files
    if event.message.media:
        file_path = await event.message.download_media()
        if file_path:
            await discord_channel.send(file=discord.File(file_path))
        else:
            print("Failed to download media.")

    # Transfer links or replies
    if event.message.reply_to_msg_id:
        original_message = await event.message.get_reply_message()
        if original_message:
            await discord_channel.send(f"**This is a reply to the message:**\n{original_message.message}")

    # Transfer other types of messages
    if event.message.poll:
        poll_question = event.message.poll.question
        options = "\n".join([f"- {o.text}" for o in event.message.poll.options])
        await discord_channel.send(f"**Poll from Telegram:**\n**{poll_question}**\n{options}")
    elif event.message.geo:
        geo = event.message.geo
        await discord_channel.send(f"**Geolocation:**\nLatitude: {geo.lat}, Longitude: {geo.long}")
    elif event.message.contact:
        contact = event.message.contact
        await discord_channel.send(f"**Contact:**\nName: {contact.first_name} {contact.last_name or ''}\nPhone: {contact.phone}")

@discord_bot.event
async def on_ready():
    """Event triggered when Discord bot starts"""
    print(f'Bot connected as {discord_bot.user}')
    await telegram_client.start()  # Start Telegram client
    print("Telegram client connected.")
    asyncio.create_task(telegram_client.run_until_disconnected())

# Start Discord bot
async def main():
    await discord_bot.start(DISCORD_TOKEN)

asyncio.run(main())
