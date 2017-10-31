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
        print(len_str,count_digit,count_symb,count_other)
    elif len_str<30:
        sum_num=0
        new_str=''
        for i in my_str:
            if i.isdigit():
                sum_num+=int(i)
            elif i.isalpha():
                new_str+=i
        print(sum_num,new_str)
    elif len_str>50:

        print(len_str)
    else:
        print('did choose else')
    return;
#for example: processing_str('wertwtretye43356345') - output string 'x biger than y on 11'
my_string=input('input string:')
processing_str(my_string)

