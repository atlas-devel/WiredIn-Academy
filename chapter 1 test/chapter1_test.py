    import random


    def is_correct_input(input):
        return input in [0, 1]


    def get_coin_side() -> int:
        return random.choice([0, 1])


    def get_side_name(toss) -> str:
        return "head" if toss == 0 else "tail"


    def view_side(my_side_name: str, coin_side_name: str):
        print(f"My bet is {my_side_name}")
        print(f"Coin is {coin_side_name}")


    def get_result(my_side, coin_side) -> str:
        return "Win" if my_side == coin_side else "Lose"


    def view_result(decision):
        print(decision)


    def play():
        print("Start 'coin toss' ")
        print("Input your bet")

        while True:
            try:
                player_input = int(input("0:head, 1:tail ->> "))
            except ValueError:
                print("Error: input should be numbers")
                continue
            descision = is_correct_input(player_input)
            if descision:
                break

            print("Bad input, please choose 1 or 0")

        computer_coin_side = get_coin_side()

        my_side = get_side_name(player_input)
        coin_side = get_side_name(computer_coin_side)
        view_side(my_side, coin_side)

        final_decision = get_result(player_input, computer_coin_side)
        view_result(final_decision)


    play()
