s1 = ("Olá mundo","Luiz","AEEEEAEASE")
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3) 


letras = set()
while True:
    inputt = input("Please enter anythings: ")
    letras.add(inputt)
    if 'l' in letras: print('Great!') ; break  
    
    print(f"Current unique inputs: {letras}")
    
