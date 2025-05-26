#การสร้าง Attribute  และ method ใน Python

#เราจะทำการสร้างclass employeeสำหรับเก็บข้อมูลพนักงาน โดยมีพนักงานบัญชี ,โปรแกรมเมอร์ ,พนักงานขา 
# และจะมีคุณสมบัติต่างๆเพิ่มเติมตามต้องการและจะมีmethodต่างๆเพิ่มเติมตามต้องการหรือเรียกว่า functions ต่าง ๆ

#พนักงาน มี ชื่อ ,เงินเดือน 
class Employee: #สร้างคลาส ชื่อEmployee 
    #สร้าง method  **********************
    def detail(self):  #สร้าง method ชื่อdetail ,มันเหมือนการสร้าง function เลย ,self คือ วัตถุตัวเอง สร้างมาเพื่อ บอกว่าส่วนนี้คือ method
        # print("เรียกใช้งาน method detail ใน class Employee")
        
        #เรียกใช้งาน method name ใน class Employee
        self.name = "เอ๊ะปวาริษา"
        self.salary = "50000"#self.salary คือ เรียกใช้งาน method ชื่อ self จุด กำหนดชื่อว่า salary และส่งค่ามาเป็น 40000
        self.position = "โปรแกรมเมอร์"
        print("ชื่อพนักงาน = {}".format(self.name))  #={}.format() คือการส่งค่ามาเป็นตัวแปร 
        #,format(self.name) คือส่งค่ามาเป็นตัวแปรชื่อ name ที่มีค่าเป็นชื่อ "เอ๊ะปวาริษา" ที่เรากําหนดไว้
        print("เงินเดือน = {}".format(self.salary))
        print("ตําแหน่ง = {}".format(self.position))  
    

#การสร้าง วัตถุ หรือ object จากคลาส Employee
emp1 = Employee()  #สร้างวัตถุ ชื่อemp1 จากคลาส Employee

emp1.detail() #เรียกใช้งาน method detail ใน class Employee
