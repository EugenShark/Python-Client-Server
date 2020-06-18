import json


def write_order_to_json():
    dict_to_json = {"item": input('Введите товар: '),
                    "quantity": input('Введите количество: '),
                    "price": input('Введите цену: '),
                    "buyer": input('Введите покупателя: '),
                    "date": input('Введите дату: ')}
    # with open('orders.json', 'r', encoding='utf-8') as f_n:
    #     f_n_content = f_n.read()
    #хотел выгрузить данные, соединить с новым словарем и записать обратно...
    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(dict_to_json, f_n, indent=4)


write_order_to_json()
