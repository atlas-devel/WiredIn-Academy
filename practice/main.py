class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"hello I am {self.name}")


class Student(Person):
    def __init__(self, name, grades):
        super().__init__(name)
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def display(self):
        print(f"{self.name}: Grades: {self.grades} | Average:{self.average():.2f} ")


class ClassRoom:
    def __init__(self):
        self.students = []

    def add_student(self, single_student):

        self.students.append(single_student)

    def highest_per_subject(self):
        if len(self.students) == 0:
            raise ValueError("students can't be empty")

        student_count = len(self.students[0].grades)
        highest_grades_per_subject = []
        for i in range(student_count):
            highest_grades_per_subject.append(
                max(student.grades[i] for student in self.students)
            )

        return highest_grades_per_subject

    def display(self):
        for student in self.students:
            student.display()
        print(f"the highest grade: {self.highest_per_subject()}")


student_names = ["leon", "anne", "bob"]
student_grades = [[30, 21, 40], [53, 55, 21], [89, 32, 66]]

classroom = ClassRoom()

for names, grades in zip(student_names, student_grades):
    classroom.add_student(Student(names, grades))

classroom.display()
