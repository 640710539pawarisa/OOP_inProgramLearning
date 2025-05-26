#Setter,Getter Method
#คือแบบ instance variable

class Employee:
    def __init__(self,name,salary,position):
    
        #private attribute
        self.__name = name
        self.__salary = salary
        self.__position = position
        
    #protected method
    def _showdata(self): 
#ใส่ _ ด้านหน้าชื่อ methodเป็นการบอกว่าเป็น protected ถ้าเอา _ ออกจะเป็นแบบ public หรือใส่ __ ด้านหน้าชื่อ methodเป็นการบอกว่าเป็น private
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("----------------------")
        print("เงินเดือน = {}".format(self.__salary))
        print("----------------------")
        print("ตําแหน่ง = {}".format(self.__position))
        print("----------------------")
        
        #เพิ่มโค้ดส่วนนี้*********** หรือเอาใช้ที่นี้ก็ได้ แต่ต้องเลือกแบบใดแบบหนึ่ง
        
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตําแหน่ง = {}".format(self.__position))
        print("----------------------")
        
    def __del__(self):
        # print("ลบ object แล้ว")
        pass

#เพิ่มโค้ดส่วนนี้***********

#คือการกําหนดค่า
#setter คือ method ที่ใช้ในการปรับเปลี่ยนค่า

    def setName(self,newname): #self คือวัตถุตัวเอง , newname คือชื่อที่เราจะเปลี่ยน
        self.__name = newname #self.__name คือชื่อที่เราจะเปลี่ยน , newname คือชื่อที่เราจะเปลี่ยน
    
    def setSalary(self,newsalary): #self คือวัตถุตัวเอง , newsalary คือเงินเดือนที่เราจะเปลี่ยน
        self.__salary = newsalary
    
    def setPosition(self,newposition): #self คือวัตถุตัวเอง , newposition คือตําแหน่งที่เราจะเปลี่ยน
        self.__position = newposition
        #หรือ ใช้คำว่า department แปลว่าตําแหน่ง แต่ คำว่า position ก็ แปลว่าตําแหน่ง
    
        
#คือ การดึงค่า    ,คือmethod ที่ให้บริการข้อมูล  ,หรือเอาไว้ return ค่าออกไป
#getter คือ method ที่ใช้ในการอ่านค่า

    def getName(self):#self คือวัตถุตัวเอง , getName คือชื่อ method, getName คือ method ที่ใช้ในการอ่าน ชื่อ
        return self.__name
    
    def getSalary(self):# getSalary คือชื่อ method, getSalary คือ method ที่ใช้ในการอ่าน เงินเดือน
        return self.__salary
    
    def getPosition(self):# getPosition คือชื่อ method, getPosition คือ method ที่ใช้ในการอ่าน ตําแหน่ง
        return self.__position
    
    #************
        
## การสร้าง วัตถุ หรือ object จากคลาส Employee
##สามารถปรับเปลี่ยนค่าได้ เช่น obj1.name = "เอ๊ะ"

##อันนี้แบบเก่าที่ต้องไปที่ attribute เพื่อปรับเปลี่ยนข้อมูลที่ต้องการ***
# obj1 = Employee("เอ๊ะปวาริษา",50000,"โปรแกรมเมอร์")  #สร้างวัตถุ ชื่อobj1 จากคลาส Employee และส่งค่าเข้าไป
# #ปรับเปลี่ยนค่า เพราะว่าเป็น public
# obj1.name = "เอ๊ะ"
# obj1._salary = 60000 
# # obj1.salary = 60000  เขียนแบบนี้ไม่ได้ เพราะเป็น protected
# obj1.__position = "Developer" #แบบ private 


#อันนี้แบบใหม่ ไม่ต้องไปที่ attribute เพื่อปรับเปลี่ยนข้อมูลที่ต้องการ***
#สร้างวัตถุ ชื่อobj1 จากคลาส Employee และส่งค่าเข้าไป
obj1 = Employee("เอ๊ะปวาริษา",50000,"โปรแกรมเมอร์")
#การเรียกใช้ method
print(obj1.getName())
print(obj1.getSalary())
print(obj1.getPosition())

print("------------------")

#หรือ
print("พนักงานดีเด่นประจำปี คือ {}".format(obj1.getName())) #การเรียกใช้ method , และใช้ format ในการแสดงผล
print("แผนก = {}".format(obj1.getPosition()))

#แสดงผล
obj1._showdata()

#note: setter,getter จะถูกเรียกใช้เมื่อ เราสร้างวัตถุ เช่น obj1 = Employee("เอ๊ะปวาริษา",50000,"โปรแกรมเมอร์") 
#แล้วก็ให้ object เข้าถึง method ที่เราสร้าง

#เช่นเราอยากทราบชื่อพนักงาน
print(obj1.getName())