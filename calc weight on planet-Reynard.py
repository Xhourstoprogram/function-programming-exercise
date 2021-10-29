def calc_weight_on_planet(mass, gravity):
    weight = (mass / 9.8) * gravity
    return weight


print(calc_weight_on_planet(120, 23.1))
