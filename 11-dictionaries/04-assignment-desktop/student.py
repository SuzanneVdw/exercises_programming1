def desktop(catalog, components):
    total_price = 0
    for i in components:
        total_price += catalog[i]
    return total_price