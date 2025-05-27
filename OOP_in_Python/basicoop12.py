#overloading คือ ทุกฟังชันมีชื่อเดียวกัน แต่จะมีการรับค่าparameter แต่ละฟังชันไม่เหมือนกัน
#overriding คือ การสืบทอดคุณสมบัติ ,เหมือนการสืบทอดคุณสมบัติจาก class แม่ทุกอย่าง

#****ที่เราอยากทำ คือ แสดงอายุของ accounting มันคือ attribute ของ Employee
#และเราอยากเพิ่ม ประสบการณ์ทำงาน และทักษะการทำงานของ Programmer  (มันอยู่ในส่วน attribute)
#และเราอยากเพิ่ม เขตพื้นที่รับผิดชอบ ของ sales (มันอยู่ในส่วน attribute)

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
        
#สร้าง class สืบทอดคุณสมบัติ 
#class ลูก

#****เพิ่ม age เข้าใน class แผนกบัญชีใน ส่วน constructor
class Accounting(Employee): 
    #สร้าง constructorภายในคลาสลูก เพื่อไม่ให้ตอนสร้าง object ไม่ต้องไปเอาconstructor จาก class แม่***
    
    #เขียนชื่อ แผนก
    __position = "แผนกบัญชี"
    def __init__(self,name,salary,age): 
        super().__init__(name,salary,self.__position) 
        #ต้องสร้าง attribute age ใน class ลูก ด้วยเพราะเราเพิ่งเพิ่มเข้า ****
        self.__age = age
        
    #overide คือmethod ที่มีชื่อเดียวใน class แม่******
    def _showdata(self): 
        super()._showdata() #เรียกใช้ method ชื่อ _showdata จาก class แม่
        print("อายุ = ",str(self.__age))
        print("############################")
#ส่วนของ str
    def __str__(self):
        return (super().__str__()) + "อายุ = {} ปี \n".format(self.__age())
    
    
class Manager(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกผู้จัดการ"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self,name,salary,position):
        super().__init__(name,salary,position) 
        super()._showdata() #เรียกใช้ method ชื่อ _showdata จาก class แม่
        print("############################")
        
    #overide คือmethod ที่มีชื่อเดียวใน class แม่******    

#****เพิ่ม experienceคือประสบการณ์, skill คือความสามารถ เข้าใน class แผนกพัฒนาโปรแกรม ใน ส่วน constructor
class Programmer(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกพัฒนาโปรแกรม"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self ,name,salary,experience,skill):
        super().__init__(name,salary,self.__position)
        #ต้องสร้าง attribute experience ใน class ลูก ด้วยเพราะเราเพิ่งเพิ่มเข้า ****
        self.__experience = experience
        #ต้องสร้าง attribute skill ใน class ลูก ด้วยเพราะเราเพิ่งเพิ่มเข้า ****
        self.__skill = skill
        
#overide คือmethod ที่มีชื่อเดียวใน class แม่******
    def _showdata(self): 
        super()._showdata() #เรียกใช้ method ชื่อ _showdata จาก class แม่
        print("ประสบการณ์ = ",str(self.__experience),"ปี")  #แปลงเป็น stringเพราะ experience เป็น int
        print("ทักษะการทํางาน = ",self.__skill)
        print("############################")

#ส่วนของ str
    def __str__(self):
        #เรียกใช้ method ชื่อ __str__ จาก class แม่
        return (super().__str__()) + "ประสบการณ์ = {} ปี \n ทักษะการทํางาน = {}\n".format(self.__experience,self.__skill)   
    
    
#*******เพิ่ม area เข้าใน class แผนกขาย ใน ส่วน constructor
class Sales(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกขาย"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__position)
        #ต้องสร้าง attribute area ใน class ลูก ด้วยเพราะเราเพิ่งเพิ่มเข้า ****
        self.area = area
        
#overide คือmethod ที่มีชื่อเดียวใน class แม่******
    def _showdata(self): 
        super()._showdata() #เรียกใช้ method ชื่อ _showdata จาก class แม่
        print("เขตพื้นที่รับผิดชอบ = ",self.area)
        print("############################")
        
#ส่วนของ str
    def __str__(self):
        return (super().__str__()) + "เขตพื้นที่รับผิดชอบ = {}\n".format(self.area)
    
    

#สร้าง object จาก class 
# 
# #เพิ่มparameterใส่เข้าไปที่เราเพิ่งเพิ่ม***
account = Accounting("สมชาย",50000,25) 
#ชื่อobject = ชื่อclass(parameterที่จะส่งเข้าไป)**เพิ่มparameterใส่เข้าไป

#ถ้าอยากให้ class ลูกเป็นคนเรียกใช้ ต้องใช้object *******
account._showdata() #เรียกใช้ method ชื่อ _showdata

manager = Manager("สมหมาย",60000,"แผนกผู้จัดการ")
manager._showdata() #เรียกใช้ method ชื่อ _showdata

programmer = Programmer("ปวาริษา",70000,2,"พัฒนาโปรแกรม")
programmer._showdata() #เรียกใช้ method ชื่อ _showdata

sales = Sales("สมชาย",80000,"เชียงใหม่")
sales._showdata() #เรียกใช้ method ชื่อ _showdata

# #เรียกใช้แบบ str *****
# print("ข้อมูลพนักงาน")
# print(account.__str__) #เรียกใช้ method ชื่อ __str__ โดยที่ account เป็น object, __str__ เป็น method
# print(manager.__str__) #เรียกใช้ method ชื่อ __str__
# print(programmer.__str__) #เรียกใช้ method ชื่อ __str__
# print(sales.__str__) #เรียกใช้ method ชื่อ __str__
# print("------------------------------")

#*****แสดงรายได้ต่อปี
print("แผนกบัญชี รายได้ต่อปี  = {}".format(account._getsalaryIncome(5000))) #5000คือ bonus ที่ได้ กรณีถ้าพนักงานได้ bonus
#{}.format(ชื่อobject._ชื่อmethod())คือเรียกใช้method ,fomat ใช้ในการแสดงผล
print("แผนกผู้จัดการ รายได้ต่อปี  = {}".format(manager._getsalaryIncome()))#กรณีไม่ได้ bonus
print("แผนกพัฒนาโปรแกรม รายได้ต่อปี  = {}".format(programmer._getsalaryIncome(10000,500))) # 5000คือ โบนัส , 500คือ OT
print("แผนกฝ่ายขาย รายได้ต่อปี  = {}".format(sales._getsalaryIncome()))







