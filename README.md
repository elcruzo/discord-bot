# Discord Bot - Tengo

Welcome to this repository containing the source for Tengo - Your Discord Bot!

## Description
Tengo is a Discord bot written in Python using the discord.py library. This bot provides various functionalities, including greeting users, sending personal messages, and fetching real-time stock prices from the Yahoo Finance API.

## Getting Started
To use the Tengo Discord bot, you need to set up a Discord application and bot, obtain your bot's token, and install the necessary dependencies. Follow these steps to get started:

1. Create a Discord application and bot:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on "New Application" and give it a name (e.g., ElCruzo).
   - In the "Bot" section, click "Add Bot" to create a bot user.
   - Under the "TOKEN" section, click "Copy" to copy your bot token.

2. Clone the repository to your local machine:
   ```
   git clone https://github.com/elcruzo/discord-bot.git
   ```

3. Create a `.env` file in the project directory and add your Discord bot token:
   ```
   TOKEN=your_bot_token_here
   ```

4. Install the required Python libraries using pip:
   ```
   pip install discord.py pandas-datareader python-dotenv
   ```

5. Run the bot script:
   ```
   python index.py
   ```

## Features
### 1. Greeting Users
The bot responds with a greeting when someone mentions `$hello`.

### 2. Sending Personal Messages
The bot can send a personal message to the user when they send `$personal`.

### 3. Fetching Stock Prices
The bot can fetch real-time stock prices from Yahoo Finance when a user sends `$stockprice <ticker>`. Replace `<ticker>` with the stock symbol you want to check.

## Bot Commands
- `$hello`: Receive a greeting from the bot.
- `$personal`: Get a personal message from the bot.
- `$stockprice <ticker>`: Fetch the real-time stock price for the specified stock symbol.

## Events
- The bot announces its connection to the server when it is started.
- When a new member joins the server, the bot sends them a welcome message.

## License
This Discord bot is open-source software licensed under the [MIT License](LICENSE).

## Author
[ElCruzo](https://github.com/elcruzo/)

---

Enjoy using Tengo, YOU Discord bot :), and feel free to contribute to its development or customize it to suit your needs!
