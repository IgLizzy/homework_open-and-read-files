# Задача №1
with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        quantity_of_ingredients = int(f.readline())
        ingredients = []
        for i in range(quantity_of_ingredients):
            ingr = f.readline().strip()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[dish] = ingredients

# print(cook_book)

# Задача №2
def get_shop_list_by_dishes(dishes, person_count):
    ingredient = {}
    if type(dishes) is not str:
        for m in dishes:
            for k, i in cook_book.items():
                if k == m:
                    for n in i:
                        ingredient[n['ingredient_name']] = {'measure': n['measure'], 'quantity': int(n['quantity']) * person_count}
        return ingredient
    else:
        for k, i in cook_book.items():
                if k == dishes:
                    for n in i:
                        ingredient[n['ingredient_name']] = {'measure': n['measure'], 'quantity': int(n['quantity']) * person_count}
                    return ingredient

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 5))

# Задача №3

