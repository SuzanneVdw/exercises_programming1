def cake(stock, recipe_ingredients):
    amounts = []
    for ingredient, amount in recipe_ingredients.items():
        amounts.append(stock.get(ingredient, 0) // amount)
    return min(amounts)