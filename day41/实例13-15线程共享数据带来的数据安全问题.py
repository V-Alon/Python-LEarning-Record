import threading
from threading import *
import time
ticket=50
def sale_ticket():
    global ticket
    for i in range(100):
        if ticket > 0:
            print(f'{threading.current_thread().name}正在出售第{ticket}张票')
            ticket -= 1
        time.sleep(1)

if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=sale_ticket)
        t.start()


