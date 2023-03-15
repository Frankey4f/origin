f = open('list of dishes.txt', 'w', encoding='utf-8')
f.write('''Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт''')
f.close()

from pprint import pprint

with open('list of dishes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingridients_count = int(file.readline())
        recipe = []
        for i in range(ingridients_count):
            product, count, measure = file.readline().strip().split(' | ')
            recipe.append({
                'Продукт': product,
                'Кол-во': count,
                'Мера': measure
            })
        file.readline()
        cook_book[dish_name] = recipe






def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for key, value in cook_book.items():
        if dishes in key:
            for ingridient in value:
                name = ingridient['Продукт']
                quantity = int(ingridient['Кол-во']) * person_count
                unit = ingridient['Мера']
                if name not in shop_list.keys():
                    shop_list[name] = {
                        'Мера': unit,
                        'Кол-во': quantity
                    }
                else:
                    shop_list[name]['quantity'] += quantity
    pprint(shop_list)


def compare_docs():
    list_of_files = ['1.txt', '2.txt', '3.txt']
    files_string = []
    for file in list_of_files:
        with open(file, 'r', encoding='utf=8') as f:
            temp = []
            for line in f:
                temp.append(line.strip())
            temp.insert(0, str(len(temp)))
            temp.insert(0, file)
            files_string.append(temp)
    files_string.sort(key=len)

    file = 'result.txt'
    with open(file, 'w', encoding='utf-8') as f:
        for string in files_string:
            for i in string:
                f.writelines(i + '\n')
    return list_of_files

