import random
import emoji
#import sys
from listas import bolos
from listas import pães
from listas import cereais
from listas import queijos
from listas import ovos
from listas import carnes
from listas import massas
from listas import cafes
from listas import pratos_caseiros
from listas import iogurtes
from listas import frutas
from listas import legumes_verduras_grãos
from listas import sucos 
from listas import frutosMar


def codigo():
  #Peso
  while True:
    try:
      peso = float(input("Digite seu peso : "))
      break
    except ValueError:
      print("ERROR! digite novamente um número")
    
  #Altura
  while True:
    try:
      altura = float(input("Digite sua altura(em metros) : "))
      break
    except ValueError:
      print("ERROR! digite novamente um número")

  #Idade
  while True:
    try:
      idade = int(input("Digite sua idade : "))
      break
    except ValueError:
      print("ERROR! digite novamente um número")

      
  #sexo
  sexo = str(input("Digite seu sexo, M para masculino e F para feminino : "))
  while sexo !=('M') and sexo!=('f') and sexo!=('m') and sexo !=('F') :
    print("ERROR! digite novamente um número")
    sexo = str(input("digite seu sexo, M para masculino e F para feminino : "))

  IMC = peso / altura**2
  if sexo == 'M' or sexo == 'm':
    if 0 < IMC < 20:
      nivel_obesidade = 0
    elif 20 <= IMC <= 24.9:
      nivel_obesidade = 1
    elif 25 <= IMC <= 29.9:
      nivel_obesidade = 2
    elif 30 <= IMC <= 39.9:
      nivel_obesidade = 3
    elif IMC > 40:
      nivel_obesidade = 4
    else:
      print("IMC invalido")
      
  elif sexo == 'F' or sexo == 'f':
    if 0 < IMC < 19:
      nivel_obesidade = 0
    elif 19 <= IMC <= 23.9:
      nivel_obesidade = 1
    elif 24 <= IMC <= 28.9:
      nivel_obesidade = 2
    elif 29 <= IMC <= 38.9:
      nivel_obesidade = 3
    elif IMC > 39:
      nivel_obesidade = 4
    else:
      print("IMC invalido")

  print("IMC",(round(IMC,2)))
  #TMB - taxa de metabolismo basal
  TMB = 0
  if sexo == 'M' or sexo == 'm':
    TMB_M = (66 + (13.8 *peso) + (5 * (altura*100)) - (6.8 * idade))
    TMB = TMB_M
  elif sexo == 'F' or sexo == 'f':
    TMB_F = (655 + (9.6 *peso) + (1.8 * (altura*100)) - (4.7 * idade))
    TMB = TMB_F  

  print("TMB",round(TMB,2))

  gastoCal = 0
  #exercicio fisico e gasto calorico aparti do TMB
  exercicio = str(input("Você pratica exercicio físico ? (S) para SIM e (N) para Não : \n"))
  while exercicio != "S" and exercicio !="s"and exercicio != "N" and exercicio !="n":
      print('Informação inválida. \nDigite novamente')
      exercicio = str(input("você pratica exercicio físico ?"))
  if exercicio == 'S' or exercicio == 's':
    frequencia = str(input("Com que frequência você pratica exercicios ?\n1 - Prática leve \n2 - Prática moderada \n3 - Prática intensa \n:"))
    if (sexo == 'M' or sexo == 'm') and frequencia == '1':
      gastoCal = TMB*1.55
    elif (sexo == 'M' or sexo == 'm') and frequencia == '2':
      gastoCal = TMB*1.78
    elif (sexo == 'M' or sexo == 'm') and frequencia == '3':
      gastoCal = TMB*2.10
    elif (sexo == 'F' or sexo == 'f') and frequencia == '1':
      gastoCal = TMB*1.56
    elif (sexo == 'F' or sexo == 'f') and frequencia == '2':
      gastoCal = TMB*1.64
    elif (sexo == 'F' or sexo == 'f') and frequencia == '3':
      gastoCal = TMB*1.82
  elif exercicio == "N" or exercicio == 'n':
    gastoCal = TMB

  # Regulação do gasto calorico
  if nivel_obesidade == 0:  # abaixo do peso
      regCal = (gastoCal + 350)
      print(emoji.emojize('\nVocê abaixo do peso:scream:\n',use_aliases=True))
  elif nivel_obesidade == 1:  # normal
      regCal = gastoCal
      print(emoji.emojize('\nVocê está com o peso normal:sunglasses:\n',use_aliases=True))
  elif nivel_obesidade == 2:  # obesidade leve
      regCal = (gastoCal - 500)
      print(emoji.emojize('\nVocê está com obesidade grau I:confused:\n',use_aliases=True))
  elif nivel_obesidade == 3:  # obesidade moderada
      regCal = (gastoCal - 550)
      print(emoji.emojize('\nVocê está com obesidade grau II:disappointed: \n',use_aliases=True))
  elif nivel_obesidade == 4:  # obesidade mórbida
      regCal = (gastoCal - 600)
      print(emoji.emojize('\nVocê está com obesidade grau III(mórbida):dizzy_face:\n',use_aliases=True))

  regCal = regCal+100

  cafe_carb = [bolos, pães, cereais]
  cafe_prot = [iogurtes, queijos, ovos]
  cafe_saud = [frutas]

  almoco_carb = [massas, pratos_caseiros]
  almoco_prot = [carnes, frutosMar, queijos]
  almoco_saud = [legumes_verduras_grãos]

  janta_carb = [massas, pratos_caseiros]
  janta_prot = [ovos, carnes]
  janta_saud = [frutas]

  # seleção Cafe
  seleçaoCC = random.choice(cafe_carb)
  seleçaoCP = random.choice(cafe_prot)
  seleçaoCS = random.choice(cafe_saud)

  # Seleção Almoço
  seleçaoAC = random.choice(almoco_carb)
  seleçaoAP = random.choice(almoco_prot)
  seleçaoAS = random.choice(almoco_saud)

  # seleção janta
  seleçaoJC = random.choice(janta_carb)
  seleçaoJP = random.choice(janta_prot)
  seleçaoJS = random.choice(janta_saud)

  cafe = regCal * 0.3
  almoco = regCal * 0.3
  janta = regCal * 0.3

  # cafe
  print(emoji.emojize('Café da Manhã :coffee:',use_aliases=True))
  lista_cafe = [seleçaoCC, seleçaoCP, seleçaoCS]
  soma_cafe = 0
  lista_cafe_vazia = []
  
  print(cafe)

  for i in (lista_cafe):
      calorias = random.choice(list(i.keys()))
      soma_cafe += calorias
      item = calorias
      itens = i.get(item)
      lista_cafe_vazia.append(itens)

  if soma_cafe <= cafe and soma_cafe >= (cafe - 50):
      print(lista_cafe_vazia)
      
      
  else:
      while soma_cafe > cafe or soma_cafe < (cafe - 50):
          soma_cafe = 0
          lista_cafe_vazia.clear()
          for i in (lista_cafe):
              calorias = random.choice(list(i.keys()))
              soma_cafe += calorias
              item = calorias
              itens = i.get(item)
              lista_cafe_vazia.append(itens)
      print(lista_cafe_vazia)
  
  print('=' * 60)

  # almoço
  print(emoji.emojize('Almoço :spaghetti:',use_aliases=True))
  lista_almoco = [seleçaoAC, seleçaoAP, seleçaoAS]
  soma_almoco = 0
  lista_almoco_vazia = []

  print(almoco)

  for i in (lista_almoco):
      calorias = random.choice(list(i.keys()))
      soma_almoco += calorias
      item = calorias
      itens = i.get(item)
      lista_almoco_vazia.append(itens)

  if soma_almoco <= almoco and soma_almoco >= (almoco - 50):
      print(lista_almoco_vazia)
      
      
  else:
      while soma_almoco > almoco or soma_almoco < (almoco - 50):
          soma_almoco = 0
          lista_almoco_vazia.clear()
          for i in (lista_almoco):
              calorias = random.choice(list(i.keys()))
              soma_almoco += calorias
              item = calorias
              itens = i.get(item)
              lista_almoco_vazia.append(itens)
      print(lista_almoco_vazia)
  
  print('=' * 60)

  # janta
  print(emoji.emojize('Jantar :ramen:',use_aliases=True))
  lista_janta = [seleçaoJC, seleçaoJP, seleçaoJS]
  soma_janta = 0
  lista_janta_vazia = []

  print(janta)

  for i in (lista_janta):
      calorias = random.choice(list(i.keys()))
      soma_janta += calorias
      item = calorias
      itens = i.get(item)
      lista_janta_vazia.append(itens)

  if soma_janta <= janta and soma_janta >= (janta - 50):
      print(lista_cafe_vazia)
      
      
  else:
      while soma_janta > janta or soma_janta < (janta - 50):
          soma_janta = 0
          lista_janta_vazia.clear()
          for i in (lista_janta):
              calorias = random.choice(list(i.keys()))
              soma_janta += calorias
              item = calorias
              itens = i.get(item)
              lista_janta_vazia.append(itens)
      print(lista_janta_vazia)    
  
  print('='*60)

  Soma_total_Cal = soma_almoco + soma_cafe + soma_janta

  print()
  print('Para informações ainda mais precisas, um nutricionista deverá ser consultado')
  print()