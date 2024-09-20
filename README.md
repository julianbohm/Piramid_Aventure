# Piramid Aventure 

### A text-base Adventure Game

Piramid Aventure is a text-based adventure game where you, the Pharaoh, have mysteriously awoken from your eternal slumber in an ancient pyramid. As you explore various chambers, your choices will determine your fate. Can you reclaim your glory, or will the gods seal your fate forever?



---

## Table of Contents

- [Overview](#overview)
- [How to Play](#how-to-play)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
- [bugs and Errors](#bugs-and-erros)
- [Strategy](#strategy)
- [Testing](#testing)
- [Flowchart](#flowcharts)
- [Deployment](#deployment)
- [Tools](#tools)
- [Acknowledgements](#acknowledgements)




---

## Overview
In **Piramid Aventure**, players explore a series of interconnected rooms
within an ancient pyramid. The goal is to navigate through the various
chambers, solve puzzles, and make wise choices to either reclaim your throne
or face eternal doom. Each room holds its own story, and each step you take
will bring you closer to either glory or downfall.

The fully deployed project can be accesed at ......

---
## How to Play
1. Upon launching the game, you'll be asked to provide your name as the Pharaoh.
2. After the welcome message, you will awaken in the Sarcophagus Chamber.
3. Navigate the pyramid using directional commands: north, south, east, west
   depending on available exits from your current room.
4. Type commands based on the prompts to explore rooms, interact with
   the environment, and solve puzzles.
5. The game ends when you either:
   - Solve the final puzzle and claim victory.
   - Meet your demise in one of the dangerous chambers like the Seth
     Temple or Anubis Chamber.

## Features

### Existing Features

The game has multiple features implemented  to make the experience more 
interactive and enjoyable.
- **Personalize your Text-based Adventure**: The game ask as input the name 
of the player at the beginning, so the user can put the name of their 
choosing for the whole game., the code also protect from accidental empty 
spaces or estarting without name.
- **Text-based Adventure**: Explore rooms, interact with the environment, 
and make choices via text commands.
- the text comands available are North, South, East, West, and Quit.
-every room gives the user the choices availables for each room, they change 
depending of the room, making it easier for the user to know where to go.
- **Puzzle Solving**: the game gives the user the challenge at the end to 
answer a puzzle to unlock paths claim victory.
- **Multiple Endings**: Your journey can end in different ways based on the 
decisions of the paths that you make.
- **Rich Storytelling**: Experience a story filled with ancient Egyptian 
mythology and aventure.

### Future Features

- **Inventory System**: Players will be able to collect items during their 
 exploration. when all items gather the last room will apear.
- **Secret Ending**: If the player does not input any commands for 30 seconds 
at the first room, a hidden "secret winning ending" is triggered,
- **Monster Battle System**: The player may encounter monsters,  Players will 
have to fight using random numbers for health and attack.
- **Randomized Puzzles**: To enhance replayability, puzzles will be randomized 
for each playthrough. This means that even if a player plays multiple times, 
they will encounter different challenges, keeping the game fresh and engaging.

---

## Bugs and Errors




---

## Testing



---

## Deployment

This project was deployed using Heroku:

Create a new Heroku app
Add two buildpacks from the "Settings" tab in that order:
Python
NodeJS
Add Config Vars from the "Settings" tab:
Key: PORT
Value: 8000
Connect your GitHub repository and deploy as normal
