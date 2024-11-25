from functionss import pretty_list_and_dict_output
lista = [1, 2, 3, 4, 5]

new_list = [
    numero
    for numero in lista
    if  numero > 2
]

pretty_list_and_dict_output(new_list)


