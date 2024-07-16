import pprint
import os


def read_recipes(file_path):

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
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
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


def main():

    cook_book = read_recipes('resipes.txt')
    pprint.pprint(cook_book)

    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)

    pprint.pprint(shop_list)


if __name__ == "__main__":
    main()


# Задача № 3


def read_files(file_names):
    file_contents = {}
    for file_name in file_names:
        with open(file_name, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            file_contents[line_count] = [f"{file_name}\n", f"{line_count}\n"] + lines
    return file_contents


def write_sorted_content(file_contents, output_file):
    sorted_file_contents = dict(sorted(file_contents.items()))
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for content in sorted_file_contents.values():
            result_file.writelines(content)
            result_file.write('\n')


def main():
    file_names = [f for f in os.listdir('.') if f.endswith('.txt')]
    file_contents = read_files(file_names)
    write_sorted_content(file_contents, 'result.txt')


if __name__ == "__main__":
    main()
