import pprint 
def pretty_list_and_dict_output(list_or_dict=None):
    if list_or_dict is None:
        print('No input provided')
        exit
    return pprint.pprint(list_or_dict, sort_dicts=False, width=40)