#Consolidation Project

import random
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class TupleOutGame:

    def __init__(self, players, target_score=50):
        self.players = players  # List of player names
        self.target_score = target_score  # Score needed to win
        self.scores = {player: 0 for player in players}  # Dictionary to track scores
        self.history = []  # Pattern 6.3: Appending turns to a history list
        self.current_player_index = 0  # Track which player's turn it is

    def roll_dice(self):
        return [random.randint(1, 6) for _ in range(3)]

    def play_turn(self, player):
        print(f"\n{player}'s turn!")
        dice = self.roll_dice()
        print(f"Initial roll: {tuple(dice)}")  # Pattern 7.4: Use of tuples for immutability

        while True:
            counts = {x: dice.count(x) for x in set(dice)}  # Pattern 7.3: Use of dictionaries
            if 3 in counts.values():
                print("Tuple Out! No points this turn.")
                self.history.append((player, 0))  # Append turn result to history
                return 0

            fixed_dice = [die for die, count in counts.items() if count == 2]
            print(f"Fixed dice: {tuple(fixed_dice)}")  # Show fixed dice as a tuple for clarity

            reroll_input = input("Do you want to reroll? (yes/no): ").strip().lower()
            if reroll_input == "no":
                break

            dice = [
                random.randint(1, 6) if counts.get(d, 0) < 2 else d
                for d in dice
            ]
            print(f"Re-rolled dice: {tuple(dice)}")

        total_score = sum(dice)
        print(f"{player} scores {total_score} points!")
        self.history.append((player, total_score))  # Append turn result to history
        return total_score

    def check_winner(self):
        for player, score in self.scores.items():
            if score >= self.target_score:
                return player
        return None

     def visualize_scores(self):
        # Convert history to usable data for Seaborn
        players = [entry[0] for entry in self.history]
        scores = [entry[1] for entry in self.history]
        turns = list(range(1, len(scores) + 1))
         
        # Plot the scores over turns
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=turns, y=scores, hue=players)
        plt.title("Player Scores Over Turns")
        plt.xlabel("Turn Number")
        plt.ylabel("Total Score")
        plt.legend(title="Players")
        plt.show()

    def summarize_game(self):
    # Create a DataFrame for the game history
    df = pd.DataFrame(self.history, columns=["Player", "Total_Score"])
    stats = df.groupby("Player").agg(
        Turns_Played=("Player", "count"),
        Total_Score=("Total_Score", "max"),
        Average_Score=("Total_Score", "mean"),
        Tuple_Outs=("Total_Score", lambda x: (x == 0).sum())
    )
    print("\nGame Summary Statistics:")
    print(stats)

    def play_game(self):
        print(f"Welcome to the Tuple Out Dice Game! First to {self.target_score} points wins.\n")
        while True:
            player = self.players[self.current_player_index]
            points = self.play_turn(player)
            self.scores[player] += points
            print("Current scores:", self.scores)

            winner = self.check_winner()
            if winner:
                print(f"\nCongratulations, {winner} wins with {self.scores[winner]} points!")
                print("\nGame History:")
                for turn in self.history:
                    print(f"Player: {turn[0]}, Score: {turn[1]}")
                break

            self.current_player_index = (self.current_player_index + 1) % len(self.players)


# Game setup and start
print("Welcome to Tuple Out Dice Game!")
num_players = int(input("Enter the number of players: "))
players = [input(f"Enter name for Player {i + 1}: ") for i in range(num_players)]
game = TupleOutGame(players)
game.play_game()
