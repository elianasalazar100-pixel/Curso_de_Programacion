# Ejercicio 1: Inversion de diccionarios.

diccionario = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 4}
def invertir_diccionario(diccionario):
    diccionario_invertido = {}
    for clave, valor in diccionario.items():
        if valor in diccionario_invertido:
            diccionario_invertido[valor] += (clave,)
        else:
            diccionario_invertido[valor] = (clave,)
    return diccionario_invertido
print(invertir_diccionario(diccionario))

# Ejercicio 2: Agrupador de Anagramas.

anagramas = ["frase", "fresa", "amor", "roma"]
def agrupador_anagramas(palabra):
    diccionario_anagramas = {}
    for palabra in anagramas:
        clave = anagramas.sort()
        if clave in diccionario_anagramas:
            diccionario_anagramas[clave].append(palabra)
        else:
            diccionario_anagramas[clave] = [palabra]
    return list(diccionario_anagramas.values())
print(agrupador_anagramas(anagramas))

# Ejercicio 3: Resumen de Gastos Mensuales.

def resumen_de_gastos(gastos):
    resumen_categoria = {}
    total_general = 0.0
    for categoria, monto in gastos:
        resumen_categoria[categoria] = resumen_categoria.get(categoria, 0.0) + monto
        total_general += monto
    return resumen_categoria, total_general
lista_transacciones = [('Comida', 100),("Transporte", 45),("Salidas", 80),("Pase d batalla", 10)]
resumen, total = resumen_de_gastos(lista_transacciones)
print("Resumen:", resumen)
print(f"Total de gastos mensuales: ${total}")

# Ejercicio 4: Transposición de Matriz a Tuplas

matriz = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
a = len(matriz)
filas = len(matriz)
columnas = len(matriz[0])
transposicion = ([1, 2, 3],
    [4, 5, 6],
    [7, 8, 9])
transposicion = [[0 for _ in range(filas)] for _ in range(columnas)]
for i in range(a):
    for j in range(i + 1, a):
        matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
print("Respuesta:", matriz)

# Ejercicio 5: Compresión Básica de Texto (RLE)

def contar_letras(frase):
    resultado = []
    caracteres = frase[0]
    conteo = 0
    for a in range(1, len(frase)):
        if frase[a] == caracteres:
            conteo += 1
        else:
            resultado.append((caracteres, conteo))
            caracteres = frase
            conteo = 1
    resultado.append((caracteres, conteo))
    return resultado
ingreso = input("Introduce el texto: ")
resultado = contar_letras(ingreso)
print(resultado)

# Ejercicio 6 : Buscador en Diccionarios Anidados

diccionario_nombres = { 
    "Alicia",
    "Nancy",
    "Lucia",
    "Robarta",
    "Casandra",
}
diccionario_ciudades = {
    "buenos aires",
    "paris",
    "quito",
    "tokyo",
    "beijing",
}
clave = "Alicia", "tokyo"
for clave in diccionario_nombres:
    print("\n¿La clave Alicia está en el diccionario?", "Alicia" in diccionario_nombres)
    break
else:
    print("contacto no se encuentra en esta lista.")
for clave in diccionario_ciudades:
    print("\n¿La clave quito está en el diccionario?", "quito" in diccionario_ciudades)
    break
else:
    print("localizacion no valida.")

# ejercicio 7: Detección de Colisiones de Horarios

hora_inicio_hora_fin = (["9:00, 11:00"], ["10:00, 12:00"], ["18:00, 20:00"], ["20:00, 23:00"])
choque = []

def detector_de_choques(hora_inicio_hora_fin):
    for a in range(len(hora_inicio_hora_fin)):
        reunion_actual = [a]
        reunion_siguiente = [a + 1]
    if reunion_siguiente < reunion_actual:
        choque.append((reunion_actual,reunion_siguiente))

respuesta = detector_de_choques(hora_inicio_hora_fin)
print(respuesta)


# ejercicio 9 :

candidatos = [("Jose"),("Anastacia"),("Alicia")]
puntos = {}
def ranking(candidatos):
    for puntos in candidatos:
        candidatos[0] =+ 1
        candidatos[1] =+ 3
        candidatos[2] =+ 2
    puntaje = {"Jose": 1, "Anastacia": 3, "Alicia": 2 }
    return sorted(puntaje.items(), key=lambda x: x[1], reverse=True)
print("\n ranking de candidatos:", ranking(candidatos))

# ejercicio 10 :

cache = {
    "instagram.com": 8, 
    "github.com": 1, 
    "linkeind.com": 4,
    "youtube.com": 12
}
visitas = ["facebook.com", "google.com", "youtube.com"]
limite_capacidad = 3

def simulador_cache(cache, visitas, limite_capacidad):
    for url in visitas:
        cache[url] = cache(url, 0) + 1
    while len(cache) > limite_capacidad:
        menos_frecuentes = (cache )
    del cache[menos_frecuentes]
    return cache
respuesta = simulador_cache(cache, visitas, limite_capacidad)
print(respuesta)