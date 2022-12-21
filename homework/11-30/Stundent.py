class Student:
    school = "nsu"

    def __init__(self, name, sex, major, country="中国"):
        self.name = name
        self.sex = sex
        self.major = major
        self.country = country

    @classmethod
    def get_school(cls):
        return cls.school

    def change_major(self,major):
        self.major = major
