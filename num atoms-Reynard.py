def num_atoms(m, am):
    na = (m / am) * (6.022 * (10**23))
    return na


print(num_atoms(10, 196.97))
