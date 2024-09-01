# Nebulla Wars

**Nebulla Wars** is a 2D space shooter game built with Python using the Pygame library. In this game, players control a spaceship and must shoot down enemy alien ships, avoid asteroids, and collect power-ups to survive as long as possible.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Controls](#game-controls)
- [Game Assets](#game-assets)
- [Code Overview](#code-overview)
- [License](#license)

## Features
- **Player spaceship**: Move your spaceship around and shoot lasers at enemies.
- **Enemies**: Multiple types of enemy ships, each with its own behavior and shooting patterns.
- **Asteroids**: Dodge or destroy incoming asteroids that can damage your ship.
- **Power-ups**: Collect power-ups to boost your ship's abilities.
- **Levels**: Progress through levels with increasing difficulty.
- **Score System**: Track your score based on how many enemies you defeat.
- **Health Bar**: Monitor your health to avoid getting destroyed.

## Installation

To install and run Nebulla Wars on your local machine, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/nebulla-wars.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd nebulla-wars
   ```

3. **Install the required dependencies:**
   ```sh
   pip install pygame
   ```

4. **Run the game:**
   ```sh
   python spaceinvaders.py
   ```

## How to Play

The objective of Nebulla Wars is to survive as long as possible while shooting down enemy ships and avoiding obstacles. As you progress, the game becomes more challenging with more enemies, faster asteroids, and tougher levels.

## Game Controls

- **Move Left**: `A` or `Left Arrow`
- **Move Right**: `D` or `Right Arrow`
- **Move Up**: `W` or `Up Arrow`
- **Move Down**: `S` or `Down Arrow`
- **Shoot**: `Spacebar`

## Game Assets

The game uses various assets, including:

- **Spaceship**: The player's spaceship.
- **Aliens**: Different types of enemy ships.
- **Asteroids**: Obstacles that players must avoid.
- **Power-ups**: Special items that give the player bonuses.
- **Lasers**: Projectiles used by both the player and enemies.
- **Background**: The space-themed background for the game.

## Code Overview

### Main Components
- **`Laser` Class**: Represents the lasers fired by both the player and enemies.
- **`Ship` Class**: An abstract class representing both the player and enemy ships.
- **`Player` Class**: Inherits from the `Ship` class and handles the player-controlled spaceship.
- **`Enemy` Class**: Inherits from the `Ship` class and represents the enemy ships.
- **`Asteroid` Class**: Represents asteroids in the game.
- **`PowerUp` Class**: Represents power-ups in the game.
- **Collision Detection**: The game uses masks for pixel-perfect collision detection between objects.

### Game Loop
The game loop handles all the key elements, including:
- Updating game states.
- Handling player input.
- Managing game levels and difficulty.
- Rendering the game screen.

### Redrawing the Window
The `redraw_window` function is responsible for updating the display with all the current game elements, including the player, enemies, asteroids, power-ups, and the player's health bar.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software as long as the original repository is credited.

---

Feel free to modify the content to better suit your project. Let me know if you need any other assistance!
