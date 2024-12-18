**Follow the Prompts:**
   - Enter the number of players.
   - Provide the name for each player.
   - Play the game by following the instructions displayed during each turn.

## Features
   - Supports two or more players.
   - Players take turns rolling dice to accumulate points.

# Turn-Based Scoring:
   - Players roll three dice on their turn.
   - If two dice show the same value, they are fixed and cannot be rerolled.
   - Players can choose whether to reroll unfixed dice.

# Tuple Out
   - If all three dice have the same value during a turn, the player "Tuples Out" and scores zero points for that turn.

# Game History Tracking
   - At the end of the game, the program displays a detailed history of all turns, showing each player's score for every turn.

# Win Conditions:
   - The game ends when a player reaches or exceeds the target score (default: 50 points).
   - The winner and final scores are displayed.

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

## Winning the Game
- The first player to reach or exceed the target score wins.
- At the end of the game, a summary of all turns and the winner is displayed.
