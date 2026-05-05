class GroupFullException(Exception):
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, {self.gender}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, {self.gender}, {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullException("Group is full")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ""

        for student in self.group:
            all_students += str(student) + "\n"

        return f"Number:{self.number}\n{all_students}"


gr = Group("PD1")

students = [
    Student("Male", 20, "Steve", "Jobs", "AN142"),
    Student("Female", 21, "Liza", "Taylor", "AN145"),
    Student("Male", 22, "John", "Brown", "AN146"),
    Student("Female", 23, "Anna", "White", "AN147"),
    Student("Male", 24, "Mike", "Green", "AN148"),
    Student("Female", 25, "Sara", "Black", "AN149"),
    Student("Male", 26, "Tom", "Wilson", "AN150"),
    Student("Female", 27, "Emma", "Moore", "AN151"),
    Student("Male", 28, "Chris", "Hall", "AN152"),
    Student("Female", 29, "Kate", "King", "AN153"),
    Student("Male", 30, "Alex", "Young", "AN154")
]

for student in students:
    try:
        gr.add_student(student)
        print(f"Student {student.last_name} added")
    except GroupFullException as e:
        print(e)

print(gr)