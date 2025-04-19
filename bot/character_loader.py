import os
import json
from config import CHARACTER_DIR


def load_all_characters():
    characters = []
    for filename in os.listdir(CHARACTER_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(CHARACTER_DIR, filename)) as f:
                try:
                    data = json.load(f)
                    characters.append(data)
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
    return characters

def get_character_by_name_and_user(name, discord_id):
    for char in load_all_characters():
        if (
            char.get("name", "").lower() == name.lower() and
            str(char.get("discord_id")) == str(discord_id)
        ):
            return char
    return None

def get_default_character_by_discord_id(discord_id):
    chars = [c for c in load_all_characters() if str(c.get("discord_id")) == str(discord_id)]
    return chars[0] if chars else None

def format_character_info():
    characters = load_all_characters()
    result = "You are Lex, the Game Master for a story-driven RPG. Speak in a cinematic, immersive tone and respond as if you're narrating an unfolding adventure."
    if not characters:
        result += "No character sheets are currently loaded. "
    else:
        result += "Here are the current characters: \n"
        for char in characters:
            result += f"{char.get('name', 'Unknown')}:"
            for key, value in char.items():
                if key not in ("name", "discord_id"):
                    val = ", ".join(value) if isinstance(value, list) else value
                    result += f"  - {key.capitalize()}: {val}"
            result += "\n"
    return result.strip()

def create_character(name, discord_id):
    name = name.strip()
    if not name:
        raise ValueError("Character name cannot be empty.")

    filename = f"{name.lower().replace(' ', '_')}.json"
    filepath = os.path.join(CHARACTER_DIR, filename)

    if os.path.exists(filepath):
        raise FileExistsError(f"Character '{name}' already exists.")

    character_data = {
        "name": name,
        "discord_id": str(discord_id)
    }

    try:
        with open(filepath, 'w') as f:
            json.dump(character_data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error creating character file: {e}")
        return False
