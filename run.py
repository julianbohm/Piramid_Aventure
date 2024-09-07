# Rooms and connections of the game
rooms = {
    'sarcophagus_chamber' : {
        'description': "You awaken in a dark chamber, the cold stone of the pyramid walls surrounds you. The flicker of ancient torchlight casts long shadows on the walls, and the air smells of dust and time. You are the Pharaoh, long entombed, but somehow, you have awoken from your eternal sleep.",
        'north': 'north_passage',
        'south': 'south_passage',
        'est': 'swamp'
    },
    'north_passage' : {
        'description': "",
        'north': 'anubis_chamber',
        'est': 'cristal_chamber'

    },
    'south_passage' : {
        'description': "",
        'south': 'seth_tempel',
        'est': 'catacombs'

    },
    'anubis_chamber' : {
        'description': "",
        
    },
    'cristal_chamber' : {
        'description': "",
        'north': 'anubis_chamber',
        'est': 'red_staircase'

    },
    'swamp' : {
        'description': "",
        'north': 'cristal_chamber',
        'south': 'catacombs',
        'est': 'horus_tempel'

    },
    'catacombs' : {
        'description': "",
        'north': 'swamp',
        'south': 'seth_tempel',
        'est': 'treasure_chamber'

    },
    'seth_temple' : {
        'description': "",
        
    },
    'red_staircase' : {
        'description': "",
        'north': 'anubis_temple',
        'south': 'horus_temple',
        'est': 'Kindom'

    },
    'horus_temple' : {
        'description': "",
        'north': 'red_staircase',
        'south':'treasure_chamber',
        'est': 'kindom'

    },
    'treasure_chamber' : {
        'description': "",
        'north': 'horus_temple',
        'south': 'seth_tempel',
        'est': 'kindom'

    },

    'victory' : {
        'description': "",

    },

}