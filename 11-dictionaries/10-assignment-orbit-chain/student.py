def orbit_chain(orbits, start):
    if start == "Sagittarius A*":
        return ["Sagittarius A*"]
    chain = [start]
    while chain[-1] != "Sagittarius A*":
        chain.append(orbits[chain[-1]])
    return chain