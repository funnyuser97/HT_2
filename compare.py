def compare(x,y):
    if x>y:
        print('x bigger than y on ',x-y)
    elif x<y:
        print('y bigger than x on ',y-x)
    else:
        print('x equal  y ')
    return;
#for example: compare(23,12) - output string 'x bigger than y on 11'
x=int(input('input x:'))  
y=int(input('input y:')) 
compare(x,y)
