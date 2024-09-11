import json

entradas = {
        "palavras": ["arroz", "feijão", "frango", "brocolis", "alface"]
}

def verificar(entradas, palavra):
    palavras = entradas.get("palavras",[])

    if palavra in palavras:
        return f'Palavra "{palavra}" encontrada.'
    else:
        return f'Palavra "{palavra}" não foi encontrada.'
    
result = verificar(entradas, 'arroz')
print(result)

result = verificar(entradas, 'pão')
print(result)