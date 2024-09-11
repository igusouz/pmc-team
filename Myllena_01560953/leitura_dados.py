import json

print("Informe uma palavra: ")
a = str(input())
print("Informe uma segunda palavra: ")
b = str(input())
dados = {
    "palavras": ["bola", "cachorro", "lelis", "lua"]
}

def lendo_dados(dados, palavra):
    palavras = dados.get('palavras', [])
    return 'A palavra "{}" foi {}encontrada.'.format(palavra, '' if palavra in palavras else 'não ')

resultado = lendo_dados(dados, b)
print(resultado)

resultado = lendo_dados(dados, a)
print(resultado)
