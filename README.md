# Street Fighter Game

A 2D arcade-style fighting game built with Python and Pygame. This project simulates a two-player fighting game with animations, health bars, sound effects, and background music.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Gameplay](#gameplay)
- [File Structure](#file-structure)
- [Controls](#controls)

## Project Overview
The **Street Fighter Game Clone** is a Python project that mimics a two-player arcade fighting game. The game includes two unique characters, each with animations, health bars, and two distinct attacks. Players can jump, move left and right, and attack their opponents with different styles. The game continues until one player’s health reaches zero, after which a victory screen is displayed.

## Features
- **Two distinct characters** with unique sprites and animations.
- **Health bars** for each player to track their remaining health.
- **Countdown timer** to delay the start of each round.
- **Sound effects** for actions and background music.
- **Victory screen** when a player wins a round.

## Setup and Installation

### Requirements
- Python 3.x
- [Pygame](https://www.pygame.org/wiki/GettingStarted) library

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AadityaPanda/Street_Fighter.git
   cd Street_Fighter
   ```

2. Install the required dependencies:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## Gameplay
Each player controls a fighter, with the objective of depleting the opponent's health bar. The game includes sound effects for attacks and movement, and players can perform different actions like running, jumping, and attacking.


https://github.com/user-attachments/assets/20e788ff-76b7-4707-8377-334d8e4d9472


## File Structure
- `main.py`: Main game loop and functions for drawing, text rendering, and player statistics.
- `fighter.py`: Fighter class, including methods for movement, health, animations, and attacks.
- `assets/`: Contains images, sound files, and fonts for the game.

## Controls

### Player 1
- Move Left: `A`
- Move Right: `D`
- Jump: `W`
- Attack 1: `R`
- Attack 2: `T`

### Player 2
- Move Left: `Left Arrow`
- Move Right: `Right Arrow`
- Jump: `Up Arrow`
- Attack 1: `M`
- Attack 2: `N`
