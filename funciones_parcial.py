import json
import re
import os



def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def leer_archivo_json(ruta:str):
   # path = r"pp_lab1_avellaneda_abril\\dt.json"
# Cargar los datos del archivo JSON
    with open(ruta , "r") as archivo:
        
        dicc = json.load(archivo) 
    return dicc['jugadores']
    
       # return json.load(archivo)['jugadores']


def imprimir_dato(texto:str):
    """
    La funcion "imprimir_dato" comprueba si la entrada en una cadena de textoby la imprime,
    de lo contrario imprime un mensaje advirtiendo que no es una cadena lo que se ingreso.
    """
    if type(texto)== str:
        print(texto)
    else:
        print("No es una cadena de texto")

def validar_opcion(expresion:str, ingreso_usuario: str)-> str:
    """
    Esta funcion valida que la opcion ingresada sea correcta
    """
    validacion_opcion = False
    if re.match(expresion, ingreso_usuario):
        validacion_opcion = int(ingreso_usuario)
    return validacion_opcion


#1
def mostrar_dream_team(lista_jugadores: list[dict])-> list:   # buscar_nombre_posicion
    """
    """
    if not lista_jugadores:              # mensaje = "Error"
        print("La lista esta vacia")
        return False
    
    if lista_jugadores:
        mensaje = "indice - Nombre - Posicion\n"
        for i in range(len(lista_jugadores)):
            jugador = lista_jugadores[i]
            mensaje += "{0} - {1} - {2}".format(i, jugador['nombre'],jugador['posicion']) + "\n"
    imprimir_dato(mensaje)
            # def mostrar_jugadores(lista_jugadores: list):
            # cont = 1
            # for jugador in lista_jugadores:
            #    print("{} - {} - {}".format(cont,jugador["nombre"], jugador["posicion"]))
            #    cont += 1
    
    
    


"""
UTF-8 (Unicode Transformation Format-8) es una codificación de caracteres que puede representar 
prácticamente todos los caracteres utilizados en cualquier idioma.
Cuando se trabaja con archivos de texto en Python, es importante asegurarse de que la codificación 
utilizada coincida con la codificación del archivo. Si no se especifica una codificación, Python respeta
la codificación predeterminada del sistema operativo, que puede variar. 
Es una buena práctica especificar la codificación al abrir o guardar archivos para evitar problemas de caracteres incorrectos o ilegibles.
 """

def imprimir_menu()-> None:
    menu =\
    """
    1. Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
       
    2. Seleccionar un jugador por su índice y mostrar sus estadísticas
       
    3. Después de mostrar las estadísticas, guardar las estadísticas de ese jugador en un archivo CSV. 

    4. Buscar un jugador por su nombre y mostrar sus logros.
      
    5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
       Team, ordenado por nombre de manera ascendente.

    6. Ingresar el nombre de un jugador y mostrar si ese jugador es
       miembro del Salón de la Fama del Baloncesto.
    7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
    8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
    9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
    10. Ingresar un valor y mostrar los jugadores que han promediado
        más puntos por partido que ese valor.
    11. Ingresar un valor y mostrar los jugadores que han promediado
        más rebotes por partido que ese valor.
    12. Ingresar un valor y mostrar los jugadores que han promediado
        más asistencias por partido que ese valor.
    13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.
    14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
    15. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un
        porcentaje de tiros libres superior a ese valor.
    16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al
        jugador con la menor cantidad de puntos por partido.
    17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
    18. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un
        porcentaje de tiros triples superior a ese valor.
    19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
    20. Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por
        posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a
        ese valor.
    """
    imprimir_dato(menu)
def dream_team_menu_principal(): 
    '''
    imprime el menu y toma una opcion del usuario
    devuelve la opcion elegida, en caso de False devuelve -1
    '''
    imprimir_menu()
    opcion = input("Ingresa una opción del menú: ").upper()
    validacion = re.match( r'^[1]?[0-9]{1}$|20|23', opcion)
    if validacion:
         return True
    else:
         return False
       
def validar_numeros(dato:str):
    """
    valida si el dato pasado es numerico, y si lo es lo convierte en int o float
    recibe un str
    retorna un int o float en caso de ser numerico, si no lo es retorna False
    """
    if re.match(r"^\d+(\.\d+)?$", dato):
        try:
            return int(dato)
        except Exception as error:
            return float(dato)
    else:
        return False
    
#2
def obtener_nombre_estadisticas(lista_jugadores:list[dict])-> dict:
    """
    Esta funcion toma una lista de diccionarios que representan a los jugadores y un indice, recupera al
    al jugador en ese indice, imprime su nombre y estadisticas y devuelve el diccionario que representa a ese jugador.

    """
    if lista_jugadores:

        indice = input("Seleccione un jugador por su indice para ver sus caracteristicas: ")
        indice = validar_opcion(r'^[0-9]{1,2}$', indice)

        if indice >= 0 and indice < len(lista_jugadores):
            jugador_con_ese_indice = lista_jugadores[indice]
            
            dic_estadisticas = {}
            dic_estadisticas = jugador_con_ese_indice["estadisticas"]

            print(jugador_con_ese_indice["nombre"])
            
            for clave, valor in dic_estadisticas.items():
                print(clave, valor)
        else:
            print("El indice es incorresto {0}".format(indice))
    
    return jugador_con_ese_indice

#3
def generar_texto(dicc_jugador: dict)-> str:
    """
    Esta funcion toma un diccionario de las estadisticas de un jugador y devuelve una cadena formateada
    que contiene su nombre, posicion y estadisticas
    """
    jugador_indice = dicc_jugador
    jugador_estadisticas = jugador_indice["estadisticas"]
    nombre_posicion = "{0}, {1}".format(jugador_indice["nombre"],  jugador_indice["posicion"])

    lista_claves = ["nombre", "posicion"]
    lista_valores =[]

    for clave, valor in jugador_estadisticas.items():
        lista_claves.append(clave)
        lista_valores.append(str(valor))
    
    claves_str = ",".join(lista_claves)
    valores_str = ",".join(lista_valores)
    
    datos_str = "{0}\n{1}, {2}".format(claves_str, nombre_posicion, valores_str)
    return datos_str


def guardar_archivo_csv(nombre_archivo:str, contenido:str)-> bool:
    """
    Esta funcion guarda el contenido de una cadena de un archivo con el nombre de archivo dado y
    devuelve un valor booleano que indica si la operacion fue exitosa o no
    """
    with open(nombre_archivo, "w+") as archivo:
        resultado = None
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creo el archivo: {0}".format(nombre_archivo))
        return False
    
    print("Erro al crear el archivo: {0}".format(nombre_archivo))
    return False


def buscar_por_nombre(lista_jugadores:list[dict], jugador: dict, nombre: str):
    """
    Esta funcion busca a traves de RegEx la coincidencia entre el paramtro "nombre" y 
    el nombre pasado como parametro
     
    parametros:
    lista_jugadores : list[dict]-> la lista original que se importo del JSON
    busqueda : tipo match.object  | null-> el resultado del re.match utilizado
    """
    if len(lista_jugadores) == 0:
        print("La lista esta vacia")
        return -1
    if nombre == " ":
        print("Ingrese un nombre valido")

    else:
        busqueda = re.search(f'{nombre}', jugador["nombre"], re.I)
        return busqueda
    

#4
def mostrar_logros_por_busqueda(lista_jugadores: list[dict], nombre: str):
    """
    """
    if len(lista_jugadores) == 0:
        print("Lista vacia")
        return False
    if nombre == " ":
        print("Ingrese un nombre valido")

    else:
        lista = lista_jugadores
        flag_jugador = False
        for jugador in lista:
            busqueda =  buscar_por_nombre(lista_jugadores, jugador, nombre) 
            if busqueda:
                flag_jugador = True
                print(jugador["nombre"] + "\n")
                for logro in jugador["logros"]:
                    print("- " + logro + "\n")
        if flag_jugador == False:
            print("No existe jugador con ese nombre")


#5
def calcular_promedio_total(lista_jugadores:list[dict], estadistica:str):
    """
    Esta funcion calcula el promedio total de la estadistica seleccionada
    """
    if len(lista_jugadores) == 0:
        print("Lista vacia.")
        return -1
    lista = lista_jugadores[:]
    if len(lista) <= 1:
        return lista
    contador = 0
    acumulador = 0
    if estadistica in lista[0]["estadisticas"].keys():
        for jugador in lista:
            acumulador += jugador["estadisticas"][estadistica]
            contador += 1
        promedio = acumulador / contador
        return promedio
    else:
        print("Estadistica inexixtente")


def ordenar_lista_segun_key(lista_jugadores: list[dict], key_a_ordenar : str, flag_estadistica = False, orden_ascendente = True)-> list:
    """
    Esta funcion genera una lista ordenada segun param "key_a_odenar" a traves de un metodo de ordenamiento
    """
    if len(lista_jugadores)== 0:
        print("Lista vacia")
        return False
    lista = lista_jugadores[:]
    rango_a = len(lista)
    flag_swap = True
    contador = 0
    while flag_swap:
        flag_swap = False
        for indice_A in range(rango_a -1):
            contador += 1
            if flag_estadistica == False:
                if orden_ascendente == True:
                    if lista[indice_A][key_a_ordenar] > lista[indice_A+1][key_a_ordenar]:
                        lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                        flag_swap = True
                elif orden_ascendente == False:
                    if lista[indice_A][key_a_ordenar] < lista[indice_A+1][key_a_ordenar]:
                        lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                        flag_swap = True
            elif flag_estadistica == True:
                if orden_ascendente == True:
                    if lista[indice_A]["estadisticas"][key_a_ordenar] > lista[indice_A+1]["estadisticas"][key_a_ordenar]:
                        lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                        flag_swap = True
                elif orden_ascendente == False:
                    if lista[indice_A]["estadisticas"][key_a_ordenar] < lista[indice_A+1]["estadisticas"][key_a_ordenar]:
                        lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                        flag_swap = True
    return lista

def mostrar_estadistica_por_jugador_ordenado(lista_jugadores : list[dict], key_orden : str, estadistica: str):
    """
    Esta funcion muestra un listado ordenado segun "key_orden", del nombre de los jugadores
    junto a la estadistica pasada por param. 
    """   
    if len(lista_jugadores) == 0:
        print("Lista vacia")
        return False
    lista_aux = lista_jugadores[:]
    lista = ordenar_lista_segun_key(lista_aux, key_orden)
    lista_jugador_nombre = []
    for jugador in lista:
        lista_jugador_nombre.append([jugador["nombre"], jugador["estadisticas"][estadistica]])
    estadistica_str = estadistica.replace("_"," ").capitalize()
    for jugador in lista_jugador_nombre:
        mensaje = "Jugador: {0}\n{1}: {2}\n".format(jugador[0], estadistica_str, jugador[1])
        print(mensaje)
    return lista_jugador_nombre

#6
def buscar_jugador_sfb(lista_jugadores: list[dict], nombre: str):
    """
    Esta funcion muestra un listado de jugadores, junto a su nombre y si se encuentran o no en un salon de fama. )sfb)

    """
    if len(lista_jugadores) == 0:
        print("Lista vacia")
        return False
    if nombre == " ":
        print("Nombre vacio.")
    else:
        lista = lista_jugadores[:]
        logro_sfb = "Miembro del Salon de la Fama del Baloncesto"
        lista_jugadores_sfb = []
        flag_jugador = False
        for jugador in lista:
            busqueda = buscar_por_nombre(lista, jugador, nombre)
            if busqueda:
                flag_jugador = True
                for logro in jugador["logros"]:
                    if logro == logro_sfb:
                        lista_jugadores_sfb.append([jugador["nombre"], "Si"])
                        break
                    else:
                        lista_jugadores_sfb.append([jugador["nombre"], " No"])

        mensaje = ""
        if flag_jugador == False:
            print("No existe jugador con ese nombre")
        else:
            for jugador in lista_jugadores_sfb:
                mensaje += "Nombre: {0}\nSe encuentra dentro del HOF?: {1}\n\n".format(jugador[0], jugador[1])
            print(mensaje)
    

#7
def encontrar_maximo(lista_jugadores:list[dict], clave_jugador:str, clave_valor:str)-> str:
    """
    Esta funcion encuentra el valor maximo de una clave especifica en la lista de jugadores y devuelve
    el nombre del jugador que tiene ese valor maximo, junto con el valor mismo, en forma de cadena de texto
    """
                           
    nombre_maximo = None
    maximo = 0
    mensaje = "Error, no se pudo sacar maximo"
    if lista_jugadores:
        for jugador in lista_jugadores:
            valor = jugador[clave_jugador][clave_valor]
            if nombre_maximo in None or valor > maximo:
                maximo = valor
                nombre_maximo = jugador["nombre"]
        clave_valor = clave_valor.replace("_"," ")
    if nombre_maximo:
        mensaje = "El jugador {0} tiene la mayor cantidad de {1}: {2}.".format(nombre_maximo, clave_valor, maximo)
    return mensaje

def mostrar_jugadores_promediado_mas_stat(lista_jugadores:list[dict], estadistica: str, valor_stat: float, flag_mostrar_posicion: False ):
    """
    Esta funcion muestra los jugadores que superen el valor de la estadistica deseada.
    """
    if len(lista_jugadores) == 0:
        print("Lista vacia")
        return False
    lista = lista_jugadores[:]
    estadistica_str = estadistica.replace("_"," ")
    lista_jugadores_prom_mayor = []
    for jugador in lista:
        if jugador["estadisticas"][estadistica] > valor_stat:
            lista_jugadores_prom_mayor.append([jugador["nombre"], jugador["estadisticas"][estadistica], jugador["posicion"]])
        if not lista_jugadores_prom_mayor:
            print("Ningun jugador posee un mayor valor que el ingresado en {0}",format(estadistica_str))
        else:
            mensaje = "\nValor Ingresado: {0}\nJugadores que superar ese valor en {1}:\n".format(valor_stat, estadistica_str)
            for jugador in lista_jugadores_prom_mayor:
                if flag_mostrar_posicion == False:
                    mensaje += "{0} - {1}\n".format(jugador[0], jugador[2], jugador[1])
            print(mensaje)
            return lista_jugadores_prom_mayor
    
def generar_promedio_segun_stat_menos_peor_valor(lista_jugadores:list[dict], estadistica: str):
    """
    Esta funcion genera el promedio de la suma de la estadistica elegida, sin tener en cuenta el stat del jugador que peor promedia
    """
    if len(lista_jugadores) == 0:
        print("Lista vacia")
        return False
    lista_aux = lista_jugadores[:]
    contador = 0
    acumulador = 0
    if estadistica in lista_aux[0]["estadisticas"].keys():
        lista_ordenada = ordenar_lista_segun_key(lista_aux, estadistica, True, False)
        lista_ordenada.pop()
        for jugador in lista_ordenada:
            acumulador += jugador["estadisticas"][estadistica]
            contador += 1
        promedio = acumulador / contador
        return promedio
    else:
        print("Estadistica inexistente")

def jugador_mas_logros(lista_jugadores:list[dict])-> dict:
    """
    Calcula el jugador con mas logros en su carrera
    recibe la lista de jugadores
    retorna el jugador con mas logros obtenidos(dict)
    """
    lista_de_jugadores = lista_jugadores[:]

    acumulador_logros = 0
    logros_jugadores = []
    logros_jugadores_sin_indices = []

    for jugador in lista_de_jugadores:
        for logro in jugador["logros"]:
            patron_cuatro_digitos = r"\d{4}"
            if re.search(patron_cuatro_digitos, logro):  # si hay un año en el logro entra
                acumulador_logros += len(re.findall(patron_cuatro_digitos, logro))  # busca esos años, y el len va a indicar cuantos son y se suman al acumulador
            elif "Miembro" in logro:
                acumulador_logros += 1
            else:
                patron = r"\d{3}"
                if re.match(patron, logro): # si el logro empieza con 1 o 2 digitos entra.
                    acumulador_logros += int(re.findall(patron, logro)[0]) # trae el numero de cada logro, lo parsea y lo suma al acumulador
        logros_jugadores.append(lista_de_jugadores.index(jugador)) # agrego el indice del jugador de la lista real
        logros_jugadores.append(acumulador_logros) # agrego la cantidad de logros que tenga  ese jugador
        logros_jugadores_sin_indices.append(acumulador_logros) # lista aparte solo con logros
        
        acumulador_logros = 0
    for indice in range(len(logros_jugadores_sin_indices)): # recorro segun el largo de la lista de solo logros
        if indice == 0 or float(logros_jugadores_sin_indices[maximo_indice]) < float(logros_jugadores_sin_indices[indice]):
            maximo_indice = indice
            numero_maximo = logros_jugadores_sin_indices[maximo_indice]
    indice_jugador_mas_logros = logros_jugadores[logros_jugadores.index(numero_maximo) -1] # dentro del [] obtiene el indice anterior del numero_maximo,
                                                                                           # que seria el indice del jugador en la listaoriginal. al ser jordan da 0
                                                                        # y los logros_jugadores[x] te da la posicion real del json del jugador con mas logros
    return lista_de_jugadores[indice_jugador_mas_logros]

def jugador_mas_temporadas(jugadores:list[dict])-> None:
    """
    Esta funcion encuentra al jugador(es) con la mayor cantidad de temporadas jugadas en base a una
    lista de dicc de jugadores y los imprime uno a la vex junto con su cantidad de temporadas 
    """
    max_temporadas = 0
    jugadores_max_temporadas = []

    for jugador in jugadores:
        temporadas = jugador["estadisticas"]["temporadas"]
        if temporadas > max_temporadas:
            max_temporadas = temporadas
            jugadores_max_temporadas = [(jugador["nombre"], temporadas)]
        elif temporadas == max_temporadas:
            jugadores_max_temporadas.append((jugador["nombre"], temporadas))
    print("Jugadores con la mayor cantidad de temporadas jugadas:")
    for jugador, temporadas in jugadores_max_temporadas:
        print("Jugador: {} | Temporadas: {}".format(jugador, temporadas))



































