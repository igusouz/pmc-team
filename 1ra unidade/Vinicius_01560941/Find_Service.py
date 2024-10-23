import json

entradas = {
        "servicos": ["casamento", "revelacao", "noivado", "culto"]
}

def verificar(entradas, palavra):
    servicos = entradas.get("servicos",[])

    if palavra in servicos:
        return f'Servico "{palavra}" encontrado.'
    else:
        return f'Servico "{palavra}" não foi encontrado.'
    
result = verificar(entradas, 'casamento')
print(result)

result = verificar(entradas, 'velorio')
print(result)
