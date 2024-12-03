lista = [
    'a', 0.2, 55, True, False, ('oi', 'olá'),
    [0,1,5,8],  {'nome': 'Luiz'}, {0,1}
]
for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print(item.upper())

    if isinstance(item, (int, float)): #
        print(f'{item} is', True)


o = []
b = {}
e = ()

