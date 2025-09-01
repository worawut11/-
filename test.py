# คลาสพื้นฐาน Person
class Person:
    def __init__(self, name, age):
        self.name = name    # เก็บชื่อ
        self.age = age      # เก็บอายุ

    def show_info(self):
        print(f"ชื่อ: {self.name}")
        print(f"อายุ: {self.age}")


# คลาส Student ที่สืบทอดจาก Person
class Student(Person):
    def __init__(self, name, age, studentID):
        # ใช้ super() เพื่อเรียก constructor ของคลาสแม่
        super().__init__(name, age)
        self.studentID = studentID   # เก็บรหัสนักเรียน

    # เมธอดแสดงข้อมูลทั้งหมด
    def show_info(self):
        super().show_info()  # เรียกการแสดงจาก Person ก่อน
        print(f"รหัสนักศึกษา: {self.studentID}")


# ----------- การใช้งาน ------------
# สร้างอ็อบเจ็กต์ Student
stu1 = Student("สมชาย", 20, "ST12345")

# แสดงข้อมูลทั้งหมด
stu1.show_info()
