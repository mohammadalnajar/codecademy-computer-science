class Student:
    def __init__(self):
        self.grade = 0
        self.attendance = 0
        self.is_passed = True if self.grade >= 55 else False
        self.classes = []
        self.assignments = []

    def __repr__(self):
        single_plural = (
            "class" if len(self.classes) == 1 else "classes"
        )  # if there is only one class, use "class"

        return f"{self.name} is {self.age} years old and is in grade {self.grade}. He has {self.attendance} attendance and is in {len(self.classes)} {single_plural}."

    # add a student
    def add_student(self):
        name, age = input(
            "Enter student name and age (please split your answers with spaces): "
        ).split()
        self.name = name
        self.age = int(age)

        print(f"{self.name} who is {self.age} years old has been added to the school")

        return self

    # a student can take a class
    def take_class(self, class_to_take):
        if class_to_take not in self.classes:
            self.classes.append(class_to_take)
            class_to_take.add_student(self)  # add student to class
            print(f"{self.name} has taken {class_to_take.name}")
        else:
            print(f"{self.name} is already in {class_to_take.name}")

    # a student can leave a class
    def leave_class(self, class_to_leave):
        if class_to_leave in self.classes:
            self.classes.remove(class_to_leave)
            class_to_leave.remove_student(self)  # remove student from class
            print(f"{self.name} has left {class_to_leave.name}")
        else:
            print(f"{self.name} is not in {class_to_leave.name}")

    def attend_class(self, class_to_attend):
        if class_to_attend in self.classes:
            self.attendance += 1
            print(f"{self.name} has attended {class_to_attend.name}")
        else:
            print(f"{self.name} is not in {class_to_attend.name}")

    # a student can submit a assignment
    def submit_assignment(self, assignment_to_submit, grade):
        if assignment_to_submit not in self.assignments:
            assignment = {}
            assignment["assignment"] = assignment_to_submit
            assignment["grade"] = grade
            assignment_to_submit.add_student(self)  # add student to assignment

            print(f"{self.name} has submitted {assignment_to_submit.name} assignment")

            if grade >= assignment_to_submit.min_grade_to_pass:
                self.grade += grade
                assignment["is_passed"] = True
                self.assignments.append(assignment)
                print(
                    f"{self.name} has passed the {assignment_to_submit.name} assignment with {grade} points"
                )
            else:
                self.grade += grade
                assignment["is_passed"] = False
                self.assignments.append(assignment)
                print(
                    f"{self.name} has failed the {assignment_to_submit.name} assignment with {grade} points"
                )
        else:
            print(
                f"{self.name} has already submitted this {assignment_to_submit.name} assignment"
            )


class Class:
    def __init__(self):
        self.teacher = None
        self.students = []

    def __repr__(self):
        print(f"{self.name} has {len(self.students)} students")

    # add a class
    def add_class(self):
        name, max_students = input(
            "Enter a new class name and max students number (please split your answers with spaces): "
        ).split()

        error = {"msg": "test"}
        print(type(name))
        print(type(max_students))

        while True:
            try:
                if not max_students.isnumeric():
                    error["msg"] = "Max students number must be an integer"
                    raise ValueError

                max_students = int(max_students)
                if max_students < 1:
                    error["msg"] = "Max students number must be greater than 0"
                    raise ValueError
                if name.isnumeric():
                    error["msg"] = "Class name must be only letters"
                    raise ValueError
                break
            except ValueError:
                msg = error["msg"] if "msg" in error else "Invalid input"
                print(f"Error: {msg}")
                name, max_students = input(
                    "Enter a new class name and max students number (please split your answers with spaces): "
                ).split()

        self.name = name
        print(f"{self.name} class has been added to the school")

        return self


print("====================================")
print("Welcome to the High School Simulator")
print("====================================")

class_one = Class().add_class()
student_one = Student().add_student()

print(student_one)

print("1" == 1)
# a class can add a student
# a class can remove a student
# a class has a name
# a class has a mandatory attendance
# a class has a min grade to pass
# a class has a teacher
# a class has a list of students
# a class has a list of assignments
# a class can add an assignment
# a class can remove an assignment


# an assignment has a name
# an assignment has a min grade to pass
# an assignment has a teacher
# an assignment has a list of students
