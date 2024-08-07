"""
Embaralha palavra: Construa uma função que receba uma string como parâmetro e 
devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, 
pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
Padronize em sua função que todos 
os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""
import random

def embaralhados(string):
    nova_string = list(string)
    random.shuffle(nova_string)
    final_string = "".join(nova_string)
    final_string_lower = final_string.lower()
    return final_string_lower 

palavra = input("Insira uma palavra:")

palavra_embaralhada = embaralhados(palavra)

print("PALAVRA EMBARALHADA")
print(palavra_embaralhada)
    