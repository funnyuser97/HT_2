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
