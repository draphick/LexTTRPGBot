import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bot.character_loader import (
    create_character,
    load_all_characters,
    get_character_by_name_and_user,
    get_default_character_by_discord_id,
    format_character_info
)

def test_create_characters():
    print("Creating characters...")
    import os
    if os.path.exists("characters/testone.json"):
        print("Test characters already exist. Skipping creation.")
        return
    try:
        create_character("TestOne", 1111)
        create_character("TestTwo", 1111)
    except Exception as e:
        print(f"Character creation error: {e}")

def test_loading():
    print("\nLoaded characters:")
    characters = load_all_characters()
    for c in characters:
        print(f" - {c.get('name')} (ID: {c.get('discord_id')})")

def test_lookup():
    print("\nLooking up characters...")
    found = get_character_by_name_and_user("TestOne", 1111)
    print("Found:", found["name"] if found else "None")

    fallback = get_default_character_by_discord_id(1111)
    print("Fallback:", fallback["name"] if fallback else "None")

def test_system_prompt():
    print("\nFormatted system prompt:")
    print(format_character_info())

def test_parse_message(msg):
    import re
    match = re.match(r"\[([\w\s]+)\]", msg)
    char = match.group(1).strip() if match else "default"
    content = re.sub(r'^\[.*?\]\s*', '', msg)
    print(f"Character: {char} | Content: {content}")

if __name__ == "__main__":
    test_create_characters()
    test_loading()
    test_lookup()
    test_system_prompt()
    test_parse_message("[Mei] I attack the ghoul with my flashlight.")
