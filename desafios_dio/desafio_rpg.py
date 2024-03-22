# Lista para armazenar os itens
itens = []

for novo_item in range(3):
    novo_item = str(input())
    itens.append(novo_item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")