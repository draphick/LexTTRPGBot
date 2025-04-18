import discord
import openai
import traceback
import re
from config import DISCORD_TOKEN, OPENAI_API_KEY, GUILD_ID, CHANNEL_ID, GPT_THREAD_ID
from character_loader import format_character_info, get_character_by_name_and_user, get_default_character_by_discord_id

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

openai.api_key = OPENAI_API_KEY

@client.event
async def on_ready():
    print(f"{client.user} has connected.")

@client.event
async def on_message(message):
    if (
        message.author == client.user or
        message.guild.id != GUILD_ID or
        message.channel.id != CHANNEL_ID or
        not message.content.startswith("!LEX")
    ):
        return

    username = message.author.display_name
    discord_id = message.author.id
    content = message.content.lstrip("!LEX").strip()

    character_name_match = re.match(r"\[([\w\s]+)\]", content)
    explicit_character = character_name_match.group(1).strip() if character_name_match else None
    character = get_character_by_name_and_user(explicit_character, discord_id) if explicit_character else get_default_character_by_discord_id(discord_id)

    if character:
        character_name = character["name"]
        prompt = f"{character_name} says: {re.sub(r'^\\[.*?\\]', '', content).strip()}"
    else:
        prompt = f"{username} says (no character profile found): {content}"

    system_message = format_character_info()

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            thread_id=GPT_THREAD_ID if GPT_THREAD_ID else None,
        )
        reply = response['choices'][0]['message']['content']
        await message.channel.send(reply)

    except Exception as e:
        error_msg = f"❌ Error communicating with Lex:\n```\n{traceback.format_exc()}\n```"
        await message.channel.send(error_msg)

client.run(DISCORD_TOKEN)
