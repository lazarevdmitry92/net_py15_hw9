# зимний салат - картофель 100г, кобаса 100гр, майонез 50мл, яйца 1шт, огурцы 50гр.
# пюре с говядиной - картофель 200гр, говядина 200гр, масло 50гр.
# торт - печенье 300гр, сметана 300мл, сгущенка 50мл

cook_book = {
    "зимний салат": [
        {"ingridient_name": "картофель", "quality": 100, "measure": "гр"},
        {"ingridient_name": "колбаса", "quality": 100, "measure": "гр"},
        {"ingridient_name": "майонез", "quality": 50, "measure": "мл"},
        {"ingridient_name": "яйца", "quality": 1, "measure": "шт"},
        {"ingridient_name": "огурцы", "quality": 50, "measure": "гр"}
    ],
    "пюре": [
        {"ingridient_name": "картофель", "quality": 200, "measure": "гр"},
        {"ingridient_name": "говядина", "quality": 100, "measure": "гр"},
        {"ingridient_name": "масло", "quality": 50, "measure": "гр"}
    ],
    "торт": [
        {"ingridient_name": "печенье", "quality": 300, "measure": "гр"},
        {"ingridient_name": "сметана", "quality": 300, "measure": "мл"},
        {"ingridient_name": "сгущенка", "quality": 50, "measure": "мл"}
    ]
}


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item["quality"] *= person_count
            if new_shop_list_item["ingridient_name"] not in shop_list:
                shop_list[new_shop_list_item["ingridient_name"]] = new_shop_list_item
            else:
                shop_list[new_shop_list_item["ingridient_name"]]["quality"] += new_shop_list_item["quality"]
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(
            "{} {} {}".format(shop_list_item["ingridient_name"], shop_list_item["quality"], shop_list_item["measure"]))


def create_shop_list():
    person_count = int(input("Введите количество человек"))
    dishes = input("введите блюда на одного человека через запятую").lower().split(", ")
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


# for shop_list_item in shop_list.values():
#   print("{ingridient_name} {quality} {measure}".format(**shop_list_item))    
create_shop_list()  
