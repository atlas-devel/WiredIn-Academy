Smartphones = []
data = [
    ("Android", 60, "red"),
    ("iPhone", 50, "blue"),
    ("Android", 70, "white"),
    ("Android", 50, "black"),
    ("Android", 60, "purple"),
    ("iPhone", 60, "black"),
    ("Android", 50, "green"),
    ("iPhone", 70, "yellow"),
    ("iPhone", 80, "purple"),
    ("Android", 60, "yellow"),
]


class SmartPhone:
    def __init__(self, phone_type, size, color):
        self.type = phone_type
        self.size = size
        self.color = color

    def display_info(self):
        print(f"type:{self.type} size:{self.size} color:{self.color}")


def create_list():
    for phone_type, size, color in data:
        Smartphones.append(SmartPhone(phone_type, size, color))


create_list()

for phone in Smartphones:
    phone.display_info()
