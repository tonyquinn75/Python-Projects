# Author:Anthony Quinn
# Date: 30/8/19
# Description:Python classes, creation, use, sub classing, overriding,overloading explained.
# A class can repersent a purpose build, define my own data type.
from Student import Student

student1 = Student("Jim", "Business", 3.7, True)
student2 = Student("Bob", "Accounting", 3.1, True)
print(student1.name)
print(student1.major)
print(student1.gpa)
print(student1.is_on_probation)
print(student1.on_honour_roll())
print(student2.on_honour_roll())
