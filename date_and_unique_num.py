import datetime;  
import random;  

for i in range (0,10):  
    nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    randomNum=random.randint(0,99)
    if randomNum<=10:  
        randomNum=str(0)+str(randomNum) 
    uniqueNum=str(nowTime)+str(randomNum)
    print(uniqueNum)