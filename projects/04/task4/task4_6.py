def set_to_zero_vector(vec, n_elements):
    if len(vec) != 0:
        for i in range(len(vec)):
            if vec[i - 1] != 0:
                vec[i - 1] = 0
    zero_index = n_elements - len(vec)
    for k in range(zero_index):
        vec.append(0)

x = []
set_to_zero_vector(x, 3)
assert x == [0, 0, 0]

y = [10, 20]
set_to_zero_vector(y, 5)
assert y == [0, 0, 0, 0, 0]