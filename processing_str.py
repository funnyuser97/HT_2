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

