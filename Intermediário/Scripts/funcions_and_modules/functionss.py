import os
import pprint

def pretty_list_and_dict_output(list_or_dict = None):
    if list_or_dict is None:
        print('\033[1m[Error] Without args !\033[0m ')
        exit(1)
    return pprint.pprint(list_or_dict, sort_dicts=False, width=40)

def clear_screen():
    if os.name() == 'nt': # se for windows
        os.system('cls')
    os.system('clear') # Mac ou linux

def arg_must_be_number(x):
    type_of_arg = type(x)
    if not isinstance(x, (float, int)):
        raise TypeError(
            f'The arg "{x}" must be a number(float or int),'
            f' you send a type "{type_of_arg.__name__}"'
        )
    return True

def not_divide_a_number_by_zero(arg):
    if arg == 0:
        raise ZeroDivisionError(f"[ERROR] Why is the divisor({arg}) zero?!")

def divide(number, divisor):
        arg_must_be_number(number)
        arg_must_be_number(divisor)
        not_divide_a_number_by_zero(divisor)
        return number / divisor
