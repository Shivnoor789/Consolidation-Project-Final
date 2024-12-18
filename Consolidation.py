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
        self.scores = {player: 0 for player in players}  # Track cumulative scores
        self.history = []  # Each element will be a dict: {'player':..., 'turn_score':..., 'cumulative_score':..., 'tuple_out':...}
        self.current_player_index = 0

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
            # Tuple Out
            print("Tuple Out! No points this turn.")
            turn_score = 0
            self.history.append({
                'player': player,
                'turn_score': turn_score,
                'cumulative_score': self.scores[player],
                'tuple_out': True
            })
            return 0

        # Identify fixed dice (those forming a pair)
        # If there's a pair, store that value in fixed_dice
        fixed_dice_values = []
        for val, cnt in counts.items():
            if cnt == 2:
                fixed_dice_values.append(val)

        if fixed_dice_values:
            print(f"Fixed dice values: {fixed_dice_values}")
        else:
            print("No fixed dice values.")

        # Reroll loop
        while True:
            reroll_input = input("Do you want to reroll? (yes/no): ").strip().lower()
            if reroll_input == "no":
                break
            # Reroll only dice not matching the fixed_dice_values
            dice = [d if d in fixed_dice_values else random.randint(1, 6) for d in dice]
            print(f"Re-rolled dice: {dice}")

        # Calculate score for this turn
        turn_score = sum(dice)
        self.scores[player] += turn_score
        print(f"{player} scores {turn_score} points this turn! (Cumulative: {self.scores[player]})")

        self.history.append({
            'player': player,
            'turn_score': turn_score,
            'cumulative_score': self.scores[player],
            'tuple_out': False
        })

        return turn_score

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
        df = pd.DataFrame(self.history)
        df["Turn"] = df.index + 1

        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x="Turn", y="cumulative_score", hue="player", palette="tab10")
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
        df = pd.DataFrame(self.history)
        # Aggregate stats
        stats = df.groupby("player").agg(
            Turns_Played=("player", "count"),
            Total_Score=("cumulative_score", "max"),
            Average_Score=("turn_score", "mean"),
            Tuple_Outs=("tuple_out", "sum")  # since tuple_out is boolean, sum will count True values
        )

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

    print("Welcome to Tuple Out Dice Game!")
    num_players = int(input("Enter the number of players: "))
    players = [input(f"Enter name for Player {i + 1}: ") for i in range(num_players)]
    game = TupleOutGame(players)
    game.play_game()

