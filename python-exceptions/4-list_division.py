#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for index in range(list_length):
        div = 0
        try:
            div = my_list_1[index] / my_list_2[index]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            newList.append(div)
    return newList
