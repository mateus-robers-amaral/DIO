# Desafio: A Aventura do Explorador
while True:
  # Entrada
  quantidade_passos = int(input())
  
  if quantidade_passos < 0:
    continue
  
  elif quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")
    break
    
  else:
    for passo in range(quantidade_passos):
        if passo > 0:
            print(f"Explorador: {passo + 1} passos")
        if passo == 0:
          print("Explorador: 1 passo")
    break