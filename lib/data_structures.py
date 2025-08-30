def get_names(spicy_foods):
    # return a list of names
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    # return only foods with heat_level > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    # print each food in required format
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # return first food that matches cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    # filter spiciest then print like print_spicy_foods
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')


def get_average_heat_level(spicy_foods):
    # average heat levels (integer division not needed, tests expect 6)
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    # return new list with spicy_food added
    return spicy_foods + [spicy_food]
