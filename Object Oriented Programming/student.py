class Student:
    def __init__(self, name, grade, age, school, teacher):
        self.name = name
        self.grade = grade
        self.age = age
        self.school = school
        self.teacher = teacher
        self.scores = []
    
    def display(self):
        print(f"    STUDENT CARD\n----\nname: {self.name}\ngrade: {self.grade}\nage: {self.age}\nschool: {self.school}\nteacher: {self.teacher}\nscores:{self.scores}")

    def change_detail(self):
        subjects = int(input("How many subjects do you have?"))
        for i in range(1, subjects+1):
            score = int(input(f"What is your score in class {i}?"))
            self.scores.append(score)
s1 = Student("Riddhima", "7th","12", "Cool place", "Ms. Cool teacher")
s2 = Student("Poop", "Kindergarten", "8", "Poopoo academy for poopoos", "Ms. I don't know what to put here")
s1.change_detail()
s2.change_detail()
s1.display()
s2.display()