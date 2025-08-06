class student:
    def __init__(self, name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

student1 = student("John", 2)
student1.display()