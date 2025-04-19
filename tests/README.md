# LexTTRPGBot

LexTTRPGBot is a Discord-integrated, ChatGPT-powered, story-driven 
TTRPG bot designed for immersive collaborative roleplaying. 
It allows you and your friends to create and control multiple 
characters and interact with an AI Game Master named **Lex**.

Built with:
- Discord.py
- OpenAI's GPT-4
- Docker + Docker Compose
- Dynamic JSON character profiles

---

## Features

- Supports multiple characters per player
- Only listens to a specific server + channel, and only when messages begin with `!LEX`
- Dynamically loaded character sheets stored as JSON
- Character switching with simple tags: `!LEX [Mei] I draw my revolver`

---

## Project Structure

```
LexTTRPGBot/
├── bot/                # Main bot code
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── character_loader.py
│   ├── requirements.txt
│   └── characters/     # Prod character sheets
├── tests/              # All test code
│   ├── dev_test.py
│   └── test_characters/
├── .env                # Main env config
├── .env.test           # Test-specific env config
├── Dockerfile          # For running the live bot
├── Dockerfile.test     # For running tests only
├── docker-compose.yml
```

---

## Setup

### 1. Clone the Repo

```bash
git clone https://github.com/draphick/LexTTRPGBot.git
cd LexTTRPGBot
```

### 2. Fill Out `.env` and `.env.test`

Update both with:
```env
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
GUILD_ID=your_discord_guild_id
CHANNEL_ID=the_channel_to_listen_to
CHARACTER_DIR=/app/bot/characters         # for prod
```

`.env.test` should point here:
```env
CHARACTER_DIR=/app/tests/test_characters
```

---

## Run Tests in Docker

```bash
docker-compose run --rm test-runner
```

This runs `dev_test.py` using test-only character data.

---

## Run the Bot in Discord

```bash
docker-compose up --build
```

Lex will come online and only respond to messages that:
- Come from the configured guild and channel
- Start with `!LEX`

---

## Character Format

Each character is a `.json` file like this:

```json
{
  "name": "Mei",
  "discord_id": "123456789012345678",
  "class": "Survivor",
  "inventory": ["axe", "flashlight"],
  "flavor": "Determined and scarred by the apocalypse"
}
```

Lex will automatically load and include this in his Game Master context.

---

## Future Goals

- `/create_character` command in Discord
- `/add_item`, `/set_class`, `/set_flavor` updates
- Dice rolling (`/roll d20+3`)
- Campaign logging
- Web frontend dashboard

---

## Credits

- AI Game Master: [ChatGPT (Lex)](https://chat.openai.com)
- Dev: [Draphick](https://github.com/draphick)
---
