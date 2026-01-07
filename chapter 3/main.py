import random
import math

teams = []
playing_teams = {"myself": None, "enemy": None}


class Team:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.total_score = 0

    def info(self):
        print(
            f"{self.name}: offensive power: {self.attack} / defensive power: {self.defense}"
        )

    def get_hit_rate(self):
        return random.randint(10, self.attack)

    def get_out_rate(self):
        return random.randint(10, self.defense)


def create_teams():

    team1 = Team("Attackers", 80, 20)
    team2 = Team("Defenders", 30, 70)
    team3 = Team("Averages", 50, 50)

    teams.append(team1)
    teams.append(team2)
    teams.append(team3)


def show_teams():
    print("Information of all teams")
    for index, team in enumerate(teams):

        print(f"{index+1}", end=" ")
        team.info()


def choice_team(player):
    try:
        choice = int(input(f"Select {player} team (1-3): "))
    except ValueError:
        print("Input must be an integer")
        return

    if choice not in [1, 2, 3]:
        print("Choice must be between 1 and 3")
        return

    selected_team = teams[choice - 1]

    if player == "myself":
        playing_teams["myself"] = selected_team
        print(f"Your team is '{selected_team.name}'")
    else:
        playing_teams["enemy"] = selected_team
        print(f"Opponent's team is '{selected_team.name}'")


def get_play_inning(inning):
    if inning == "top":
        offense = playing_teams["myself"]
        defense = playing_teams["enemy"]
    else:
        offense = playing_teams["enemy"]
        defense = playing_teams["myself"]

    # Use randomness per inning
    score = math.floor((offense.get_hit_rate() - defense.get_out_rate()) / 10)

    if score < 0:
        score = 0
    return score


def show_scoreboard(you, opponent, you_scores, opponent_scores):
    print("________|" + "|".join(f"{i:^3}" for i in range(1, 10)) + "| R |")

    print(f"{'You':<8}|", end="")
    for score in you_scores:
        print(f"{score:^3}|", end="")
    print(f"{you.total_score:^3}|")

    print(f"{'Opponent':<8}|", end="")
    for score in opponent_scores:
        print(f"{score:^3}|", end="")
    print(f"{opponent.total_score:^3}|")


def play():
    you = playing_teams["myself"]
    opponent = playing_teams["enemy"]

    you_scores = []
    opponent_scores = []

    for i in range(9):
        top_score = get_play_inning("top")
        you_scores.append(top_score)
        you.total_score += top_score

        if i == 8 and opponent.total_score > you.total_score:
            opponent_scores.append("X")
            break

        bottom_score = get_play_inning("bottom")
        opponent_scores.append(bottom_score)
        opponent.total_score += bottom_score

    show_scoreboard(you, opponent, you_scores, opponent_scores)


# make teams
create_teams()

# show all teams
show_teams()
choice_team("myself")
choice_team("enemy")
play()
