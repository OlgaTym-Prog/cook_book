import pprint

cook_book = {}

with open('recipes.txt', 'r', encoding='UTF-8') as f:
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        count = int(f.readline().strip())
        ingredients = []
        for i in range(count):
            ingredient = f.readline().strip()
            name, quantity, measure = ingredient.split(' | ')
            ingredients.append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})
        cook_book[dish_name] = ingredients
        f.readline()

pprint.pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if name in shopping_list:
                    shopping_list[name]['quantity'] += quantity
                else:
                    shopping_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюда {dish} нет в книге рецептов")

    return shopping_list


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)

pprint.pprint(shop_list)

f.close()

# Задача № 3

file_names = ['1.txt', '2.txt', '3.txt']
file_contents = {}

with open('1.txt', encoding='utf') as f1, open('2.txt', encoding='utf') as f2, \
        open('3.txt', encoding='utf') as f3:
    files = [f1, f2, f3]
    for file in files:
        lines = file.readlines()
        line_count = len(lines)

        file_contents[line_count] = [f"{file.name}\n", f"{line_count}\n"] + lines

    sorted_file_contents = dict(sorted(file_contents.items()))

    with open('result.txt', 'w', encoding='utf-8') as result_file:
        for line_count, content in sorted_file_contents.items():
            result_file.writelines(content)
            result_file.write('\n')

f1.close()
f2.close()
f3.close()