#สร้าง class สืบทอดคุณสมบัติ
#Inheritance คือการสืบทอดคุณสมบัติ

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

#เพิ่มโค้ดส่วนนี้***********
#สร้าง class สืบทอดคุณสมบัติ 
#class ลูก

class Accountant(Employee): #สืบทอดคุณสมบัติมาจาก Employee ชื่อ class ว่า่ Accountant
    #สร้าง constructorภายในคลาสลูก เพื่อไม่ให้ตอนสร้าง object ไม่ต้องไปเอาconstructor จาก class แม่***
    
    #เขียนชื่อ แผนก
    __position = "แผนกบัญชี"
    def __init__(self):
        pass
    
class Manager(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกผู้จัดการ"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self):
        pass

class Programmer(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกโปรแกรมเมอร์"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self):
        pass

class Sales(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกขาย"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self):
        pass

#สร้าง object จาก class
account = Accountant() #ชื่อobject = ชื่อclass(parameterที่จะส่งเข้าไป)
manager = Manager()
programmer = Programmer()
sales = Sales()
#แสดงชื่อบริษัท
print(account.companyname)
#อยากทราบเงินเดือนต่ําสุดของprogrammer
print("เงินเดือนต่ำสุดของprogrammer = ",programmer.minsalary)

#ถ้ากรณี __minsalary เป็น private attribute จะต้อง print แบบนี้
# print("เงินเดือนต่ำสุดของprogrammer = ",programmer._Employee__minsalary)




