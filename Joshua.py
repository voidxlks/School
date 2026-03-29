class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.enrolled = False

    def enroll(self):
        self.enrolled = True
        print(f"{self.name} is now enrolled in voidxlks school!")

    def add_grade(self, grade):
        if not self.enrolled:
            print("Student is not enrolled.")
            return
        self.grades.append(grade)
        print(f"Added grade {grade} for {self.name}")

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        print("\n--- Student Info ---")
        print(f"Name: {self.name}")
        print(f"Enrolled: {self.enrolled}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.average_grade():.2f}")


# Create Joshua student
joshua = Student("Joshua")

# Simulate school actions
joshua.enroll()
joshua.add_grade(85)
joshua.add_grade(92)
joshua.add_grade(78)

# Show info
joshua.info()
