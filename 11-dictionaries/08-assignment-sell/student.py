def sell(stock, model):
    if stock[model] == 1:
        stock.pop(model)
    else:
        stock[model] -= 1