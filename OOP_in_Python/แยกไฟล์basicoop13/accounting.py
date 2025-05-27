#เรียกใช้ class employee
from employee import Employee

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
    
    