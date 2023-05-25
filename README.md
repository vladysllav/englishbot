# English Skills Telegram Bot

A Telegram bot built with Python that checks English language skills.

## Description

The English Skills Telegram Bot is designed to assist users in evaluating their English language skills. It analyzes user messages and provides feedback on their English proficiency. This bot is built using Python and integrates with the Telegram Bot API.

## Features

- Check English language skills based on user input
- Provide feedback on English proficiency
- Easy setup and usage

## Installation

1. Clone the repository:

   ```shell
   git clone git@github.com:vladysllav/englishbot.git
   ```

2. Install the required dependencies using Poetry:

   ```shell
   cd englishbot/
   poetry install
   ```

3. Create a `.env` file based on the `.env.example` file:

   ```shell
   cp .env.example .env
   ```

   Update the `.env` file with your actual Telegram bot token.

## Usage

To start the English Skills Telegram Bot, run the following command:

```shell
poetry run python bot.py
```

The bot will be up and running, ready to evaluate users' English skills.
