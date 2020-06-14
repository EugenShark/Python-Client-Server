my_list_0 = ['разработка', 'администрирование', 'protocol', 'standard']
my_list_1 = []


def encoding_func(enc):
    for i in my_list_0:
        my_list_1.append(str.encode(i, enc))
        print(str.encode(i, enc))


def decoding_func(dec):
    for i in my_list_1:
        print(bytes.decode(i, dec))


encoding_func('utf-8')
decoding_func('utf-8')
