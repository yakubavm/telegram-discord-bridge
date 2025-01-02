# Telegram-Discord Bridge

A Python script that bridges communication between Telegram and Discord by transferring messages, media, and more.

## Features

- Transfers text messages from Telegram to Discord.
- Sends media files (images, videos, etc.) from Telegram to Discord.
- Handles Telegram replies, polls, geolocations, and contacts.
- Easy to configure and use.

## Requirements

- **Python**: Version 3.8 or higher.
- **Telegram API Credentials**: `api_id` and `api_hash` from [Telegram Developer Portal](https://my.telegram.org/apps).
- **Discord Bot Token**: Generated via the [Discord Developer Portal](https://discord.com/developers/applications).
- Installed Python packages: `telethon` and `discord.py`.

## Installation

1. Download the script:
   ```bash
   cd telegram-discord-bridge
   ```

2. Install the required Python libraries:
   ```bash
   pip install telethon discord.py
   ```

3. Configure the script by editing the following variables:
   ```python
   TELEGRAM_API_ID = 'your_telegram_api_id'
   TELEGRAM_API_HASH = 'your_telegram_api_hash'
   TELEGRAM_CHANNEL = 'your_channel_or_chat_username'

   DISCORD_TOKEN = 'your_discord_bot_token'
   DISCORD_CHANNEL_ID = 123456789012345678  # Replace with your Discord channel ID
   ```

## Usage

1. Run the script:
   ```bash
   python script_name.py
   ```
2. The bot will monitor the specified Telegram channel or chat and transfer messages and content to the Discord channel.

## Configuration Example

Replace placeholders in the script with your actual credentials:

```python
# Telegram settings
TELEGRAM_API_ID = '123456'
TELEGRAM_API_HASH = 'abcdef1234567890abcdef1234567890'
TELEGRAM_CHANNEL = 'example_channel'

# Discord settings
DISCORD_TOKEN = 'your_discord_bot_token'
DISCORD_CHANNEL_ID = 987654321098765432
```

## Troubleshooting

- **Error: Failed to find Discord channel.**
  - Ensure that your Discord bot has the necessary permissions to access the specified channel.

- **Error: Failed to download media.**
  - Check if the Telegram client can download media and verify sufficient storage is available.

- **Bot does not transfer messages.**
  - Double-check the Telegram channel username and Discord channel ID.

## Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, or create pull requests to improve the script.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
