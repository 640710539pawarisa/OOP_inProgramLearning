#super class
#ระบุ class แม่ และกำหนดการทำงานให้กับ class ย่อย
#ใส่ชื่อและเงินเดือน ใน parameter constructor __init__ ในคลาสย่อย
class Employee: # class แม่
    #class variable มันเป็น public  
    
    minsalary = 12000 #min salary คือเงินเดือนต่ําสุด
    maxsalary = 80000 #max salary #คือเงินเดือนสูงสุด
    companyname = "บริษัท xyz จำกัด" 
    
    def __init__(self,name,salary,position):
        #instance variable , ขอบเขตของชื่อและเงินเดือน และตําแหน่ง
        #private attribute
        self.__name = name
        self.__salary = salary
        self.__position = position
        
        #note : จะถูกเข้าถึงได้ก็ต่อเมื่อ สร้างวัตถุ จาก class Employee
        
    #private method
    def _showdata(self): 
#ใส่ _ ด้านหน้าชื่อ methodเป็นการบอกว่าเป็น protected ถ้าเอา _ ออกจะเป็นแบบ public หรือใส่ __ ด้านหน้าชื่อ methodเป็นการบอกว่าเป็น private
        print("ชื่อพนักงาน = ",self.__name)
        print("----------------------")
        print("เงินเดือน = ",self.__salary)
        print("----------------------")
        print("ตําแหน่ง = ",self.__position)
        print("----------------------")
        
#สร้าง class สืบทอดคุณสมบัติ 
#class ลูก

class Accountant(Employee): #สืบทอดคุณสมบัติมาจาก Employee ชื่อ class ว่า่ Accountant
    #สร้าง constructorภายในคลาสลูก เพื่อไม่ให้ตอนสร้าง object ไม่ต้องไปเอาconstructor จาก class แม่***
    
    #เขียนชื่อ แผนก
    __position = "แผนกบัญชี"
    def __init__(self,name,salary,position): #เพิ่ม parameter ที่จะส่งเข้าไป***ในconstructor
        super().__init__(name,salary,position) #สืบทอดคุณสมบัติมาจาก Employee  *****เพิ่มส่วนนี้
        super()._showdata()#คือเรียกใช้ method ชื่อ _showdataจากคลาสแม่โดยใช้คําสั่ง super
    
class Manager(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกผู้จัดการ"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self,name,salary,position):
        super().__init__(name,salary,position) 
#super() สืบทอดคุณสมบัติมาจาก Employee,._init__ สืบทอดคุณสมบัติมาจาก Employee ,(ชื่อparameterที่จะส่งเข้าไป)
        super()._showdata()#ใช้class แม่เป็นคนเรียกใช้

class Programmer(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกพัฒนาโปรแกรม"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self ,name,salary,position):
        super().__init__(name,salary,position)
        super()._showdata()

class Sales(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกขาย"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self,name,salary,position):
        super().__init__(name,salary,position)
        super()._showdata()

#สร้าง object จาก class
account = Accountant("สมชาย",50000,"แผนกบัญชี") #ชื่อobject = ชื่อclass(parameterที่จะส่งเข้าไป)**เพิ่มparameterใส่เข้าไป

#ถ้าอยากให้ class ลูกเป็นคนเรียกใช้ ต้องใช้object *******
account._showdata() #เรียกใช้ method ชื่อ _showdata


manager = Manager("สมหมาย",60000,"แผนกผู้จัดการ")
programmer = Programmer("ปวาริษา",70000,"แผนกพัฒนาโปรแกรม")
sales = Sales("สมใจ",60000,"แผนกขาย")
#แสดงชื่อบริษัท
print(account.companyname)
#อยากทราบเงินเดือนต่ําสุดของprogrammer
print("เงินเดือนต่ำสุดของprogrammer = ",programmer.minsalary)





