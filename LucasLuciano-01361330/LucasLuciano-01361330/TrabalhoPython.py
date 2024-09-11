import json

dados ={
    "palavras": ["lucas", "jadson", "igor", "myllena"]
} 


def verificarPalavra(dados, palavra):
    palavras = dados.get("palavras", [])

    if palavra in palavras:
        return f'A palavra "{palavra}" foi encontrada com sucesso.'
    else:
        return f'A palavra "{palavra}" não foi encontrada.'


res = verificarPalavra(dados, 'lucas')
print(res)

res = verificarPalavra(dados, 'hiago')
print(res)
