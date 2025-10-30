"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Chu Hemmingway
Date: 10/27/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
AI helped with the main program area for testing functions
"""
import os

def create_character(name, character_class):
    char_creation = {"name": name, "class": character_class, "level": 1, "gold": 100, "strength": 60, "magic": 32, "health": 100}
    # stats = calculate_stats(character_class,1)
    # char = {
    #         "name": name,
    #         "class": character_class,
    #         "level": 1,
    #         "strength": 45,
    #         "magic": 50
    #         "health": 80,
    #         "gold": 100
    #     }

    return char_creation
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
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
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
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
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
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

        
    
    
    
    # return character

    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

def level_up(character):
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    return character

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    # print("=== CHARACTER CREATOR ===")
    # print("Test your functions here!")
    # char = create_character("Aria", "Mage")
    # print("New character created!\n")
    # display_character(char)
    # print()

    # # # Save the character to a file
    # save_character(char, "aria_character.txt")
    # print("Character saved to 'aria_character.txt'\n")

    # # # Load the character from the file
    # # loaded_char = load_character("aria_character.txt")
    # # if loaded_char:
    # #     print("Character successfully loaded!\n")
    # #     display_character(loaded_char)
    # # else:
    # #     print("Character file not found.\n")

    # # # Level up the character
    # print("\nLeveling up character...")
    # level_up(char)
    # display_character(char)
    
    # Example usage:
    char = create_character("TestHero", "Warrior")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")
    level_up(char)
    display_character(char)
    level_up(char)
    display_character(char)
