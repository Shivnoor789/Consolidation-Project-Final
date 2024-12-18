# Tuple Out Dice Game

A turn-based dice game where players accumulate points while avoiding "Tuple Out". The first player to reach the target score wins.

## How to Run

- Ensure Python is installed on your computer.
- Install required libraries:
  ```
  pip install seaborn matplotlib
  pip install pandas
  ```
- Run the game:
  ```
  python tuple_out_game.py
  ```
- Follow the prompts to play the game.

## Features

   - **Turn-Based Scoring**: Players roll dice to score points. Fixed dice cannot be rerolled.
   - **Tuple Out Rule**: If all three dice show the same value, the player scores zero for the turn.
   - **Score Visualization**: At the end of the game, a line chart displays each player's scores over the turns using Seaborn.
   - **Game History Tracking**: Records and displays the scores for every turn.   
   - **Game Statistics Summary**:Displays stats like total turns, average score, and number of "Tuple Outs" per player using Pandas.

# Win Conditions:
   - The game ends when a player reaches or exceeds the target score (default: 50 points).

# Example Gameplay
1. Player 1 rolls `2, 2, 4`:
   - The two `2`s are fixed, and the player chooses to reroll the `4`.
   - The reroll results in `3`, so the player scores `2 + 2 + 3 = 7` points.

2. Player 2 rolls `5, 5, 5`:
   - All three dice have the same value, so the player "Tuples Out" and scores `0` points for the turn.

3. Player 3 rolls `1, 4, 6`:
   - The player chooses to reroll all three dice.
   - The reroll results in `2, 2, 5`, fixing the `2`s.
   - The player decides not to reroll the `5` and scores `2 + 2 + 5 = 9` points.
