import random
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

class TupleOutGame:
    """
    A turn-based dice game where players aim to avoid "Tuple Out" and accumulate scores. 
    The first player to reach the target score wins.
    """
    def __init__(self, players, target_score=50):
        """
        Initialize the game with player names, a target score, and data tracking.
        
        Args:
            players (list): List of player names.
            target_score (int): Score required to win the game.
        """
        self.players = players
        self.target_score = target_score
        self.scores = {player: 0 for player in players}  # Track total scores
        self.history = []  # Store (player, cumulative score) per turn
        self.current_player_index = 0  # Track the current player

    def roll_dice(self):
        """
        Simulate rolling three dice.

        Returns:
            list: A list of three integers between 1 and 6.
        """
        return [random.randint(1, 6) for _ in range(3)]

    def play_turn(self, player):
        """
        Conduct a single turn for a player.

        Args:
            player (str): Name of the player taking the turn.

        Returns:
            int: Points scored during this turn.
        """
        print(f"\n{player}'s turn!")
        dice = self.roll_dice()
        print(f"Initial roll: {dice}")

        # Check for Tuple Out (all dice match)
        counts = {x: dice.count(x) for x in set(dice)}
        if 3 in counts.values():
            print("Tuple Out! No points this turn.")
            self.history.append((player, self.scores[player]))  # Log current cumulative score
            return 0

        # Allow rerolling of unfixed dice
        fixed_dice = [die for die, count in counts.items() if count == 2]
        print(f"Fixed dice: {fixed_dice}")

        while True:
            reroll_input = input("Do you want to reroll? (yes/no): ").strip().lower()
            if reroll_input == "no":
                break
            # Reroll only dice that are not fixed
            dice = [
                random.randint(1, 6) if dice.count(d) < 2 else d
                for d in dice
            ]
            print(f"Re-rolled dice: {dice}")

        # Calculate score
        total_score = sum(dice)
        self.scores[player] += total_score
        self.history.append((player, self.scores[player]))  # Log updated cumulative score
        print(f"{player} scores {total_score} points!")

        return total_score

    def check_winner(self):
        """
        Check if any player has reached the target score.

        Returns:
            str: The name of the winning player, or None if no winner yet.
        """
        for player, score in self.scores.items():
            if score >= self.target_score:
                return player
        return None

    def visualize_scores(self):
        """
        Generate a line graph of player scores over the game turns using Seaborn.
        """
        # Prepare data
        players = [entry[0] for entry in self.history]
        scores = [entry[1] for entry in self.history]
        turns = list(range(1, len(scores) + 1))

        # Plot the scores
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=turns, y=scores, hue=players, palette="tab10")
        plt.title("Player Scores Over Turns")
        plt.xlabel("Turn Number")
        plt.ylabel("Cumulative Score")
        plt.legend(title="Players")
        plt.show()

    def summarize_game(self):
        """
        Summarize the game statistics using Pandas, including total turns, average score,
        and the number of 'Tuple Outs' for each player.
        """
        # Create a DataFrame for the game history
        df = pd.DataFrame(self.history, columns=["Player", "Total_Score"])
        stats = df.groupby("Player").agg(
            Turns_Played=("Player", "count"),
            Total_Score=("Total_Score", "max"),
            Average_Score=("Total_Score", "mean"),
            Tuple_Outs=("Total_Score", lambda x: (x == 0).sum())
        )

        # Display the stats summary
        print("\nGame Summary Statistics:")
        print(stats)

    def play_game(self):
        """
        Run the game until a player reaches the target score.
        """
        print(f"Welcome to Tuple Out! First to {self.target_score} points wins.")
        while True:
            player = self.players[self.current_player_index]
            self.play_turn(player)

            winner = self.check_winner()
            if winner:
                print(f"\nCongratulations, {winner} wins with {self.scores[winner]} points!")
                self.visualize_scores()  # Show score visualization
                self.summarize_game()  # Display game statistics
                break

            self.current_player_index = (self.current_player_index + 1) % len(self.players)


# Game setup
if __name__ == "__main__":
    print("Welcome to Tuple Out Dice Game!")
    num_players = int(input("Enter the number of players: "))
    players = [input(f"Enter name for Player {i + 1}: ") for i in range(num_players)]
    game = TupleOutGame(players)
    game.play_game()
