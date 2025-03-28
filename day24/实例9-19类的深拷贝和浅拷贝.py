class CPU():
    pass
class Disk():
    pass
class Computer():
    def __init__(self, disk,cpu):
        self.disk = disk
        self.cpu = cpu


cpu = CPU()
disk = Disk()

#创建一台计算计对象
com = Computer(disk,cpu)

com1=com

print(com,'子对象的内存地址',com.cpu,com.disk)
print(com1,'子对象的内存地址',com1.cpu,com1.disk)







#类对象的浅拷贝
print('-'*50)
import copy
com2=copy.copy(com)
print(com,'子对象的内存地址是：',com.cpu,com.disk)
print(com2,'子对象的内存地址是：',com2.cpu,com.disk)