class Student:
    # Constructor
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.__content = None
    # To get name
    def getName(self):
        return self.name
    def getId(self):
        return self.id
# To check if this person is employee
    def isGrade(self):
        return False
# Inherited or Sub class (Note Person in bracket)
class Subject(Student):
    def __init__(self, name,id):
        self.name=name
        self.id=id

    # Here we return true
    def isSubject(self):
        return True
class Grade(Subject):
    def __init__(self, name, id):
        self.name=name
        self.id=id
class Status():
            def __init__(self, name, id):
                self.name = name
                self.id = id
class Result(Student):
    def __init__(self, name, id):
     super()
     self.name = name
     self.id = id
    def isSubject(self):
            return True
emp = Student("Geek1","3")  # An Object of Employee
print(emp.getName(),emp.getId(), emp.isGrade())