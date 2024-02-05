
def desktop(catalog, components):
    total = 0
    for component in components:
        total += catalog[component]
    return total