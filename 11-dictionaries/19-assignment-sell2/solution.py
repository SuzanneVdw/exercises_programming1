def sell2(stock, model, size):
    if model not in stock:
        return False
    available_sizes = stock[model]
    if size not in available_sizes:
        return False
    available_sizes[size] -= 1
    if available_sizes[size] == 0:
        del available_sizes[size]
    if len(available_sizes) == 0:
        del stock[model]
    return True