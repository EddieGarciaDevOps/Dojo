def draw_stars(input):
    for item in input:
        if type(item) is int:
            print('*' * item)
        else:
            print(item[0] * len(item))

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)
