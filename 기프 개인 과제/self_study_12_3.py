import threading
import time

class Count:

    def __init__(self,num_):
        self.num=num_

    def count(self):
        sum=0
        for i in range(1,self.num+1):
            sum+=i

        print("1+2+3+....+{} = {}".format(self.num,sum))


num1=Count(1000)
num2=Count(1000000)
num3=Count(10000000)

th1=threading.Thread(target=num1.count)
th2=threading.Thread(target=num2.count)
th3=threading.Thread(target=num3.count)

th1.start()
th2.start()
th3.start()