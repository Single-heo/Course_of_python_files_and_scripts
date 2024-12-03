string = 'teste'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'O metodo:{metodo}', f'existe em:{string}', sep='\n')
    print(getattr(string, metodo)()) # Needs '()' to take the metod and run it.