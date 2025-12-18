import random
import math
import string

level = 1
rows = 4
column = 5

data = [["A", "F"], ["U", "V"], ["W", "M"]]
column_list = string.ascii_uppercase[:column]
col_dict = {letter: index for index, letter in enumerate(column_list)}


unique_position = random.randint(0, (rows * column) - 1)


def section_message():
    print(f"Level: {level}")


def view_question():
    selected_array = data[random.randint(0, 2)]

    print(selected_array)

    current_position = 0
    row_number = 1

    print("/| " + "".join(column_list))
    print("-" * (len(column_list) + 6))

    for _ in range(rows):
        line = ""
        for y in range(column):
            if current_position == unique_position:
                line += selected_array[1]
            else:
                line += selected_array[0]
            current_position += 1
        print(f"{row_number}| {line}")
        row_number += 1


def change_input_number(input_str):
    x, y = list(input_str)
    column_part = col_dict[x.upper()]
    row_part = int(y) - 1
    return row_part * column + column_part


def is_correct(mistake_number, guessed_position):
    print("Correct!") if mistake_number == guessed_position else print("Wrong")


def change_string(number):
    row = math.floor(number / column) + 1
    col_letter = column_list[number % column]
    correct_cell = f"{col_letter}" + f"{row}"
    print(f"Correct answer is {correct_cell}")
    return correct_cell


def start_message():
    print("Input cell number (e.g. A1) of different character.")
    section_message()
    mistake_number = int(unique_position)
    print(f"Debug: mistake_number = {mistake_number}")

    view_question()
    print("(E.g. A1) A1")
    mistake_guess = input("Debug: choice = ")
    guess_position = change_input_number(mistake_guess)

    print(f"Debug: input_number = {guess_position}")
    is_correct(mistake_number, guess_position)
    change_string(mistake_number)


def play():
    start_message()


play()
