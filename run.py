# Rooms and connections of the game
rooms = {
    'sarcophagus_chamber' : {
        'description': "You awaken in a dark chamber, the cold stone of the pyramid walls surrounds you. The flicker of ancient torchlight casts long shadows on the walls, and the air smells of dust and time. You are the Pharaoh, long entombed, but somehow, you have awoken from your eternal sleep.",
        'north': 'north_passage',
        'south': 'south_passage',
        'est': 'swamp'
    },
    'north_passage' : {
        'description': "The North passage narrows as you proceed, leading deeper into the pyramid. The walls are etched with hieroglyphs of your past glory. You feel a sense of destiny.",
        'north': 'anubis_chamber',
        'est': 'cristal_chamber'

    },
    'south_passage' : {
        'description': "The South passage is narrow and dimly lit, the walls slick with condensation. As you walk, strange sounds echo in the distance—whispers of the long-dead. The flicker of your torch casts shifting shadows on the walls, and your footsteps seem to quicken the heartbeat of the ancient stone.",
        'south': 'seth_tempel',
        'est': 'catacombs'

    },
    'anubis_chamber' : {
        'description': "You step into the Chamber of Anubis, the air heavy with the scent of incense and the weight of millennia. The towering statues of Anubis, jackal-headed and cold, watch as you approach the center of the room. A stone altar rises before you, flanked by dark torches flickering with blue flames."
         "Atop the altar lies the Scales of Ma’at, waiting to weigh your heart against the feather of truth. Anubis’ voice fills the chamber, deep and resonant: 'Pharaoh, your journey ends here. All your choices have led to this moment. Your heart will be judged.'",
        
    },
    'cristal_chamber' : {
        'description': "You enter the heart of the Crystal Chambers, where the walls shimmer with a thousand reflections of light. The air hums with ancient magic, and in the center, a massive crystal pulses with energy. Horus’ voice returns: 'Pharaoh, the power you seek lies within, but it is guarded by forces beyond your understanding.'",
        'north': 'anubis_chamber',
        'est': 'red_staircase'

    },
    'swamp' : {
        'description': "",
        'north': 'cristal_chamber',
        'south': 'catacombs',
        'est': 'horus_tempel'

    },
    """
    'catacombs' : {
        'description': "You enter the catacombs beneath the temple, where your old warriors stand as bronze statues. Their eyes seem to follow you as you walk among them, frozen in time but eerily lifelike.
        "At the center of the chamber, your most trusted general stands in solemn vigil. Anubis' voice echoes, “They await your command. Will they rise once more, or remain trapped in bronze?",
        'north': 'swamp',
        'south': 'seth_tempel',
        'est': 'treasure_chamber'
        """

    },
    'seth_temple' : {
        'description': "You enter the Temple of Seth, its dark interior filled with the god's ominous presence. The altar at the center radiates an unsettling energy, and Seth’s laughter echoes through the chamber.
        "As you approach, Seth’s voice intones, “Here your journey ends, Pharaoh. Chaos reigns supreme.' The shadows close in, and the temple’s darkness claims you, sealing your fate.",
        
    },
    'red_staircase' : {
        'description': "",
        'north': 'anubis_temple',
        'south': 'horus_temple',
        'est': 'Kindom'

    },
    'horus_temple' : {
        'description': "You are inside the ancient Temple of Horus, sunlight streaming through high windows, casting the god’s symbol on the floor. A voice echoes through the chamber: 'Pharaoh {name}, I have returned to guide you. Choose your path wisely.' Before you. Horus’ voice grows softer, 'Each path holds your fate; may the gods favor you.'",
        'north': 'red_staircase',
        'south':'treasure_chamber',
        'est': 'kindom'

    },
    'treasure_chamber' : {
        'description': "You find yourself deep within the Temple of Horus, standing before a massive stone door adorned with golden hieroglyphs. The voice of Horus speaks softly: “Beyond this lies the Treasure Chamber, but only the worthy may claim its riches. Choose carefully, Pharaoh {name}.",
        'north': 'horus_temple',
        'south': 'seth_tempel',
        'est': 'kindom'

    },

    'victory' : {
        'description': "You stand victorious in the heart of the temple, the gods now silent as the power of your triumph fills the air. The treasures of the kingdom lie before you—gold, jewels, and relics of immense power, all now yours to command. The throne room shimmers with wealth beyond imagination, and your subjects bow in reverence as you take your place upon the throne.
        "The voice of Horus echoes one final time: “Pharaoh, the kingdom is yours. Power, riches, and eternal glory await you.”
        "As the light of the gods fades, you realize that your reign has only just begun, your name destined to echo through eternity.",

    },

}

# Inicial player's location
current_room = 'sarcophagus_chamber'


# Main game function
def play_game():
    global current_room 

    """
    ask player for input name at the start of the game, and Welcome message with line spacing
    """
    name = input("What is your name, Pharaon?" )

    print(f"\nWelcome, Pharaon {name}, to the land of the living!\n")
