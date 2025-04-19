from character_loader import (
    create_character,
    load_all_characters,
    get_character_by_name_and_user,
    get_default_character_by_discord_id,
    format_character_info
)
from config import CHARACTER_DIR

def test_create_characters():
    print("test_create_characters")
    import os
    if not os.path.exists(f"{CHARACTER_DIR}/testone.json"):
        print("testone")
        create_character("TestOne", 1111)
    if not os.path.exists(f"{CHARACTER_DIR}/testtwo.json"):
        print("testtwo")
        create_character("TestTwo", 2222)
    if not os.path.exists(f"{CHARACTER_DIR}/testonea.json"):
        print("testonea")
        create_character("TestOneA", 1111)
    if not os.path.exists(f"{CHARACTER_DIR}/testthree.json"):
        print("testthree")
        create_character("TestThree", 3333)

def test_duplicate_name_different_discord_user_create_characters():
    print("test_duplicate_name_different_discord_user_create_characters")
    try:
        create_character("TestOne", 2222)
    except Exception as e:
        print(f"Character creation error: {e}")

def test_duplicate_name_same_discord_user_create_characters():
    print("test_duplicate_name_same_discord_user_create_characters")
    try:
        create_character("TestOne", 1111)
    except Exception as e:
        print(f"Character creation error: {e}")

def test_load_all_characters():
    print("\ntest_load_all_characters")
    characters = load_all_characters()
    for c in characters:
        print(f" - {c.get('name')} (ID: {c.get('discord_id')})")

def test_get_character_by_name_and_user():
    print("\ntest_get_character_by_name_and_user")
    found = get_character_by_name_and_user("TestOne", 1111)
    print("Found:", found["name"] if found else "None")

def test_get_default_character_by_discord_id():
    print("\ntest_get_default_character_by_discord_id")
    fallback = get_default_character_by_discord_id(1111)
    print("Fallback:", fallback["name"] if fallback else "None")

def test_format_character_info():
    print("\ntest_system_prompt")
    print(format_character_info())

if __name__ == "__main__":
    test_create_characters()
    test_duplicate_name_different_discord_user_create_characters()
    test_duplicate_name_same_discord_user_create_characters()
    test_load_all_characters()
    test_get_character_by_name_and_user()
    test_get_default_character_by_discord_id()
    test_format_character_info()
