class student:
    def __init__(self, name, branch, gpa):
        self.name = name
        self.branch = branch
        self.gpa = gpa

    def is_topper(self):
        if self.gpa >= 8:
            return True
        else:
            return False
        