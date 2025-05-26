#Class Variable & instance variable

#คือแบบ instance variable

class Employee:
    #class variable มันเป็น public  
    
    #ถ้าเราอยากทราบว่าเงินเดือนต่ําสุด และเงินเดือนสูงสุด ให้เราใช้ class variable โดย สร้างชื่อ _minsalary และ _maxsalary
    _minsalary = 12000 #min salary คือเงินเดือนต่ําสุด
    _maxsalary = 50000 #max salary #คือเงินเดือนสูงสุด
    _companyname = "บริษัท xyz จำกัด" 
    #อยากทราบชื่อบริษัท แล้วprint ชื่อบริษัท
    
    #วงจรชีวิตของตัวแปร min salary และ max salary จะเริ่มต้นของclass ถึงจุดสิ้นสุดของ class
    
    #class variable จะถูกเข้าถึงได้เลย ไม่จําเป็นต้องสร้างวัตถุ โดยอ้างอิงไปที่ชื่อ class และก็ตามด้วยชื่อตัวแปร
    
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
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("----------------------")
        print("เงินเดือน = {}".format(self.__salary))
        print("----------------------")
        print("ตําแหน่ง = {}".format(self.__position))
        print("----------------------")


#สร้างวัตถุ ชื่อobj1 จากคลาส Employee และส่งค่าเข้าไป
obj1 = Employee("เอ๊ะปวาริษา",50000,"โปรแกรมเมอร์")
#การเรียกใช้ method
#อยากทราบเงินเดือนต่ําสุดของพนักงาน และเงินเดือนสูงสุดของพนักงาน
print("เงินเดือนต่ำสุดของพนักงาน = ",str(Employee._minsalary))
#แสดงผลเงินเดือนต่ําสุด ,ไม่จำเป็นต้องสร้างวัตถุ ก็สามารถเรียกใช้ได้ ,strแปลงเป็น string ด้วย
print(Employee._maxsalary)#แสดงผลเงินเดือนสูงสุด

#อยากทดสอบการเข้าถึงinstance variable ชื่อพนักงาน ได้ไหม
# print(Employee.__name) #ไม่สามารถเข้าถึงได้ เนื่องจากเป็น private attribute ,print แบบนี้จะแสดง error

#อยากทราบชื่อบริษัท
print(Employee._companyname)