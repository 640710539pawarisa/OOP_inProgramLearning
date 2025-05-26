#ฟังกืชั่นเกี่ยวกับ Class และ Object หรือ ฟังก์ชั่นเพิ่มเติม หรือฟังก์ชันเสริม

#*******************
#เราอยากเช็คว่า object ถูกนิยามจาก class employee หรือไม่
#หรือเช็คว่า obj1 มี Attribute อะไรบ้าง

class Employee: #สร้างคลาส ชื่อEmployee 
    
#defult constructor ค่าเริ่มต้น คือไม่ปรับเปลี่ยนโครงสร้างด้านใน method

    def __init__(self): #สร้าง constructor ที่ไม่มีการส่งค่าอะไรเข้ามา
        print("Default Constructor")

#constructor ที่มีการส่งค่าอะไรเข้ามา  ,มีการปรับเปลี่ยนค่าด้านใน method
    def __init__(self,name,salary,position): #สร้าง constructor , underscore 2ตัว แล้วinit แล้วก็ underscore 2ตัว
            # print("Default Constructor")
            # #มันจะแสดง คำว่า Default Constructor 3 ครั้งเพราะเราสร้าง object 3 ตัว
            self.name = name #self.name คือ attribute ชื่อ่ name ,attribute คือ ค่าที่เรากําหนดไว้ หรือคุณสมบัติ
            self.salary = salary
            self.position = position
    
#สร้าง Method ชื่อ showdata มาเพื่อ แสดงผลอย่างเดียว  จะแสดงผลของ object โดยมี attribute ชื่อ name และ salary และ position

    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("----------------------")
        print("เงินเดือน = {}".format(self.salary))
        print("----------------------")
        print("ตําแหน่ง = {}".format(self.position))
        print("----------------------")
        
#การนิยาม Destructor คือ สั่งให้ object นั้นหายไป หรือลบออกจากโครงสร้าง ,คือการคืนค่าให้หน่วยความจำ

#************ไม่จำเป็นต้องระบุก็ได้
    def __del__(self): #สร้าง destructor ที่ไม่มีการส่งค่าอะไรเข้ามา 
        # print("Call Destructor") 
        pass
        
#การสร้าง วัตถุ หรือ object จากคลาส Employee
#สามารถปรับเปลี่ยนค่าได้ เช่น obj1.name = "เอ๊ะ"
#คนที่ 1
obj1 = Employee("เอ๊ะปวาริษา",50000,"โปรแกรมเมอร์")  #สร้างวัตถุ ชื่อobj1 จากคลาส Employee และส่งค่าเข้าไป
#ปรับเปลี่ยนค่า
obj1.name = "เอ๊ะ"
#คนที่ 2
obj2 = Employee("โคล่า",40000,"พนักงานขาย")  #สร้างวัตถุ ชื่อobj2 จากคลาส Employee
#คนที่ 3
obj3 = Employee("เซเว่น",35000,"พนักงานบัญชี")  #สร้างวัตถุ ชื่อobj3 จากคลาส Employee


#******
#วิธีเช็ค
print(isinstance(obj1,Employee)) 
#ตรวจสอบว่า obj1 มาจากคลาส Employee หรือไม่ ถ้าเป็น True จะแสดงว่า obj1 มาจากคลาส Employee

print("------------------")

#หรือเช่น ช้าง เป็น สัตว์ป่า หรือเปล่า

#เช็คว่า obj1 มี attribute อะไรบ้าง
print(dir(obj1)) 

print("------------------")

#หรือ obj1 มี method ชื่อ showdata  หรือไม่  ถ้าเป็น True จะแสดงว่า obj1 มี method showdata หรือไม่
print(dir(obj1.showdata))

print("------------------")

#ส่วนของ class
#เช็คว่า obj1 อยู่ที่ class อะไร หรือ เช็คว่า obj1 อยู่ที่ class Employee หรือไม่
print(obj1.__class__)

print("------------------")