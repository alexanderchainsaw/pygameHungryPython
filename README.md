# <p align="center">HungryPython</p>
![](https://github.com/alexanderchainsaw/pygameHungryPython/assets/126553365/16a23d50-3b6d-4341-b1be-cb2879a70183)

This is a classic Snake game implemented using the Pygame library in Python. The game allows the player to control a snake to eat food and grow longer while avoiding collisions with the snake's own body.
The snake is stylized to look like the one from Python logo, the food is represented by various programming langues logos.


## Project Structure
The project is organized into several files and directories:

- `hungry_python.py`: The main file of the project. It inherits from the Settings class at `settings.py`, uses initialized assets from the Assets class at `assets.py`. Its main objective is to handle the main game loop.
- `settings.py`: This file contains the `Settings` class, which stores constant variables such as the screen resolution, square size, snake speed. It also initializes the Pygame environment and manages the clock, screen, and fonts used in the game. The screen resolution is collected using `ctype` library, which is then matched to the predefined dictionary to set square size of one movement block. If collected screen resolution has not matched, it will set default values of width, height, square size of - 1000, 720, 40. The file also contains the `SliceableDeque`
class which will be used to generate snake body and make it sliceable (which will be needed for painting the snake in 2 colors)
Also contains
- `assets.py`: This file contains the `Assets` class, which stores the in-game asset images. It loads the images based on the square size defined in the `Settings` class.

## Requirements
- Python 3
- Pygame library

## Installation
1. Clone the repository:
```
https://github.com/alexanderchainsaw/pygameHungryPython.git
```
3. Install requirements.txt:
```
pip install -r /requirements.txt
```

## Usage
1. Navigate to the project directory:
cd pygame-snake
2. Run the game:
python main.py
3. Use the arrow keys or `WASD` keys to control the snake.
4. Press `ENTER` to start the game and `ESC` to quit.
5. Avoid collisions with the snake's own body.
6. Eat the food to grow longer and increase the score.
