#เรียกใช้ class employee
from employee import Employee

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
    
    