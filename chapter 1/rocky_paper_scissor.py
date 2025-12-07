import random
import sys

hands = ["rock", "scissors", "paper"]
results = {"win": "you win", "lose": "you lose", "draw": "draw try again"}


# computer hand
def start_message():
    print("Start ‘rock-paper-scissors’ game")


def get_computer():
    return random.randint(0, 2)


# player hand
def get_player():
    while True:
        try:
            print()
            print("input your hand")
            player_hand_choice = int(input("0=rock, 1=scissors, 2=paper >>> "))
            if player_hand_choice in [0, 1, 2]:
                return player_hand_choice

            elif player_hand_choice > 2:
                print("input is out range")

        except ValueError:
            print()
            print("invalid input")
            replay = ""
            while replay.lower() != "r":
                replay = input("Press click R to start / Q to quit > ")
                if replay.lower() == "q":
                    print("Exiting...")
                    sys.exit()


def view_result(player_hand, computer_hand):
    if player_hand == computer_hand:
        return "draw"

    elif (
        player_hand == 0
        and computer_hand == 1
        or player_hand == 1
        and computer_hand == 2
        or player_hand == 2
        and computer_hand == 0
    ):
        return "win"
    else:
        return "lose"


def get_hand_name(hand_number):
    return hands[hand_number]


def view_hand(player_hand_number, computer_hand_number):
    print(f"My hand is {get_hand_name(player_hand_number)}")
    print(f"Rival's hand is {get_hand_name(computer_hand_number)}")


def get_result(show_result):
    return results[show_result]


def play_game():
    # rock
    player = get_player()
    computer = get_computer()

    # showing player hands
    view_hand(player, computer)

    # passing arguments to view_result function
    game_result = view_result(player, computer)

    # showing result
    print(get_result(game_result))

    if game_result == "draw":
        play_game()


start_message()
play_game()
