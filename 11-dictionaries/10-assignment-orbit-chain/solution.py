def orbit_chain(orbits, start):
    current = start
    result = [start]
    while current in orbits:
        current = orbits[current]
        result.append(current)
    return result