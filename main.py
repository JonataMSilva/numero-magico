'''Construir um jogo de adivinhação onde o usuário deve inserir o número esperado pelo programa. Sempre que o usuário inserir um número, deve-se informar se este número é maior ou menor que o número mágico e então perguntar um novo número. Se o usuário acertar o número mágico, uma mensagem de vitória deve ser apresentada e o programa então é encerrado.'''

import random

numero_magico = random.randint(1,100)
qtd_tentativas = 5

print(f'Voce tem {qtd_tentativas} tentativas')
numero_usuario = int(input("Digite um numero de 1 a 100 para adivinhar o numero magico: "))

while numero_usuario != numero_magico:
  if numero_usuario > numero_magico:
    print("Seu numero é maior que o numero magico")
  elif numero_usuario < numero_magico:
    print("Seu numero é menor que o numero magico")
  else:
    None
  qtd_tentativas -= 1
  print(f'Voce tem {qtd_tentativas} tentativas')
  numero_usuario = int(input("Digite um numero de 1 a 100 para adivinhar o numero magico: "))
  if qtd_tentativas == 1:
    if numero_usuario == numero_magico:
      break
    print ("acabou suas tentativas")
    print(f"O numero magico era {numero_magico}")
    break
if numero_usuario == numero_magico:
  print (f"Parabens, {numero_magico} é o numero magico! ")
