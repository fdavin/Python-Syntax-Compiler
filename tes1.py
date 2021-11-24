x = 230

if x <= 4:
    x += 5
    if True:
        x -=2
    elif False:
        x -=3
elif x >= 1:
    break
else:
    raise TypeError("Wrong input.")