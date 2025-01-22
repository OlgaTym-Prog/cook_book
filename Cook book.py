import pprint

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
