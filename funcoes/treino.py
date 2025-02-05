def juntar_nome(nome, sobrenome):
    resultado = nome + ' ' + sobrenome
    return resultado

def juntar_ultimo_nome(nome, ultimo_sobrenome):
    resultado_completo = nome + ' ' + ultimo_sobrenome
    return resultado_completo

def executar_tudo(nome, sobrenome, ultimo_sobrenome):
    resultado1 = juntar_nome(nome, sobrenome)
    resultado_completo = juntar_ultimo_nome(resultado1, ultimo_sobrenome)
    return resultado_completo

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2