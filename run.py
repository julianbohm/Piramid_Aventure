# Function for rooms dictionary
def create_rooms():
    return {
        'sarcophagus_chamber': {
            'description': (
                "You awaken in a dark chamber, the cold stone of the pyramid"
                "walls surrounds you. The flicker of ancient torchlight casts"
                "long shadows on the walls, and the air smells of dust and"
                "time. You are the Pharaoh, long entombed, but somehow,"
                "you have awoken from your eternal sleep."
            ),
            'north': 'north_passage',
            'south': 'south_passage',
            'east': 'swamp'
        },
        'north_passage': {
            'description': (
                "The North passage narrows as you proceed, leading deeper into"
                "the pyramid. The walls are etched with hieroglyphs of your"
                "past glory. You feel a sense of destiny."
            ),
            'north': 'anubis_chamber',
            'east': 'cristal_chamber',
            'south': 'sarcophagus_chamber'
        },
        'south_passage': {
            'description': (
                "The South passage is narrow and dimly lit, the walls slick"
                "with condensation. As you walk, strange sounds echo in the"
                "distance—whispers of the long-dead. The flicker of your"
                "torch casts shifting shadows on the walls, and your footsteps"
                "seem to quicken the heartbeat of the ancient stone."
            ),
            'north': 'sarcophagus_chamber',
            'south': 'seth_temple',
            'east': 'catacombs'
        },
        'anubis_chamber': {
            'description': (
                "You step into the Chamber of Anubis, the air heavy with the"
                "scent of incense and the weight of millennia. The towering"
                "statues of Anubis, jackal-headed and cold, watch as you"
                "approach the center of the room. A stone altar rises before"
                "you, flanked by dark torches flickering with blue flames."
                "Atop the altar lies the Scales of Ma’at, waiting to weigh"
                "your heart against the feather of truth. Anubis’ voice fills"
                "the chamber, deep and resonant: 'Pharaoh, your journey ends"
                "here. All your choices have led to this moment."
                "Your heart will be judged.'"
            ),
        },
        'cristal_chamber': {
            'description': (
                "You enter the heart of the Crystal Chambers, where the walls"
                "shimmer with a thousand reflections of light. The air hums"
                "with ancient magic, and in the center, a massive crystal"
                "pulses with energy. Horus’ voice returns: 'Pharaoh, the power"
                "you seek lies within, but it is guarded by forces beyond"
                "your understanding.'"
            ),
            'north': 'anubis_chamber',
            'east': 'red_staircase',
            'west': 'north_passage',
            'south': 'swamp'
        },
        'swamp': {
            'description': (
                "You are in a dark, muddy swamp. The air is thick with decay,"
                "wet earth, and strange noises. Vines hang from trees, and the"
                "ground squelches underfoot. The dim light barely cuts through"
                "the dense canopy."
            ),
            'north': 'cristal_chamber',
            'south': 'catacombs',
            'east': 'horus_temple',
            'west': 'sarcophagus_chamber'
        },
        'catacombs': {
            'description': (
                "You enter the catacombs beneath the temple, where your old"
                " warriors stand as bronze statues. Their eyes seem to follow"
                "you as you walk among them, frozen in time but eerily"
                "lifelike. At the center of the chamber, your most trusted "
                "general stands in solemn vigil. Anubis voice echoes, They "
                "await your command. Will they rise once more, or remain"
                "trapped in bronze?"
            ),
            'north': 'swamp',
            'south': 'seth_temple',
            'east': 'treasure_chamber',
            'west': 'south_passage'
        },
        'seth_temple': {
            'description': (
                "You enter the Temple of Seth, its dark interior filled with"
                "the god's ominous presence. The altar at the center radiates"
                "an unsettling energy, and Seth’s laughter echoes through the"
                "chamber. As you approach, Seth’s voice intones, “Here your"
                "journey ends, Pharaoh. Chaos reigns supreme.' The shadows"
                "close in, and the temple’s darkness claims you,"
                "sealing your fate."
            ),
        },
        'red_staircase': {
            'description': (
                "You stand before a grand staircase, its steps colored red"
                "from years of wear. The air grows lighter, and you feel"
                "a sense of hope as you ascend to the top."
            ),
            'north': 'anubis_chamber',
            'south': 'horus_temple',
            'east': 'victory',
            'west': 'cristal_chamber'
        },
        'horus_temple': {
            'description': (
                "You are inside the ancient Temple of Horus, sunlight "
                "streaming through high windows, casting the god’s symbol on"
                "the floor. A voice echoes through the chamber: I have"
                "returned to guide you. Choose your path wisely.' Before you."
                "Horus’ voice grows softer, 'Each path holds your fate;"
                "may the gods favor you.'"
            ),
            'north': 'red_staircase',
            'south': 'treasure_chamber',
            'east': 'victory',
            'west': 'swamp'
        },
        'treasure_chamber': {
            'description': (
                "You find yourself deep within the Temple of Horus, standing"
                "before a massive stone door adorned with golden hieroglyphs."
                "The voice of Horus speaks softly: “Beyond this lies the"
                "Treasure Chamber, but only the worthy may claim its riches."
                "Choose carefully."
            ),
            'north': 'horus_temple',
            'south': 'seth_temple',
            'east': 'victory',
            'west': 'catacombs'
        },
        'victory': {
            'description': (
                "You stand victorious in the heart of the temple, the gods now"
                "silent as the power of your triumph fills the air. The"
                "treasures of the kingdom lie before you—gold, jewels, and"
                "relics of immense power, all now yours to command. The throne"
                "room shimmers with wealth beyond imagination, and your"
                "subjects bow in reverence as you take your place upon"
                "the throne. The voice of Horus echoes one final time:"
                " Pharaoh, the kingdom is yours. Power, riches, and eternal"
                "glory await you. As the light of the gods fades, you realize"
                "that your reign has only just begun, your name destined to"
                "echo through eternity."
            ),
        },
    }


# Function to welcome and get the player name
def welcome_player():
    name = input("What is your name, Pharaoh? ")
    print(f"\nWelcome, Pharaoh {name}, to the land of the living!\n")
    return name


#Function current room
def describe_current_room(room, rooms):
    print(rooms[room]['description'])


# Main game function
def play_game():
    global current_room

    while True:
        command = input("Enter a direction (north, south, east, west) or 'quit' to end the game: ").lower()

        # quit command  send a goodbye massage and end the game.
        if command == 'quit':
            print(f"Farewell, Pharaoh {name}!!!!!")
            break
        # move the players to the other romms.
        if command in rooms[current_room]:
            current_room = rooms[current_room][command]
            print(f"\nYou move {command} and find yourself in {current_room} :\n")
            print(rooms[current_room]['description'])
            print()
            # victory room finish the game with a message of vitory.
            if current_room == 'victory':
                print(f"\nCongratulations, Pharaoh {name}, you have achieved victory and eternal glory!")
                break
            elif current_room == 'seth_temple' or current_room == 'anubis_chamber':
                print(f"you lose Pharaoh {name}, your name will be forgotten.")
                break
        else:
            print("You can't go that way, try another direction.")


# Start the game
play_game()