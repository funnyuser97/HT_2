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

