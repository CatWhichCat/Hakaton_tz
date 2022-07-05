# Задание №1

# def task(array):
#     return array.find('0')

# print(task("111111111110000000000000000"))

# Задание №2


def task(x1, y1, x2, y2, x3, y3, x4, y4):
    min_x = min(x1, x2)
    min_y = min(y1, y2)
    max_x = max(x1, x2)
    max_y = max(y1, y2)

    # if min_x < x3 < max_x and min_y < y3 < max_y:
    #     return True

    # if min_x < x4 < max_x and min_y < y4 < max_y:
    #     return True

    if (min_x < x3 < max_x or min_x < x4 < max_x) and (min_y < y3 < max_y
                                                       or min_y < y4 < max_y):
        return True
    return False


print(task(1, 1, 2, 2, 3, 3, 4, 4))
# print(task(1, 2, 5, 5, 3, 7, 7, 4))
