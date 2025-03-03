#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            else:
                if not (isinstance(my_list_1[i], (int, float)) and
                        isinstance(my_list_2[i], (int, float))):
                    print("wrong type")
                elif my_list_2[i] == 0:
                    print("division by 0")
                else:
                    result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(result)
    return new_list
