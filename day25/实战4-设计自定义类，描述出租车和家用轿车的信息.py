class Car(object):
    def __init__(self,type,id,):
        self.type = type
        self.id = id

    def start(self):
        print('启动')
    def stop(self):
        print('停止')


class Taxi(Car):
    def __init__(self,type,id,company):
        super().__init__(type,id)
        self.company = company

    def start(self):
        print('乘客你好！')
        print(f'我是{self.company}的出租车司机，我的车牌是{self.id}请上车')

    def stop(self):
        print('目的地到了，下车注意安全！')

class Family(Car):
    def __init__(self,type,id,name):
        super().__init__(type,id)
        self.name = name

    def start(self):
        print(f'我的车{self.name}，想怎么开就怎么开，开小米su7创死你')

    def stop(self):
        print('到家了，可以休息了')

taxi=Taxi('小米SU7','陕A88888','公交一公司')
taxi.start()
taxi.stop()

print('-'*50)
family_car=Family('上汽名爵','陕A00000','哈基米')
family_car.start()
family_car.stop()
 