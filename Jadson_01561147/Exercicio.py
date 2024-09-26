# -*- coding: utf-8 -*-
"""Exercício_Python_1.ipynb



**Exercício 1 - Aquecimento de Python para Ciência de Dados**

1. Imprima "Hello, World!" no console.
"""

print ("Hello, World!")

"""2. Crie uma variável x com valor 10 e imprima seu valor."""

a = 10
print(a)

"""3. Some dois números e exiba o resultado."""

def soma(a, b):
    resultado = a + b
    return resultado

n1= 5
n2 = 10
resultado = soma(n1, n2)
print(resultado)

"""4. Verifique se um número é par ou ímpar.

"""

def paridade(num):
  if num % 2 == 0:
    return "par"
  else:
    return "impar"

num = 7

resultado = paridade(num)
print(f"O número {num} é {resultado}.")

"""5. Crie uma função que receba dois números e retorne a soma deles."""

def soma(num1, num2):
    return num1 + num2
    
resultado = soma(5, 10)
print(resultado)


"""6. Crie uma lista com os números de 1 a 5 e imprima-a.

"""

array = [1, 2, 3, 4, 5]

array.append(6)

print(array)

"""7. Adicione o número 6 à lista criada na questão anterior.

"""

array = [1, 2, 3, 4, 5, 6]

print(array)

"""8. Remova o número 3 da lista."""

array = [1, 2, 3,4, 5]

array.remove(3)

print(array)

"""9. Acesse o terceiro elemento da lista."""

array = [1, 2, 3, 4, 5]

print(array[2])

"""10. Imprima o tamanho da lista."""

array = [1, 2, 3, 4, 7]

print(len(array))

"""11. Crie um dicionário com informações de um carro (marca, modelo, ano)."""

dicionario = {
    "marca": "Volkswagen",
    "modelo": "Gol quadrado",
    "ano": 1995
}

print(dicionario)

"""12. Acesse o valor associado à chave "marca" no dicionário."""

dicionario = {
    "marca": "Volkswagen",
    "modelo": "Gol quadrado",
    "ano": 1999
}

print(dicionario["marca"])

"""13. Adicione uma nova chave "cor" com valor "preto" ao dicionário."""

dicionario = {
    "marca": "Volkswagen",
    "modelo": "Gol quadrado",
    "ano": 2000,
    "cor": "preto"
}

print(dicionario)

"""14. Verifique se a chave "modelo" existe no dicionário.

"""

dicionario = {
    "marca": "Volkswagen",
    "modelo": "Gol quadrado",
    "ano": 1998,
    "cor": "preto"
}

if "modelo" in dicionario:
  print("a chave existe")
else:
  print("a chave nao existe")

"""15. Itere sobre as chaves do dicionário e imprima cada uma delas."""

dicionario = {
    "marca": "Volkswagen",
    "modelo": "Gol quadrado",
    "ano": 1998,
    "cor": "preto"
}

for chave in dicionario:
    print(chave)

"""15. Itere sobre as chaves do dicionário e imprima cada uma delas."""

dicionario = {
    "marca": "Volkswagen",
    "modelo": "Gol quadrado",
    "ano": 1997,
    "cor": "preto"
}

for valor in dicionario.values():
    print(valor)

"""17. Crie uma função que receba uma lista e retorne a soma dos elementos."""

def soma_lista(lista):
    return sum(lista)

numeros = [1, 3, 5, 7, 9]
resultado = soma_lista(numeros)
print(resultado)

"""18. Crie uma função que receba um dicionário e retorne todas as suas chaves.

"""

def chaves_dicionario(dicionario):
    return list(dicionario.keys())

dicionario_exemplo = {
    "marca": "Volkswagen",
    "modelo": "Gol quadrado",
    "ano": 1997,
    "cor": "preto"
}

resultado = chaves_dicionario(dicionario_exemplo)
print("As chaves do dicionário são:", resultado)

"""
19. Crie uma função que receba um dicionário e imprima chave e valor em linhas separadas."""

def imprime_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(f"Chave: {chave}")
        print(f"Valor: {valor}\n")

dicionario_exemplo = {
    "marca": "Volkswagen",
    "modelo": "Gol quadrado",
    "ano": 1998,
    "cor": "preto"
}

imprime_dicionario(dicionario_exemplo)

"""20. Crie uma classe chamada Pessoa com atributos nome e idade, e um método que imprima esses dados."""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprime_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


pessoa1 = Pessoa("Ana", 30)
pessoa1.imprime_dados()
