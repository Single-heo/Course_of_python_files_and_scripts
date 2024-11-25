import os
import pprint

def pretty_list_and_dict_output(list_or_dict = None):
    if list_or_dict is None:
        print('\033[1m[Error]\033[0m ')
        exit(1)
    return pprint.pprint(list_or_dict, sort_dicts=False, width=40)

def clear_screen():
    if os.name() == 'nt': # se for windows
        os.system('cls')
    os.system('clear') # Mac ou linux