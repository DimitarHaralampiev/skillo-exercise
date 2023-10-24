class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def __str__(self):
        return f'Student info: {self.name} {self.age}'


student_info = input('Please enter name and age ').split()
student = Student(student_info[0], student_info[1])
print(student.name)
print(student.age)
