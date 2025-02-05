import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funcoes.treino import executar_tudo, soma, sub, juntar_nome

pessoas = [
    {
        "nome": "Thiago",
        "sobrenome": "Souza",
        "idade": 26, #soma idade + 5
        "peso": 84 #tira 10kg
        #adiciona campo nome completo
    },
    {
        "nome": "Eduardo",
        "sobrenome": "dias",
        "idade": 27,
        "peso": 75
    },
    {
        "nome": "Vitinho",
        "sobrenome": "careca",
        "idade": 28,
        "peso": 80
    },
    {
        "nome": "Marcos",
        "sobrenome": "onix",
        "idade": 40,
        "peso": 100
    }
]

for pessoa in pessoas:
    if pessoa["nome"] == "Eduardo":
        pessoas.remove(pessoa)
        
    adicao = 5
    nova_idade = soma(pessoa["idade"], adicao)
    pessoa["idade"] = nova_idade
    subtrai = 10
    novo_peso = sub(pessoa["peso"], subtrai)
    pessoa["peso"] = novo_peso
    nome_completo = juntar_nome(pessoa["nome"], pessoa["sobrenome"])
    pessoa["nome_completo"] = nome_completo

print(pessoas)