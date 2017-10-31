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
