#เรียกใช้ class employee
from employee import Employee

class Manager(Employee):
    #เขียนชื่อ แผนก
    __position = "แผนกผู้จัดการ"
    #สร้าง constructorภายในคลาสลูก
    def __init__(self,name,salary,position):
        super().__init__(name,salary,position) 
        super()._showdata() #เรียกใช้ method ชื่อ _showdata จาก class แม่
        print("############################")
        
    #overide คือmethod ที่มีชื่อเดียวใน class แม่****** 