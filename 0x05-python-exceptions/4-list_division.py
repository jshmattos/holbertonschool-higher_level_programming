
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        prod = 0
        try:
            prod = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            div_list.append(prod)
    return div_list
