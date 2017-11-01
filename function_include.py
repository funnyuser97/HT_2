
from math import ceil
#this function is main function in program
def menu(a,b,c):
    val=a*task1(a*2) + b*task2(b*2) + c*task3(c*2)  
    return val
#this function calculates something value, using input value
#and return resalt to main function
def task1(val):
    m1=23
    m2=34
    res=m1*m2
    print('res: ',res)
    return val*res

#this function calculates something value, using input value
#and return resalt to main function
def task2(val):
    y=float(input('Input lambda: '))
    T1c=float(input('Input T1c: '))
    mult=T1c*y
    print('mult = ',mult) 
    return val*int(mult)
#this function calculates something value, using input value
#and return resalt to main function
def task3(val):
    y=[]
    for i in range(4):
        print('Input lambda(',i,'):')
        y.append(float(input()))

    print ('sum :{0}'.format(sum(y)))
    return val*ceil(sum(y)*100)

print('reasult=res+mult+sum =',menu(1,2,3))
