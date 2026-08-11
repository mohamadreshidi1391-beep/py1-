class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):
        print(self.name, "-", self.age, "سال", "-", "نمره:", self.grade)

# ساخت چند شیء (دانش‌آموز)
student1 = Student("علی", 10, 18)
student2 = Student("سارا", 11, 20)
student3 = Student("رضا", 10, 19)

# نمایش اطلاعات
student1.show_info()
student2.show_info()
student3.show_info()