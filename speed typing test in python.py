from time import*
import random as r

def mistake(partest,usertest):
    error =0
    for i in range(len(partest)):
        try:
            if(partest[i]!=usertest[i]):
                error=error+1
        except:
            error=error+1
    return error
def time_speed(time_start,time_end,userinput):
    time_difference=time_end-time_start
    time_round=round(time_difference,2)
    speed=len(userinput)/time_round
    return round(speed)




while True:
    check=input("ready to test:yes/no")
    if(check=='yes'):
        test=["My name is Shreya Choudhary","i love playing games","India is My country"]
        test1=r.choice(test)
        print("Speed Typing Test in Python")
        print(test1)
        print()
        print()
        time1=time()
        testinput=input("enter:")
        time2=time()
        print("SPEED:",time_speed(time1,time2,testinput),"word/second")
        print("ERROR",mistake(test1,testinput))
    elif check=='no':
        break
    else:
        print("WRONG")

