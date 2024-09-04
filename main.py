def mover_trem(lista_direcoes):

  contador_movimento = 0
  contador_direcao = 0
  posicao_atual = 0
  ultima_direcao = ""

  for direcao_atual in lista_direcoes:

    if ultima_direcao == direcao_atual:
      contador_direcao += 1

    if contador_direcao == 20:
      print("O trem não pode ir na mesma direção por mais de 20 vezes consecutivas...")
      break
      
    if contador_movimento == 50:
      print("O trem chegou ao limite de movimentos, parando...")
      break
    
    if direcao_atual == "DIREITA":
      posicao_atual += 1
    else:
      posicao_atual -= 1

    ultima_direcao = direcao_atual
    contador_movimento += 1
  
  print(
    "--> Posição atual: " + str(posicao_atual) + "\n"  + 
    "--> Última direção: " + ultima_direcao + "\n" + \
    "--> Quantidade de movimentos: " + str(contador_movimento)
  )

  return lista_direcoes

mover_trem(["ESQUERDA","ESQUERDA","DIREITA","DIREITA","ESQUERDA"])