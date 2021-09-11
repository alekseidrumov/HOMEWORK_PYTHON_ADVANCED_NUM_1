int_list = [1,2,3,4]
chet_num = []
nechet_num = []
for i in int_list:
    if i % 2 == 0:
        chet_num.append(i)
for i in int_list:
    if i % 2 != 0:
        nechet_num.append(i)
print(chet_num + nechet_num)