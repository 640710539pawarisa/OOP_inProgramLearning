#เรียกใช้ class employee
from employee import Employee

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
    
    