#sentry-bot
Sentry bot is my second Discord bot, made using Python this time. It is pretty much the successor to kbot, and it is better in pretty much almost every way.
Some features include:
    *Lots of commands compared to kbot
    *Some commands send images or video
    *Some commands randomly select from a long list of messages
    *Built-in coronavirus tracker, with data scraped from world-o-meters. This is my first time making a web scraper

This repo is unlikely to continue. If I ever want to make another Discord bot in the future, I'll probably just start from scratch (for no specific reason).

If you want to use the bot for yourself for whatever reason:

*Install these libraries:
    discord.py (discord)
    BeautifulSoup (bs4)
    dotenv (python-dotenv)

*Make a .env file in the directory with:
    *DISCORD_TOKEN = your-bot-token
    *DISCORD_PREFIX = your-prefix
    *DISCORD_OWNER = your-discord-id
