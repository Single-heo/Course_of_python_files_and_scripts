# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis. e de condicionais
# print(list(range(10)))

import pprint

def p(L):
    import pprint
    if L is None:
        print("Where is the parameter ?")
    pprint.pprint(L,sort_dicts=False, width=40)


products = [
    {'nome': 'p1', 'preço': 20},
    {'nome': 'p2', 'preço': 10}, # it will not be interacted with for the explanation below: 👇👇👇
    {'nome': 'p3', 'preço': 30}
]

## increasing the price of products in 5% of the total, this creates a new list
new_products = [
   {**product, 'preço': product['preço'] * 1.05} # here created a new list
   if product['preço'] > 20 else {**product} # it will only be increased if greater than 20
   for product in products # read the previous list 👈
   if product['preço'] > 10 # but only if the price is greater than 10 👈
]
# print()
p(new_products)

listt = [n for n in range(10) if n < 5]
p(listt)
