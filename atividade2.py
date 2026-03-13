# Dever 1
estoque = [
    {"nome": "Notebook", "preco": 3500, "quantidade": 3},
    {"nome": "Mouse", "preco": 80, "quantidade": 10},
    {"nome": "Teclado", "preco": 200, "quantidade": 5},
    {"nome": "Monitor", "preco": 900, "quantidade": 2},
    {"nome": "Headset", "preco": 450, "quantidade": 0}
]

valor_total = 0

for item in estoque:
    valor_item = item["preco"] * item["quantidade"]
    valor_total += valor_item

    if valor_item > 500:
        print("Item com valor acima de R$500:", item["nome"])

print("Valor total em estoque: R$", valor_total)

#produtos em falta
produtos_em_falta = [item["nome"] for item in estoque if item["quantidade"] == 0]

print("Produtos em falta:", produtos_em_falta)


# Dever 2

frase = input("\nDigite uma frase: ")
palavras = frase.lower().split()
contagem = {}

# Conta as palavras
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

# Total
total_palavras = len(palavras)

#  palavras únicas
palavras_unicas = len(contagem)

#mais frequente
palavra_mais_frequente = max(contagem, key=contagem.get)

#  repetidas
repetidas = [palavra for palavra, qtd in contagem.items() if qtd > 1]

# final
print("\nRELATÓRIO")
print("Total de palavras:", total_palavras)
print("Total de palavras únicas:", palavras_unicas)
print("Palavras repetidas:", repetidas)
print("Palavra mais frequente:", palavra_mais_frequente)
