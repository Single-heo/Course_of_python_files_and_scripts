from functionss import pretty_list_and_dict_output

lista1 = []

for x in range(3):
    for y in range(3):
        lista1.append((x,y))

lista2 = [
    [x for y in range(3)]
    for x in range(3)
]

pretty_list_and_dict_output(lista2)