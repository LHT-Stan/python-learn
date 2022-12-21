class Student:
    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score
        

student = Student(10)
student.score()
print(student.score())


