arvore = [5, {'maior': [6, {'maior': 7, 'menor': 3}], 'menor': [4, {'menor': 2, 'maior': 9}]}]

def percorre(arvore, procurado):
    while True:
        if isinstance(arvore, list):
            if arvore[0] == procurado:
                return True
            elif procurado < arvore[0]:
                try:
                    arvore = arvore[1]['maior']
                except:
                    return False
            else:
                try:
                    arvore = arvore[1]['menor']
                except:
                    return False
        else:
            return False

procurado = int(input("Digite o número a ser procurado: "))
encontrado = percorre(arvore, procurado)
print(f"Encontrado: {encontrado}")
