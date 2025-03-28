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
com2=copy.copy(com)#com2是新产生的对象，com2的子对象，cpu，disk不变
print(com,'子对象的内存地址是：',com.cpu,com.disk)
print(com2,'子对象的内存地址是：',com2.cpu,com.disk)

#类对象的深拷贝
print('-'*50)
import copy
com3=copy.deepcopy(com)#com3是新产生的对象，com3的子对象，cpu，disk也会重新产生
print(com,'子对象的内存地址是：',com.cpu,com.disk)
print(com2,'子对象的内存地址是：',com2.cpu,com.disk)