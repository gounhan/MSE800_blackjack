# Blackjack Game

## Overview

This is a simple console-based Blackjack game implemented in Python. The game allows a single player to play against a computer dealer. The goal is to get as close to 21 as possible without exceeding it. If both the player and dealer have the same score, it results in a draw. The player can choose to draw additional cards or stick with their current hand.

## Features

- Deal cards to the player and dealer.
- Calculate scores and check for Blackjack.
- Allow the player to draw additional cards or stick with their current hand.
- The dealer plays according to standard Blackjack rules.
- Compare the player’s and dealer’s scores to determine the winner.
- Option to play multiple rounds.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/MSE800_blackjack.git
   cd MSE800_blackjack
   ```

2. **Ensure Python is Installed**

   Make sure Python 3.6 or higher is installed on your system. You can check this by running:

   ```bash
   python --version
   ```

3. **Run the Game**

   Navigate to the project directory and run the game script:

   ```bash
   python main.py
   ```

## Project Structure

- `art.py`: Contains the `logo()` function that returns the ASCII art logo for the game.
- `main.py`: The main game script that implements the Blackjack game logic.
- `README.md`: This file.

## How to Play

1. **Start the Game**

   When prompted, type 'y' to start a new game or 'n' to exit.

2. **Gameplay**

   - The game will deal two cards each to the player and dealer.
   - The player will be shown their cards and the dealer’s first card.
   - The player can choose to draw another card or stick with their current hand by typing 'y' or 'n'.
   - The dealer will draw cards until their score is at least 17.
   - The final scores of both the player and dealer will be compared to determine the winner.

3. **Winning and Losing**

   - If the player’s score exceeds 21, they lose.
   - If the dealer’s score exceeds 21, the player wins.
   - If either the player or dealer has a Blackjack (two cards adding up to 21), special conditions apply.
   - The game will announce the result (win, lose, or draw).

4. **Play Again**

   After each game, you will be asked if you want to play again. Type 'y' to play another round or 'n' to exit.

## Code Overview

- **`deal_card()`**: Returns a random card from the deck.
- **`calculate_score(cards)`**: Calculates the score for a given hand of cards. Handles Blackjack and adjusts for Aces if necessary.
- **`compare(user_score, computer_score)`**: Compares the final scores of the player and dealer to determine the result.
- **`play_game()`**: Manages the flow of the game, including dealing cards, player decisions, and dealer actions.

## Contributing

Feel free to fork this repository and make contributions. For major changes, please open an issue to discuss what you would like to change.
