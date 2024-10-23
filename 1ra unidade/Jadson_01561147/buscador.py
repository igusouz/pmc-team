import json

def achar_palavra(texto, palavra):
    if palavra.lower() in texto.lower():
        return f'A palavra "{palavra}" foi encontrada no texto.'
    else:
        return f'A palavra "{palavra}" não foi encontrada no texto.'

# Exemplo de JSON
json_content = """
{
    "mensagem": "olá jadson, você gosta de programação?",
    "autor": "Lucas",
    "idade": 23
}
"""

dados = json.loads(json_content)

exemplo = dados["mensagem"]
buscador_de_palavra = "jadson"

resultado = achar_palavra(exemplo, buscador_de_palavra)
print(resultado)
