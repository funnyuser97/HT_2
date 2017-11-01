#THIS IS FIRST TASK -SEASON
#this function return season, that include input month
#for example season(11)-return 'autumn' 
def season0(x):
    month_tuple=['winter','spring','summer','autumn']

    if x>=1 and x<=12:
        x=x//3
        if x==4:
            x=0
        return month_tuple[x]
    else:
        return 'error input!!!'

def season1(x):
    month_tuple=['winter','spring','summer','autumn']
    x-=1
    if (x>=0 and x<2) or x==11:
        return month_tuple[0]
    elif (x>=2 and x<5):
        return month_tuple[1]
    elif (x>=5 and x<8):
        return month_tuple[2]
    elif (x>=8 and x<11):
        return month_tuple[3]
    else:
        return 'error input!!!'

def season2(x):
    month_dict={0:'winter',1:'spring',2:'summer',3:'autumn',4:'winter'}
    return month_dict.get(x//3,'error input!!!')

month=int(input('Enter number month: '))

print('This is ',season0(month))
print('This is ',season1(month))
print('This is ',season2(month))

#THIS IS SECOND TASK - DEFAULT_PARAMETR

#the function adds a value in increments to the step
#for example sumator(0,4,1)-return 10, because 0+1+2+3+4=10
#default value this is parametr step. 
#if this parametr is not present, then program uotput error message
def sumator(a,b,s=0):
    suma=0
    next_value=a
    if s!=0:
        while next_value<=b:
            suma+=next_value
            next_value+=s
    else:
        print('Error input step!!!')
    return suma;
# input parametrs
start=int(input('Enter first value: '))
finish=int(input('Enter last value: '))
step=input('Enter step: ')
#call function
if step.isdigit():
    print(sumator(start,finish,int(step)))
else:
print(sumator(start,finish))

#THIS IS 3-TH TASK - FUNCTION, THAT INCUDE 3 FUNCTION

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

#THIS IS 4-TH TASK - FUNCTION, THAT COMPARE 2 NUMBERS

def compare(x,y):
    if x>y:
        print('x biger than y on ',x-y)
    elif x<y:
        print('y biger than x on ',y-x)
    else:
        print('x equal  y ')
    return;
#for example: compare(23,12) - output string 'x biger than y on 11'
x=int(input('input x:'))  
y=int(input('input y:')) 
compare(x,y)

#THIS IS 5-TH TASK - FUNCTION, THAT PROCESSING STRING

#this function processinf input string
#if lenght string is from 30 to 50, then  
def processing_str(my_str):
    len_str=len(my_str)
    if len_str>=30 and len_str<=50:
        count_digit=0
        count_symb=0
        count_other=0
        for i in my_str:
            if i.isdigit():
                count_digit+=1 
            elif i.isalpha():
                count_symb+=1
            else:
                count_other+=1
        print('len =',len_str,'amount of numbers =',count_digit,
            '\namount of symbols =',count_symb,'other =',count_other)
    elif len_str<30:
        sum_num=0
        new_str=''
        for i in my_str:
            if i.isdigit():
                sum_num+=int(i)
            elif i.isalpha():
                new_str+=i
        print('sum all numbers:',sum_num,'\nstring without numbers',new_str)
    elif len_str>50:
        count_symb=0
        new_str=''
        for i in my_str:
            if i.isdigit():
                new_str+=i
            elif i.isalpha():
                count_symb+=1
        print('amount of symbols',count_symb,'\nstring without symbols:',new_str)
#in the way will output amount of character in string and will output string without characters
    else:
        print('did choose else')
    return;
#for example: processing_str('wertwtretye43356345') - output string 'x biger than y on 11'
my_string=input('input string:')
processing_str(my_string)


#THIS IS 6-TH TASK - ANY 3 FUNCTION

from math import exp,pi,log,ceil
def menu(x):
    if x==1:     
        task1()
    elif x==2:     
        task2()
    elif x==3:     
        task3()
    else:     
        print('Incorrect choose!!!')
    return;

def task1():
    Pc=float(input('Input Pc(t): '))
    t=float(input('Input t: '))
    T=float(input('Input T: '))
    P1=exp(-t/T)
    P2=exp(-pi*t**2/(4*T**2))
    m1=log(1-Pc)/log(1-P1)-1
    m2=log(1-Pc)/log(1-P2)-1
    print('m1 = ',ceil(m1),' m2 = ',ceil(m2))
    return;

def task2():
    y=float(input('Input lambda: '))
    T1c=float(input('Input T1c: '))
    suma=T1c*y
    m=find_num(suma,0,1)
    print('m = ',m) 
    return;

def find_num(suma,prev,m):
    tmp=0
    for i in range(m):
        tmp=tmp + (1/(i+1))
    if tmp>suma and (suma-prev)>(tmp-suma):
        return ceil(tmp)
    elif tmp>suma and (suma-prev)<(tmp-suma):
        return ceil(prev)
    return find_num(suma,tmp,m+1);


def task3():
    m=int(input('Input m: '))
    t=float(input('Input t: ')) 
    y=[]
    p=[]
    p_tmp=[]
    f=[]
    for i in range(4):
        print('Input lambda(',i,'):')
        y.append(float(input()))
        p_temp=exp(-y[i]*t)
        p.append(p_temp)
        p_tmp.append(1-p[i])
        f.append(p[i]*y[i])
    Pc=1-(p_tmp[0]*p_tmp[1]*p_tmp[2]*p_tmp[3])
    Fc=sum((f[0]*p_tmp[1]*p_tmp[2]*p_tmp[3],
            f[1]*p_tmp[0]*p_tmp[2]*p_tmp[3],
            f[2]*p_tmp[1]*p_tmp[0]*p_tmp[3],
            f[3]*p_tmp[1]*p_tmp[2]*p_tmp[0]))
    yc=Fc/Pc
    sum_m=0
    for i in range(m+1):
        sum_m+=(1/(i+1))
    T1c=1/yc*sum_m
    print ('Pc(t) = {0:8.6f} Fc(t) = {1:8.6f}'.format(Pc,Fc))
    print('lambda(c) {0:8.6f} T1c = {1:8.6f}'.format(yc,T1c))
    return;
x=int(input('Please choose task (1-3):'))
while x!=4: 
    menu(x)
    x=int(input('Please choose task (1-3):'))

#THIS IS 7-TH TASK - CALCULATOR

def calculate(action,num1,num2):
    if action=='+':
        res=num1+num2
    elif action=='-':
        res=num1-num2
    elif action=='*':
        res=num1*num2
    elif action=='/':
        res=num1/num2
    else: res='error, incorrect choose action'
    return res
#forexample calculate('+',2,3) return 5

action=input('Input action: ')
num1=float(input('Input first number: '))
num2=float(input('Input second number: '))

print(calculate(action,num1,num2))	


