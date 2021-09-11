str = input()
num_str = ''
num = ''

for i in str:
    if i.isdigit():
        num = num + i
    else:
        if num != '':
            num_str = num_str + num
            num = ''
if num != '':
    num_str = num_str + num
 
print(num_str)