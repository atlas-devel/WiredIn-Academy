teams = []


class Team:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def info(self):
        print(
            f"{self.name}: offensive power: {self.attack} / defensive power: {self.defense}"
        )


def create_teams():
    global teams

    team1 = Team("attackers", 80, 20)
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
        player_team = int(input("Select your team (1-3)"))
    except ValueError:
        print("input should be integer number")
        return

    if player_team not in [1, 2, 3]:
        print("player team should be in range of 1-3")
        return


# make teams
create_teams()

# show all teams
show_teams()
