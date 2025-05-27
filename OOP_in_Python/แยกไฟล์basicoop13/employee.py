#แยกไฟล์

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
        print("เงินเดือน = ",self.__salary)
        print("ตําแหน่ง = ",self.__position)
        
#******เพิ่มโค้ดส่วนนี้***********
#สร้าง method ที่จะคํานวณรายได้ของพนักงาน
# #รายได้ต่อปี = เงินเดือน * 12 + โบนัส
#     def _getsalaryIncome(self):
#         return self.__salary * 12 #รายได้ต่อปี self.__salary * 12คือ ตัวเอง.__เงินเดือน * 12
    
    #การ overloading method ****************
#********คํานวณรายได้ต่อปีแบบบวกโบนัสเข้าไปด้วย********
    def _getsalaryIncome(self,bonus=0,overtime=0):  #สร้าง method ที่จะคํานวณรายได้ของพนักงาน ,โดยกำหนด default value เป็น 0
        return (self.__salary * 12) + bonus+overtime #รายได้ต่อปี self.__salary * 12คือ ตัวเอง.__เงินเดือน * 12
    
#note ; ระบุเลข โบนัสเข้าไปมันก็จะเอาไปบวก แล้วเอาไปคํานวณ แต่ถ้าไม่ระบุเลข โบนัสมันจะเอาไปบวกเป็น 0
        