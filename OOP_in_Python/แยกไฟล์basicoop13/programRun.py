#เรียกใช้ class employee
from employee import Employee
#เรียกใช้ class accounting
from accounting import Accounting
#เรียกใช้ class manager    
from manager import Manager
#เรียกใช้ class programmer
from programmer import Programmer
#เรียกใช้ class sales
from sales import Sales

#_________________________________________________________________________-
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







