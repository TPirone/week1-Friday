# def sum_list(num1, num2, *args):
#
#
#     my_total = num1 + num2
#     for element in args:
#         my_total += element
#
#     return my_total

# print(sum_list(10, 10, 10))


def sum_list(*args):
    my_total = 0
    if len(args) < 2:
        return "Enter at least 2 numbers"
    else:
        for element in args:
            if type(element) not in (int, float):
                return "This function only accept numbers"
            else:
                my_total += element

    return my_total