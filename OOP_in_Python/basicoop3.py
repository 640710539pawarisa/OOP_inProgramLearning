#การกำหนดค่า Attribute ให้กับ object

#สิ่งที่เราอยากทำคือ เพิ่มพนักงานมาเพิ่มเติม อยากปรับเปลี่ยนชื่อพนักงาน อยากปรับเปลี่ยนเงินเดือน อยากปรับเปลี่ยนตําแหน่ง เป็นคนละคน

#แบบที่ 1
class Employee: #สร้างคลาส ชื่อEmployee 
    #สร้าง method  **********************
    def detail(self,name,salary,position):  #สร้าง method ชื่อdetail ,มันเหมือนการสร้าง function เลย 
        # self คือ วัตถุตัวเอง สร้างมาเพื่อ บอกว่าส่วนนี้คือ method
        # print("เรียกใช้งาน method detail ใน class Employee")
        
        #เรียกใช้งาน method name ใน class Employee
        self.name = name #self.name คือ attribute ชื่อ name ,attribute คือ ค่าที่เรากําหนดไว้ หรือคุณสมบัติ
        self.salary = salary  #self.salary คือ เรียกใช้งาน method ชื่อ self จุด กำหนดชื่อว่า salary และส่งค่ามาเป็น 50000
        self.position = position
        print("ชื่อพนักงาน = {}".format(self.name))  #={}.format() คือการส่งค่ามาเป็นตัวแปร 
        #,format(self.name) คือส่งค่ามาเป็นตัวแปรชื่อ name ที่มีค่าเป็นชื่อ "เอ๊ะปวาริษา" ที่เรากําหนดไว้
        print("เงินเดือน = {}".format(self.salary))
        print("ตําแหน่ง = {}".format(self.position))  
    

#การสร้าง วัตถุ หรือ object จากคลาส Employee
#คนที่ 1
obj1 = Employee()  #สร้างวัตถุ ชื่อobj1 จากคลาส Employee

obj1.detail("เอ๊ะปวาริษา",50000,"โปรแกรมเมอร์") #เรียกใช้งาน method detail ใน class Employee 
#เรียกใช้งาน method name ใน class Employee,ส่งค่ามาเป็นตัวแปร ชื่อ name และ salary ,และส่งค่ามาเป็นตัวแปร position

#คนที่ 2
obj2 = Employee()  #สร้างวัตถุ ชื่อobj2 จากคลาส Employee

obj2.detail("โคล่า",40000,"พนักงานขาย") #เรียกใช้งาน method detail ใน class Employee

#คนที่ 3
obj3 = Employee()  #สร้างวัตถุ ชื่อobj3 จากคลาส Employee

obj3.detail("เซเว่น",35000,"พนักงานบัญชี") #เรียกใช้งาน method detail ใน class Employee

print("-------------------------------------------------------------------------")
#---------------------------------------------------------------------------------

#แบบที่ 2

class Employee: #สร้างคลาส ชื่อEmployee 
    #สร้าง method  **********************
    def detail(self,name,salary,position):  #สร้าง method ชื่อdetail ,มันเหมือนการสร้าง function เลย 
        # self คือ วัตถุตัวเอง สร้างมาเพื่อ บอกว่าส่วนนี้คือ method
        # print("เรียกใช้งาน method detail ใน class Employee")
        
        #เรียกใช้งาน method name ใน class Employee
        self.name = name #self.name คือ attribute ชื่อ name ,attribute คือ ค่าที่เรากําหนดไว้ หรือคุณสมบัติ
        self.salary = salary  #self.salary คือ เรียกใช้งาน method ชื่อ self จุด กำหนดชื่อว่า salary และส่งค่ามาเป็น 50000
        self.position = position
        
#สร้าง Method ชื่อ showdata มาเพื่อ แสดงผลอย่างเดียว  จะแสดงผลของ object โดยมี attribute ชื่อ name และ salary และ position

    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("----------------------")
        print("เงินเดือน = {}".format(self.salary))
        print("----------------------")
        print("ตําแหน่ง = {}".format(self.position))
        print("----------------------")
        
        
#การสร้าง วัตถุ หรือ object จากคลาส Employee

#คือการส่งค่าเข้าไปใน method detail ผ่าน parameter หรือส่งข้อมูลที่เราอยากจะที่แสดง
#คนที่ 1
obj1 = Employee()  #สร้างวัตถุ ชื่อobj1 จากคลาส Employee

obj1.detail("เอ๊ะปวาริษา",50000,"โปรแกรมเมอร์") #เรียกใช้งาน method detail ใน class Employee 
#เรียกใช้งาน method name ใน class Employee,ส่งค่ามาเป็นตัวแปร ชื่อ name และ salary ,และส่งค่ามาเป็นตัวแปร position

#คนที่ 2
obj2 = Employee()  #สร้างวัตถุ ชื่อobj2 จากคลาส Employee

obj2.detail("โคล่า",40000,"พนักงานขาย") #เรียกใช้งาน method detail ใน class Employee

#คนที่ 3
obj3 = Employee()  #สร้างวัตถุ ชื่อobj3 จากคลาส Employee

obj3.detail("เซเว่น",35000,"พนักงานบัญชี") #เรียกใช้งาน method detail ใน class Employee

#แบบที่ 3
#ส่วนของแสดงผลลัพธ์
obj1.showdata() #เรียกใช้งาน method showdata ใน class Employee

obj2.showdata() #เรียกใช้งาน method showdata ใน class Employee

obj3.showdata() #เรียกใช้งาน method showdata ใน class Employee