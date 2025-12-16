import random

level = 1
data = [["A", "F"], ["U", "V"], ["W", "M"]]


def section_message():
    print(f"Level: {level}")


def view_question():
    selected_array = data[random.randint(0, 2)]
    unique_position = random.randint(0, 8)

    print(selected_array)

    current_position = 0

    for _ in range(3):
        line = ""
        for y in range(3):
            if current_position == unique_position:
                line += selected_array[1]
            else:
                line += selected_array[0]
            current_position += 1
        print(line)


def start_message():
    print("Input cell number (e.g. A1) of different character.")
    section_message()
    print("Debug: mistake_number = 2")
    view_question()
    print("(E.g. A1) A1")
    print("Debug: choice = A1")


def play():
    start_message()


play()
