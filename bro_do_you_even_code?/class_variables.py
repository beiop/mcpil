class Student:
    
    class_year = 2024
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob",30)
student2 = Student("Patrick",55)


print(Student.class_year)
print(Student.num_students)