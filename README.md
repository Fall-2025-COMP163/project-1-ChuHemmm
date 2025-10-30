[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21349609&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character
def create_character(name, character_class):
    char_creation = {"name": name, "class": character_class, "level": 1, "gold": 100, "strength": 60, "magic": 32, "health": 100}
    return char_creation 
calculate_stats(character_class, level) - Calculate character stats
if character_class == "Warrior":
        strength = 10 + (3 * level)
        magic = 2 + (1 * level)
        health = 100 + (10 * level)
    elif character_class == "Mage":
        strength = 3 + (1 * level)
        magic = 12 + (4 * level)
        health = 70 + (6 * level)
    elif character_class == "Rogue":
        strength = 7 + (2 * level)
        magic = 5 + (2 * level)
        health = 60 + (5 * level)
    elif character_class == "Cleric":
        strength = 6 + (2 * level)
        magic = 10 + (3 * level)
        health = 90 + (8 * level)
    else:
        strength = 5 + (1 * level)
        magic = 5 + (1 * level)
        health = 80 + (5 * level)
    return (strength, magic, health)
save_character(character, filename) - Save character to file
if character == {} or filename =="":
        return False 
    
    directory = os.path.dirname(filename)
    if directory != "" and not os.path.exists(directory):
        return False
    
    with open(filename, "w") as char_file:
        char_file.write(f"Character Name: {character['name']}\n")
        char_file.write(f"Class: {character['class']}\n")
        char_file.write(f"Level: {character['level']}\n")
        char_file.write(f"Strength: {character['strength']}\n")
        char_file.write(f"Magic: {character['magic']}\n")
        char_file.write(f"Health: {character['health']}\n")
        char_file.write(f"Gold: {character['gold']}\n")
    
    return True
load_character(filename) - Load character from file
if not os.path.exists(filename):
        return None

    character = {}
    with open(filename, "r") as file:
        for line in file:
            if ": " not in line:
                continue
            key, value = line.strip().split(": ", 1)
            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)

    return character
display_character(character) - Display character info
 print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

level_up(character) - Increase character level
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge

AI helped me with my main function and giving me programs to test 
