"""
GUESS THE NUMBER

Pedir ao utilizador para inserir o nome

IA: GERAR NÚMERO 0-20

UTILIZADOR:
6 TENTATIVAS PARA ACERTAR

IA: APENAS RESPONDE SUPERIOR OU INFERIOR
IA: NÚMERO DE TENTATIVAS RESTANTES
 ----------------
VITÓRIA
IA: MENSAGEM DE SUCESSO
IA: NÚMERO NECESSÁRIO PARA ACERTAR

-----------------
Jogar outra vez?

-----------------
Pensar em Scoreboard
Guardar a informação do Jogador Vencedor e número de tentativas utilizado
"""
import random

nome = input("Qual é o teu nome?: ")
numerosecreto = random.randint(1, 20)
print("Tens 6 tentativas para acertares o número que a IA gerou!")
tentativas = 6
while tentativas <= 6:
  numero = int(input("Insira um valor: "))
  if numero == numerosecreto:
    print("Número correto")
    print("Acertaste logo na primeira tentativa!")
    exit()
  elif numero > numerosecreto:
    print("Número errado, é superior")
    tentativas -= 1
    print(f"Tens mais {tentativas} tentativas")
  elif numero < numerosecreto:
    print("Número errado, é inferior")
    tentativas += 1
    print(f"Tens mais {tentativas} tentativas")
  else:
    print(f"Tens mais {tentativas} restantes")
print(f"Queres jogar outra vez {nome}?")
