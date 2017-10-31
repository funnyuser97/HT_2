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
        return tmp
    elif tmp>suma and (suma-prev)<(tmp-suma):
        return prev
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
menu(x)
