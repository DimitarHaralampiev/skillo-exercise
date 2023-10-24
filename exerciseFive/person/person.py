class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Person Information: {self.first_name} {self.last_name} - {self.age}'


person_info = input('Please enter first name, last name and age ').split()
person = Person(person_info[0], person_info[1], person_info[2])
print(person)