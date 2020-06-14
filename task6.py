my_list = ('сетевое программирование', 'сокет', 'декоратор')
with open('test_task6.txt', 'w', encoding='utf-8') as txt_file:
    for i in my_list:
        txt_file.write('%s\n' % i)
txt_file.close()
with open('test_task6.txt', encoding='utf-8') as txt_file:
    for i in txt_file:
        print(i, end='')
txt_file.close()
