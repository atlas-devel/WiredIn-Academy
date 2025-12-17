import random
import math

level = 1
data = [["A", "F"], ["U", "V"], ["W", "M"]]
columns = ["A", "B", "C"]
col_dict = {"A": 0, "B": 1, "C": 2}


unique_position = random.randint(0, 8)


def section_message():
    print(f"Level: {level}")


def view_question():
    selected_array = data[random.randint(0, 2)]

    print(selected_array)

    current_position = 0
    row_number = 1

    print("/| " + "".join(columns))
    print("-------")

    for _ in range(3):
        line = ""
        for y in range(3):
            if current_position == unique_position:
                line += selected_array[1]
            else:
                line += selected_array[0]
            current_position += 1
        print(f"{row_number}| {line}")
        row_number += 1


def change_input_number(input_str):
    x, y = list(input_str)
    column = col_dict[x]
    row = int(y) - 1
    return row * 3 + column


def is_correct(mistake_number, guessed_position):
    print("Correct!") if mistake_number == guessed_position else print("Wrong")


def change_string(number):
    row = math.floor(number / 3)
    column = [key for key, value in col_dict.items() if value == number % 3]
    correct_cell = f"{column[0]}" + f"{row}"
    print(f"Correct answer is {correct_cell}")
    return correct_cell


def start_message():
    print("Input cell number (e.g. A1) of different character.")
    section_message()
    mistake_number = int(unique_position)
    print(f"Debug: mistake_number = {mistake_number}")

    view_question()

    mistake_guess = input("Debug: choice = ")
    guess_position = change_input_number(mistake_guess)

    print("(E.g. A1) A1")
    print(f"Debug: input_number = {guess_position}")
    is_correct(mistake_number, guess_position)
    change_string(mistake_number)


def play():
    start_message()


play()
