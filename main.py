#import random
#import emoji
import sys
import trabalho


def terminar():
    sys.exit()

def numero_inválido():
    print("\nValor inválido, Digite novamente \n")

def mostra_menu():
  print('_'*54)
  print("|",'MENU PRINCIPAL'.center(50),"|")
  print("|",' '.center(50),"|")
  print("|",'Digite o número correspondente a opção que deseja:'.center(50),"|")
  print('|','1 - INICIAR'.center(50),'|')
  print("|",'0 - ENCERRAR'.center(50),"|")
  print("|",' '.center(50),"|")
  print('_'*54)

while True:
  mostra_menu()
  numMenu = input("Digite o numero da ação que deseja: ")
  if numMenu == '1':
    print()
    print()
    print("APLICAÇÃO INICIADA".center(55))
    print()
    print()
    trabalho.codigo()
  if numMenu == '0':
    print()
    print()
    print("APLICAÇÃO FINALIZADA".center(55))
    print()
    print()
    terminar()
  else:
    numero_inválido()    