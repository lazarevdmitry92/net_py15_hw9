def get_cook_book():
    cook_book = {}
    with open('menu.txt', encoding='utf-8') as f:
        for line in f:
            dishlist = []
            cook_book[line.strip()] = dishlist
            score = int(f.readline())
            j = 0
            while j < int(score):
                ingredient = f.readline().strip().split(' | ')
                ingredient[1] = int(ingredient[1])
                ingredient_dict = dict(zip(("ingridient_name", "quantity", "measure"), (ingredient)))
                dishlist.append(ingredient_dict)
                j += 1
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item["quantity"] *= person_count
            if new_shop_list_item["ingridient_name"] not in shop_list:
                shop_list[new_shop_list_item["ingridient_name"]] = new_shop_list_item
            else:
                shop_list[new_shop_list_item["ingridient_name"]]["quantity"] += new_shop_list_item["quantity"]
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(
            "{} {} {}".format(shop_list_item["ingridient_name"], shop_list_item["quantity"], shop_list_item["measure"]))


def create_shop_list():
    cook_book = get_cook_book()
    print(cook_book)
    person_count = int(input("Введите количество человек"))
    dishes = input("введите блюда на одного человека через запятую").split(", ")
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


create_shop_list()
