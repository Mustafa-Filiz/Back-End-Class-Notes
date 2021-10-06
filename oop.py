import os
os.system("cls" if os.name == "nt" else "clear")

# def printtype(data):
#     for i in data:
#         print(i, type(i))


# test =[123, "Barry", [1,2,3], (1,2,3), {1,2,3}, True, lambda x: x,{
#     "name": "henry", "age": 38
# }]

# printtype(test)

# Defining Class

# class Person:
#     name = "Barry"
#     age = 44

# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.name)

# Person.job = "teacher"
# print(person1.job)
# print(person2.job)


#  Class attributes ve instance attributes

# Person.name = "Rafael"
# person1.name = "Henry"
# print(person1.name)
# print(person2.name)

# SELF keyword

# class Person:
#     name = "Barry"
#     age = 44
#     def test(self):
# 	    print("test")

#     def get_details(self):
# 	    print("name: ", self.name, "age: ", self.age , "location: ", self.location)

#     def set_details(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location

# person1 = Person()
# person1.test()
# Person.test(person1)
# person1.set_details("Henry", 38, "Ankara")
# person1.get_details()


# class Person:
#     name = "Barry"
#     age = 44

#     def test(self):
#         print("test")

#     def get_details(self):
#         print("name: ", self.name, "age: ",
#               self.age, "location: ", self.location)

#     def set_details(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location

#     @staticmethod
#     def salute():
#         print("Hi there! ", Person.name)

# Person.salute()
# person1 = Person()
# person1.salute()


# Special methods

# class Person:
# 	company = "Clarusway"

# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def __str__(self):
# 		return f"Name : {self.name}   Age: {self.age}"

# 	def __len__(self):
# 		return self.age

# person1 = Person("Barry", 44)
# print(person1.name, person1.age)

# lst = [1,2,3]
# print(len(lst))
# print(len(person1))

# abstraction and encapsulation

# lst = [3,2,5,9,1]
# lst.sort()
# print(lst)

# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000
#         self.__id1 = 4000

#     def __str__(self):
#         return f"Name: {self.name}  Age: {self.age}"

# person1 = Person("Rafe", 39)
# person1._id = 3000
# print(person1._id)
# print(person1.__id1)

# class Person:
#     company = "Clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Name: {self.name}  Age: {self.age}"


# class Employee(Person):
#     def __init__(self, name, age, path):
#         self.name = name
#         self.age = age
#         self.path = path


# emp1 = Employee("Barry", 44, "FS")
# print(emp1)


# inheritance and polymorphise

class Person:
    company = "Clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}  Age: {self.age}"

class Lang:
	def __init__(self, langs):
		self.langs = langs


class Employee(Person, Lang):
    def __init__(self, name, age, path):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        self.path = path

    def __str__(self):
        return f"Name: {self.name}  Age: {self.age}   Path: {self.path}"


emp1 = Employee("Barry", 44, "FS")
print(emp1)

print(Employee.mro())