ourlist = []
while True:
    print('1 - вывод списка, 2 - добавить елемент,') 
    print('3 - удалить елемент, 4 - подсчет елементов')
    print('5 - выход')
    what_do = input()
    if what_do == '1':
        print(ourlist)
    elif what_do == '2':
        type_element = input('1 - int, 2, - str : ')
        if type_element == "1":
            element = int(input("Какой елемент вставлять : "))
            ourlist.append(element)
        else:
            element = input("Какой елемент вставлять : ")
            ourlist.append(element)
    elif what_do == '3':
        kak_deletnut = input('1 - удалить по номеру, 2 - удалить по названию : ')
        if kak_deletnut == '1':
            nomer = int(input('какой номер : '))
            try:
                ourlist.pop(nomer - 1)
            except:
                print('такого елемента нет!!!')
        if kak_deletnut == '2':
            name = input('какое имя : ')
            try:
                ourlist.remove(name)
            except:
                ourlist.remove(int(name))
    elif what_do == '4':
        print('елементов : ',len(ourlist))
    elif what_do == '5':
        break
