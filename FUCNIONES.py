
from preguntas import preguntas
from TABLERO import tablero,posicion_inicial
import random




#FUNCIONES USUARIO

#NOMRE USUARIO
def pedir_nombre()->str:
    nombre = input("INGRESE NOMBRE: ")
    return nombre
    
#JUGAR SI O NO
def preguntar_si_quiere_jugar()->str:
    jugar = input("QUIERE JUGAR ? (SI-NO): ").lower()
    jugar = validar_pregunta_volver_jugar(jugar)
    return jugar

def preguntar_volver_jugar()->str:
    volver_jugar = input("QUIERE SEGUIR  JUGANDO ? (SI-NO): ").lower()
    volver_jugar = validar_pregunta_volver_jugar(volver_jugar)
    return volver_jugar


#VALIDACION 
def validar_pregunta_volver_jugar(respuesta:str)->str:
    while respuesta != "si" and respuesta != "no":
        respuesta = input("ERROR, USA (SI-NO): ").lower()
    return respuesta


#RESPUESTA USUARIO
def dar_respuesta_usuario()->str:
    respuesta = input("SELECCIONE RESPUESTA (A-B-C): ").lower()
    respuesta = validar_respuesta_usuario(respuesta)
    return respuesta

#VALIDACION
def validar_respuesta_usuario(respuesta:str)->str:
    while respuesta != "a" and respuesta != "b" and respuesta != "c":
        respuesta = input("ERROR, SELECCIONE RESPUESTA (A-B-C): ").lower()
    return respuesta











#PREGUNTAS

#MESCLAR PREGUNTAS
def mesclar_preguntas(lista:list)->list:
    random.shuffle(lista)
    return lista

#shuffle reorganiza los elementos de lista en un orden aleatorio



#OPCIONES 
def mostrar_opciones(pregunta:dict):
    print("A-",pregunta["respuesta_a"])
    print("B-",pregunta["respuesta_b"])
    print("C-",pregunta["respuesta_c"])



#VERIFICAR PREGUNTAS
def verificar_pregunta_correcta(pregunta:dict,respuesta_usuario:str)->bool:
    retorno = False
    if respuesta_usuario == pregunta["respuesta_correcta"]:
        retorno = True
    return retorno


#RESULTADO PREGUNTA CORRECTA/INCORRECTA
def mostrar_resultado(respuesta:bool):
    if respuesta:
        mostrar_respuesta_correcta()
    else:
        mostrar_respuesta_incorrecta()

def mostrar_respuesta_correcta()->str:
    print("RESPUESTA CORRECTA")

def mostrar_respuesta_incorrecta()->str:
    print("RESPUESTA INCORRECTA")



def mostrar_sin_preguntas()->str:
    print("NO HAY MAS PREGUNTAS SE TERMINO EL JUEGO")


def verificar_contador_preguntas(contador:int)->bool:
    retorno = False
    if contador == 16:
        retorno = True
    return retorno










#MOVIMIENTOS

#MOVIMIENTO TABLERO
def retroceder_y_avanzar(respuesta:bool,posicion:int,tablero:list)->int:
    if respuesta:
        posicion += 1
        posicion = subir_escalera(posicion,tablero)
        print("LA POSICION ACTUAL ES: ",posicion)

    else:
        posicion -= 1
        posicion = bajar_serpientes(posicion,tablero)
        print("LA POSICION ACTUAL ES: ",posicion)

    return posicion


#AVANZAR
def subir_escalera(posicion:int,tablero:list)->int:
    if 0 <= posicion < len(tablero):
        if tablero[posicion] == 1:
            print("ESCALERA, AVANZAS 2 POSICIONES")
            posicion += 1
        elif tablero[posicion] == 2:
            print("ESCALERA, AVANZAS 3 POSICIONES")
            posicion += 2
    return posicion



#RETROSEDER
def bajar_serpientes(posicion:int,tablero:list)->int:
    if 0 <= posicion < len(tablero):
        if tablero[posicion] == 1:
            print("SERPIENTE, RETROCEDES 2 POSICIONES")
            posicion -= 1
        elif tablero[posicion] == 2:
            print("SERPIENTE, RETROCEDES 3 POSICIONES")
            posicion -= 2
        elif tablero[posicion] == 3:
            print("SERPIENTE, RETROCEDES 4 POSICIONES")
            posicion -= 3
    return posicion





#FUNCIONES TERMINAR JUEGO 
def ganar_o_perder(posicion:int)->str:
    resultado = "si"
    if posicion == 30:
        mostrar_ganador()        
        resultado = "no"
    elif posicion == 0:
        mostrar_perdedor()
        resultado = "no"
    return resultado

def mostrar_ganador():
    print("GANASTE")


def mostrar_perdedor():
    print("PERDISTE")



#USUARIO NO QUIERE JUGAR MAS
def no_jugar_mas():
    print("GRACIAS POR JUGAR")


#FUNCIONES CSV
def guardar_score(nombre:str,posicion:int):
    
    with open("score.csv","a") as archivo:
        archivo.write(f"{nombre}, posicion alcanzada fue: {posicion}\n")




def finalizar_juego(nombre:str,posicion:str):
    no_jugar_mas()
    guardar_score(nombre,posicion)
    jugar = "no"
    return jugar







# JUEGO PRINCIPAL
def juego(lista:list):
    nombre = pedir_nombre()
    jugar = preguntar_si_quiere_jugar()
    posicion = posicion_inicial
    guardar_score(nombre,posicion)

    
    while jugar == "si":
        preguntas_aleatorias = mesclar_preguntas(lista)
        contador_preguntas = 0


        for pregunta in preguntas_aleatorias:

            print(pregunta["pregunta"])
            mostrar_opciones(pregunta)
            respuesta_usuario = dar_respuesta_usuario()
            respuesta_correcta = verificar_pregunta_correcta(pregunta,respuesta_usuario)
            mostrar_resultado(respuesta_correcta)
            posicion = retroceder_y_avanzar(respuesta_correcta,posicion,tablero)

            contador_preguntas += 1
            contador_actual = verificar_contador_preguntas(contador_preguntas)
            estado_actual = ganar_o_perder(posicion)



        if estado_actual == "no" or contador_actual:
            jugar = finalizar_juego(nombre,posicion)
            break
        jugar = preguntar_volver_jugar()


