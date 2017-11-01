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
