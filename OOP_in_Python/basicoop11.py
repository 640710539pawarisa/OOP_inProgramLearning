#แปลง object เป็น string

#และเราจะสร้าง method คำนวณรายได้ของพนักงาน

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
    #แสดงรายละเอียดของพนักงาน
    def _showdata(self): 
        print("ชื่อพนักงาน = ",self.__name)
        print("----------------------")
        print("เงินเดือน = ",self.__salary)
        print("----------------------")
        print("ตําแหน่ง = ",self.__position)
        print("----------------------")
        
#******เพิ่มโค้ดส่วนนี้***********
#สร้าง method ที่จะคํานวณรายได้ของพนักงาน
#รายได้ต่อปี = เงินเดือน * 12 + โบนัส
    def _getsalaryIncome(self):
        return self.__salary * 12 #รายได้ต่อปี self.__salary * 12คือ ตัวเอง.__เงินเดือน * 12
    
    
#*********เพิ่มโค้ดส่วนนี้********
#ในส่วนการแปลง object เป็น string ใช้ __str__()
    def __str__(self):
        return "ชื่อพนักงาน = {}\nเงินเดือน = {}\nตําแหน่ง = {}\nรายได้ต่อปี = {}\n".format(self.__name,self.__salary,self.__position,self._getsalaryIncome())
    print("----------------------")
    #ส่งค่าออกไป เป็น string "ส่วนที่ 1 {}\nส่วนที่ 2 {}\nส่วนที่ 3".format(ค่าที่ต้องการส่งออกไป)
    #fomat ใช้ในการแสดงผล
    #มีส่วนนี้ ตรงส่วน showdataไม่จำเป็นแล้ว
    
#-----------------------------------------------------------------------------------
        
#สร้าง class สืบทอดคุณสมบัติ 
#class ลูก

class Accountant(Employee): 
    #สร้าง constructorภายในคลาสลูก เพื่อไม่ให้ตอนสร้าง object ไม่ต้องไปเอาconstructor จาก class แม่***
    
    #เขียนชื่อ แผนก
    __position = "แผนกบัญชี"
    def __init__(self,name,salary,position): 
        super().__init__(name,salary,position) 
        super()._showdata()
    
class Manager(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกผู้จัดการ"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self,name,salary,position):
        super().__init__(name,salary,position) 
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

#*****เพิ่มโค้ดส่วนนี้********
print("รายได้ต่อปี  = {}".format(account._getsalaryIncome()))
#{}.format(ชื่อobject._ชื่อmethod())คือเรียกใช้method ,fomat ใช้ในการแสดงผล
print("รายได้ต่อปี  = {}".format(manager._getsalaryIncome()))
print("รายได้ต่อปี  = {}".format(programmer._getsalaryIncome()))
print("รายได้ต่อปี  = {}".format(sales._getsalaryIncome()))

#วิธีเรียกใช้งาน ที่แปลง object เป็น string ,มาแสดงข้อมูลทั้งหมด
print("แสดงข้อมูล\n{}".format(account))
print("แสดงข้อมูล\n{}".format(manager))
print("แสดงข้อมูล\n{}".format(programmer))
print("แสดงข้อมูล\n{}".format(sales))








