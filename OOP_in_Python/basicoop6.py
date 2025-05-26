#Encapsulation

class Employee:
    def __init__(self,name,salary,position):
        #เพิ่มส่วนนี้**********
        #public attribute
        self.name = name
        #protected attribute คือใส่ _ ด้านหน้าชื่อ attribute
        self._salary = salary
        #private attribute คือใส่ __ ด้านหน้าชื่อ attribute
        self.__position = position
        self._showdata() #เรียกใช้ method ชื่อ _showdata หาเจอเพราะ อยู่ใน class เดียวกัน
        
    #public method
    def _showdata(self): 
#ใส่ _ ด้านหน้าชื่อ methodเป็นการบอกว่าเป็น protected ถ้าเอา _ ออกจะเป็นแบบ public หรือใส่ __ ด้านหน้าชื่อ methodเป็นการบอกว่าเป็น private
        print("ชื่อพนักงาน = {}".format(self.name))
        print("----------------------")
        print("เงินเดือน = {}".format(self._salary))
        print("----------------------")
        print("ตําแหน่ง = {}".format(self.__position))
        print("----------------------")
        
    def __del__(self):
        # print("ลบ object แล้ว")
        pass

#การสร้าง วัตถุ หรือ object จากคลาส Employee
#สามารถปรับเปลี่ยนค่าได้ เช่น obj1.name = "เอ๊ะ"
#คนที่ 1
obj1 = Employee("เอ๊ะปวาริษา",50000,"โปรแกรมเมอร์")  #สร้างวัตถุ ชื่อobj1 จากคลาส Employee และส่งค่าเข้าไป
#ปรับเปลี่ยนค่า เพราะว่าเป็น public
obj1.name = "เอ๊ะ"
obj1._salary = 60000 
# obj1.salary = 60000  เขียนแบบนี้ไม่ได้ เพราะเป็น protected
obj1.__position = "Developer" #แบบ private 


#อยากรู้ obj1 ชื่อว่าอะไร
print(obj1.name)

#อยากรู้ obj1 เงินเดือนเท่าไหร่
print(obj1._salary)

#แสดงผล
# obj1.showdata() #เรียกแบบนี้ไม่ได้ เพราะเป็น protected ต้องเขียนแบบนี้ เช่น
obj1._showdata()
