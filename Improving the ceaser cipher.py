def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: wrong input")
        if ok:
            ok = value >= min and value <= max # if finally the OK variable becomes true, then next step, it checks if the value is within the range of MIN and MAX variables, so the user cannot choose anything beyond these two maximums and minimums
        if not ok:
            print("Error: the value not within  permited range ( ", str(min), str(max), ")")
    return value; # return is always tied to a function, instead of simply using print()


v = read_int(prompt = "Enter a number from -10 to 10: ", min = -10, max = 10)
print("The number is:", v)