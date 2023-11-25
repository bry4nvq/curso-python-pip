import random as rd

def logica_ppt(usuariomano, maquinamano):
  respuesta = None
  if usuariomano == maquinamano:
    respuesta = 'Empate'
    
  elif usuariomano == 'papel':
    if maquinamano == 'piedra':
      respuesta = 'usuario'
    else:
      respuesta = 'maquina'
      
  elif usuariomano == 'piedra':
    if maquinamano == 'tijera':
      respuesta = 'usuario'
    else:
      respuesta = 'maquina'
      
  else:
    if maquinamano == 'piedra':
      respuesta = 'maquina'
    else:
      respuesta = 'usuario'
      
  return respuesta

def juegoppt()->str:

  diccionario = {"puntos_usuario" : 0, "puntos_maquina" : 0 }

  options = ("piedra","papel","tijera")
  rondas = 2
  round = 1

  while diccionario["puntos_usuario"] < rondas and diccionario["puntos_maquina"] < rondas:

    print("*"*20)
    print("ROUND", round)
    print("*"*20)
    round += 1
    usuariomano = input("Elija entre piedra, papel o tijera: ").lower()
    if usuariomano in options:
      maquinamano = rd.choice(options)
      template = f"Maquina mano fue: {maquinamano} \nUsuario mano fue: {usuariomano}"
      ganador = logica_ppt(usuariomano,maquinamano)

      if ganador == 'usuario':
         diccionario["puntos_usuario"] += 1
         print(template)
         print('Ganó usuario')
         print("el marcador es: ", diccionario)
         print("-"*30,"\n")
      elif ganador == 'maquina':
        diccionario["puntos_maquina"] += 1
        print(template)
        print('Ganó maquina')
        print("el marcador es: ", diccionario)
        print("-"*30,"\n")
      else:
        print(template)
        print('Empate')
        print("el marcador es: ", diccionario)
        print("-"*30,"\n")

    else:
      print("Digite una opción correcta")
 
  if diccionario["puntos_usuario"] == rondas:
    print('El ganador del juego es el usuario')
  else:
    print('El ganador del juego es la máquina')

juego = juegoppt()