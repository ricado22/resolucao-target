# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# Função para contar a ocorrência da letra 'a' (maiúscula ou minúscula) em uma string
def contar_letras_a(string):
    # Contagem de 'a' minúsculo e 'A' maiúsculo
    return string.count('a') + string.count('A')

# Lista de strings pré-definida
lista_strings = [
    "Amazônia", 
    "Piano", 
    "Carro", 
    "Abacaxi", 
    "Lua", 
    "Maracujá", 
    "Andar", 
    "Casa", 
    "Jardim", 
    "Brasil"
]

# Função principal para verificar cada string na lista
def verificar_lista_strings(lista):
    for string in lista:
        # Chama a função para contar as letras 'a' e 'A'
        qtd_a = contar_letras_a(string)
        
        # Exibe se há ocorrências e quantas são
        if qtd_a > 0:
            print(f"A string '{string}' contém {qtd_a} ocorrência(s) da letra 'a' ou 'A'.")
        else:
            print(f"A string '{string}' NÃO contém a letra 'a' ou 'A'.")

# Chama a função principal
if __name__ == "__main__":
    verificar_lista_strings(lista_strings)
