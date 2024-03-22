capacidade_atual, aumento_percentual = map(int, input().split())

nova_capacidade = int((aumento_percentual / 100) * capacidade_atual + capacidade_atual)
print(nova_capacidade)