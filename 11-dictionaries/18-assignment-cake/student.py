def cake(stock, recipe_ingredients):
    number_item = 10000000000000
    for i in recipe_ingredients:
        if i not in stock:
            return 0
        if (stock[i]//recipe_ingredients[i]) < number_item:
            number_item = stock[i]//recipe_ingredients[i]
    return number_item