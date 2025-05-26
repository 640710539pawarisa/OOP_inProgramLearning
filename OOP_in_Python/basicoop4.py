#ตัวสร้าง constructor
#เอามาจาก basicoop3.py ,มาจากเรื่อง #การกำหนดค่า Attribute ให้กับ object

#สิ่งที่เราอยากทำคือ เพิ่มพนักงานมาเพิ่มเติม อยากปรับเปลี่ยนชื่อพนักงาน อยากปรับเปลี่ยนเงินเดือน อยากปรับเปลี่ยนตําแหน่ง เป็นคนละคน

#แบบที่ 2

class Employee: #สร้างคลาส ชื่อEmployee 
    
#***เพิ่มส่วนนี้

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
        print("Call Destructor") 
        
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

#แสดงผล
obj1.showdata() #เรียกใช้งาน method showdata ใน class Employee
obj2.showdata() #เรียกใช้งาน method showdata ใน class Employee
obj3.showdata() #เรียกใช้งาน method showdata ใน class Employee