# EJERCICIOS IA 

# ejercicio 1
def encontrar_ruta(grafo, nodo_inicio, nodo_fin, bloqueados):
    bloqueados_set = set(bloqueados)
    if nodo_inicio in bloqueados_set or nodo_fin in bloqueados_set:
        return []

    visitado = {nodo_inicio}
    cola = [[nodo_inicio]]

    while cola:
        ruta_actual = cola.pop(0)
        nodo_actual = ruta_actual[-1]
        if nodo_actual == nodo_fin:
            return ruta_actual

        for vecino in grafo.get(nodo_actual, []):
            if vecino in bloqueados_set or vecino in visitado:
                continue
            visitado.add(vecino)
            nueva_ruta = ruta_actual + [vecino]
            cola.append(nueva_ruta)

    return []

if __name__ == "__main__":
    ejemplo_grafo = {
        "A": ["B", "C"],
        "B": ["A", "D", "F"],
        "C": ["A", "B", "D"],
        "D": ["C"],
        "E": ["B", "A"],
    }

    ruta = encontrar_ruta(ejemplo_grafo, "C", "B", bloqueados=["A"])
    print("Ruta actual:", ruta)



# Ejercicio 2
"""
AFD (Autómata Finito Determinista) simulado.

Autor: Generado por asistente
"""
from typing import Dict, Iterable, Mapping


def simulate_afd(s: str, start_state: str, accept_states: Iterable[str], transitions: Mapping[str, Mapping[str, str]]) -> bool:
    """Simula un AFD sobre la cadena `s`.

    Args:
        s: cadena de entrada a evaluar.
        start_state: estado inicial del autómata.
        accept_states: colección de estados de aceptación.
        transitions: diccionario de transiciones con formato:
            {estado: {caracter: siguiente_estado}}

    Returns:
        True si la cadena es aceptada (estado final en accept_states),
        False en caso contrario o si falta alguna transición.
    """
    current = start_state
    accept_set = set(accept_states)

    for ch in s:
        state_trans = transitions.get(current)
        if not state_trans:
            return False
        # Si no existe transición con `ch`, falla
        next_state = state_trans.get(ch)
        if next_state is None:
            return False
        current = next_state

    return current in accept_set


if __name__ == "__main__":
    # Ejemplo 1: lenguaje sobre {0,1} que acepta cadenas que terminan en '1'
    transitions1 = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q1'},
    }
    start = 'q0'
    accepts = {'q1'}

    tests = ["", "0", "1", "1010", "1011"]
    print('Ejemplo - cadenas que terminan en 1:')
    for t in tests:
        print(f"{t!r}: {simulate_afd(t, start, accepts, transitions1)}")

    # Ejemplo 2: reconoce la cadena exacta 'ab' (alfabeto {a,b})
    transitions2 = {
        's': {'a': 'q1'},
        'q1': {'b': 'q2'},
        'q2': {},
    }
    print('\nEjemplo - reconoce exactamente "ab":')
    for t in ["", "a", "ab", "aba"]:
        print(f"{t!r}: {simulate_afd(t, 's', {'q2'}, transitions2)}")



# Ejercicio 3 
def validar_tablero_sudoku(matriz):
    if len(matriz) != 9 or any(len(fila) != 9 for fila in matriz):
        return False

    filas = {i: set() for i in range(9)}
    columnas = {j: set() for j in range(9)}
    subcuadriculas = {k: set() for k in range(9)}

    for i in range(9):
        for j in range(9):
            valor = matriz[i][j]
            if valor == 0:
                continue
            if not isinstance(valor, int) or valor < 1 or valor > 9:
                return False

            if valor in filas[i]:
                return False
            filas[i].add(valor)

            if valor in columnas[j]:
                return False
            columnas[j].add(valor)

            indice_subcuadricula = (i // 3) * 3 + (j // 3)
            if valor in subcuadriculas[indice_subcuadricula]:
                return False
            subcuadriculas[indice_subcuadricula].add(valor)

    return True

tablero_valido = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

print('\nValidador de Sudoku:')
print('Tablero válido:', validar_tablero_sudoku(tablero_valido))


# Ejercicio 4 :
from typing import List


def justify_text(words: List[str], max_width: int) -> List[str]:
    """Justifica `words` para que cada línea tenga exactamente `max_width` caracteres.

    - Agrupa palabras en líneas temporales usando un bucle.
    - Distribuye espacios sobrantes matemáticamente entre los huecos.
    - La última línea y las líneas con una sola palabra se left-justifican.

    Retorna una lista de strings justificadas.
    """
    res: List[str] = []
    n = len(words)
    i = 0

    while i < n:
        # Determinar el rango de palabras que caben en la línea
        j = i + 1
        line_len = len(words[i])
        while j < n and line_len + 1 + len(words[j]) <= max_width:
            line_len += 1 + len(words[j])
            j += 1

        num_words = j - i

        # Si es la última línea o solo hay una palabra, left-justify
        if j == n or num_words == 1:
            line = ' '.join(words[i:j])
            line += ' ' * (max_width - len(line))
        else:
            total_chars = sum(len(w) for w in words[i:j])
            total_spaces = max_width - total_chars
            gaps = num_words - 1
            space_between, extra = divmod(total_spaces, gaps)

            # Construir la línea insertando spaces; los primeros `extra` huecos reciben +1 espacio
            parts = []
            for k in range(gaps):
                parts.append(words[i + k])
                parts.append(' ' * (space_between + (1 if k < extra else 0)))
            parts.append(words[j - 1])
            line = ''.join(parts)

        res.append(line)
        i = j

    return res


def resolver_dependencias(paquetes):
    """Determina el orden de instalación de paquetes con sus dependencias.

    Recibe un dict de la forma {paquete: [dependencias]}.
    Usa un bucle while y listas auxiliares para procesar paquetes liberados.
    Detecta deadlocks cuando no quedan paquetes disponibles y todavía hay dependencias.
    """
    # Asegurar que también se consideran dependencias que no aparecen como claves
    todos_paquetes = set(paquetes)
    for deps in paquetes.values():
        todos_paquetes.update(deps)

    dependencias = {pkg: [] for pkg in todos_paquetes}
    for pkg, deps in paquetes.items():
        dependencias[pkg] = list(deps)

    orden = []
    disponibles = [pkg for pkg, deps in dependencias.items() if not deps]
    procesados = set()

    while disponibles:
        paquete = disponibles.pop(0)
        orden.append(paquete)
        procesados.add(paquete)

        for otro, deps in dependencias.items():
            if paquete in deps:
                deps.remove(paquete)
                if not deps and otro not in procesados and otro not in disponibles:
                    disponibles.append(otro)

    if len(orden) != len(todos_paquetes):
        return "Error: Deadlock detectado por dependencias circulares."

    return orden


if __name__ == "__main__":
    paquetes_ejemplo = {
        "bootloader": [],
        "kernel": ["bootloader"],
        "driver": ["kernel"],
        "app": ["driver", "kernel"],
    }
    print("Orden de instalación:", resolver_dependencias(paquetes_ejemplo))
    paquetes_ciclo = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],
    }
    print("Ciclo detectado:", resolver_dependencias(paquetes_ciclo))


if __name__ == "__main__":
    # Ejemplo clásico para probar visualmente
    ejemplo_palabras = ["This", "is", "an", "example", "of", "text", "justification."]
    ancho = 16
    salida = justify_text(ejemplo_palabras, ancho)
    print("Ancho:", ancho)
    for l in salida:
        print(repr(l))


# Ejercicio 5 
def procesar_lotes_transacciones(saldos, bloques):
    
    saldos_finales = saldos.copy()

    for bloque in bloques:
        # Copia temporal para aplicar el bloque completo
        saldos_temporales = saldos_finales.copy()
        bloque_valido = True

        for operacion in bloque:
            if len(operacion) != 3:
                bloque_valido = False
                break

            tipo, cuenta, monto = operacion

            if cuenta not in saldos_temporales or not isinstance(monto, (int, float)):
                bloque_valido = False
                break

            if tipo == 'deposito':
                saldos_temporales[cuenta] += monto
            elif tipo == 'retiro':
                if monto < 0 or saldos_temporales[cuenta] < monto:
                    bloque_valido = False
                    break
                saldos_temporales[cuenta] -= monto
            else:
                bloque_valido = False
                break

        if bloque_valido:
            saldos_finales = saldos_temporales

    return saldos_finales


if __name__ == '__main__':
    saldo_inicial = {
        'A001': 500,
        'A002': 300,
        'A003': 0,
    }

    lotes = [
        [
            ('deposito', 'A001', 200),
            ('retiro', 'A002', 100),
        ],
        [
            ('retiro', 'A001', 800),  # falla: no hay fondos suficientes en este bloque
            ('deposito', 'A003', 50),
        ],
        [
            ('deposito', 'A003', 120),
            ('retiro', 'A002', 50),
        ],
    ]

    resultado = procesar_lotes_transacciones(saldo_inicial, lotes)
    print('Saldos finales:', resultado)


# Ejercicio 6
def resolver_dependencias(paquetes):
    """Retorna el orden de instalación de paquetes según sus prerrequisitos.

    paquetes: dict con llave paquete y valor lista de dependencias.
    Retorna lista de instalación ordenada o mensaje de error si existe un ciclo.
    """
    orden = []
    procesados = []
    pendientes = list(paquetes.keys())

    while pendientes:
        liberados = []

        for paquete in pendientes:
            deps = paquetes.get(paquete, [])
            if all(dependencia in procesados for dependencia in deps):
                liberados.append(paquete)

        if not liberados:
            return "Error: Deadlock detectado por dependencias circulares"

        for paquete in liberados:
            orden.append(paquete)
            procesados.append(paquete)
            pendientes.remove(paquete)

    return orden


if __name__ == "__main__":
    ejemplo = {
        "A": ["B", "C"],
        "B": ["C"],
        "C": [],
        "D": ["A"],
    }
    resultado = resolver_dependencias(ejemplo)
    print(resultado)


# Ejercicio 7
def optimizar_carga(peso_max, items):
    """Resuelve el problema de la mochila 0/1 usando memoización.

    Args:
        peso_max: capacidad máxima de peso permitida.
        items: lista de tuplas (id, peso, valor).

    Returns:
        Tupla (valor_max, [ids_seleccionados]).
    """
    memo = {}
    n = len(items)

    def mejor(indice, peso_restante):
        if indice == n or peso_restante <= 0:
            return 0, []

        key = (indice, peso_restante)
        if key in memo:
            return memo[key]

        item_id, peso, valor = items[indice]

        # Caso sin incluir el item actual
        valor_sin, ids_sin = mejor(indice + 1, peso_restante)
        mejor_valor, mejor_ids = valor_sin, ids_sin

        # Caso incluyendo el item actual, si cabe
        if peso <= peso_restante:
            valor_con, ids_con = mejor(indice + 1, peso_restante - peso)
            valor_con += valor
            if valor_con > mejor_valor:
                mejor_valor = valor_con
                mejor_ids = ids_con + [item_id]

        memo[key] = (mejor_valor, mejor_ids)
        return memo[key]

    return mejor(0, peso_max)


if __name__ == '__main__':
    ejemplo_items = [
        ('A', 4, 6),
        ('B', 2, 4),
        ('C', 3, 5),
        ('D', 1, 3),
    ]
    valor_maximo, seleccion = optimizar_carga(7, ejemplo_items)
    print('Valor máximo:', valor_maximo)
    print('IDs seleccionados:', seleccion)


# Ejercicio 8 
def ordenar_libro_por_precio(ordenes, tipo):
    """Ordena la lista de órdenes por precio según el lado del libro.

    - 'COMPRA': mayor precio primero.
    - 'VENTA': menor precio primero.
    """
    return sorted(
        ordenes,
        key=lambda orden: orden['precio'],
        reverse=(tipo == 'COMPRA')
    )


def cruzar_orden(order_book, nueva_orden):
    """Cruza una orden nueva contra el libro de órdenes existente.

    Args:
        order_book: dict con claves 'COMPRA' y 'VENTA', cada una lista de órdenes.
        nueva_orden: dict con campos 'tipo', 'precio', 'cantidad' y opcional 'id'.

    Returns:
        Tuple (transacciones, order_book_actualizado).
    """
    if nueva_orden['tipo'] not in ('COMPRA', 'VENTA'):
        raise ValueError("El tipo de orden debe ser 'COMPRA' o 'VENTA'.")

    libro = {
        'COMPRA': [dict(o) for o in order_book.get('COMPRA', [])],
        'VENTA': [dict(o) for o in order_book.get('VENTA', [])],
    }
    contrario = 'VENTA' if nueva_orden['tipo'] == 'COMPRA' else 'COMPRA'
    transacciones = []
    cantidad_restante = nueva_orden['cantidad']

    libro[contrario] = ordenar_libro_por_precio(libro[contrario], contrario)

    while cantidad_restante > 0 and libro[contrario]:
        mejor_contraparte = libro[contrario][0]
        precio_match = mejor_contraparte['precio']

        if nueva_orden['tipo'] == 'COMPRA' and precio_match > nueva_orden['precio']:
            break
        if nueva_orden['tipo'] == 'VENTA' and precio_match < nueva_orden['precio']:
            break

        cantidad_ejecutada = min(cantidad_restante, mejor_contraparte['cantidad'])
        transacciones.append({
            'tipo': nueva_orden['tipo'],
            'precio': precio_match,
            'cantidad': cantidad_ejecutada,
            'orden_iniciadora': nueva_orden.get('id'),
            'orden_contraparte': mejor_contraparte.get('id'),
        })

        cantidad_restante -= cantidad_ejecutada
        mejor_contraparte['cantidad'] -= cantidad_ejecutada

        if mejor_contraparte['cantidad'] == 0:
            libro[contrario].pop(0)

    if cantidad_restante > 0:
        orden_residual = dict(nueva_orden)
        orden_residual['cantidad'] = cantidad_restante
        libro[nueva_orden['tipo']].append(orden_residual)
        libro[nueva_orden['tipo']] = ordenar_libro_por_precio(libro[nueva_orden['tipo']], nueva_orden['tipo'])

    return transacciones, libro


if __name__ == '__main__':
    libro_inicial = {
        'COMPRA': [
            {'id': 'B1', 'precio': 99, 'cantidad': 10},
            {'id': 'B2', 'precio': 95, 'cantidad': 5},
        ],
        'VENTA': [
            {'id': 'S1', 'precio': 100, 'cantidad': 7},
            {'id': 'S2', 'precio': 90, 'cantidad': 8},
        ],
    }

    nuevo = {'id': 'N1', 'tipo': 'COMPRA', 'precio': 98, 'cantidad': 12}
    transacciones, libro_actualizado = cruzar_orden(libro_inicial, nuevo)

    print('Transacciones ejecutadas:')
    for t in transacciones:
        print(t)
    print('Libro actualizado:')
    print(libro_actualizado)


# Ejercicio 9
def aplanar_json(diccionario):
    """Convierte un diccionario anidado en un diccionario plano.

    Las claves anidadas se concatenan con punto. Los índices de listas
    se incluyen como parte de la ruta de clave.
    """
    resultado = {}
    pila = [("", diccionario)]

    while pila:
        ruta, valor = pila.pop()

        if isinstance(valor, dict):
            if not valor:
                resultado[ruta] = valor
                continue
            for clave, subvalor in valor.items():
                nueva_ruta = f"{ruta}.{clave}" if ruta else clave
                pila.append((nueva_ruta, subvalor))
        elif isinstance(valor, list):
            if not valor:
                resultado[ruta] = valor
                continue
            for indice, elemento in enumerate(valor):
                nueva_ruta = f"{ruta}.{indice}" if ruta else str(indice)
                pila.append((nueva_ruta, elemento))
        else:
            resultado[ruta] = valor

    return resultado


if __name__ == '__main__':
    ejemplo_json = {
        'empresa': {
            'ventas': [
                {'monto': 100, 'producto': 'A'},
                {'monto': 150, 'producto': 'B'},
            ],
            'sucursal': {'ciudad': 'Lima', 'empleados': 12},
        },
        'fecha': '2026-05-31',
        'metadata': [None, {'activo': True}],
    }

    print('Diccionario original:')
    print(ejemplo_json)
    print('\nDiccionario aplanado:')
    print(aplanar_json(ejemplo_json))


# Ejercicio 10
def construir_arbol_huffman(frecuencias):
    """Construye la jerarquía binaria de un árbol de Huffman.

    Recibe un diccionario {caracter: frecuencia}.
    Convierte a lista de tuplas y usa while hasta que quede un solo elemento.
    En cada ciclo ordena, saca los dos nodos de menor frecuencia y crea
    una nueva tupla anidada (suma, (nodo_izq, nodo_der)).
    """
    if not frecuencias:
        raise ValueError("El diccionario de frecuencias no puede estar vacío.")

    nodos = [(frecuencia, caracter) for caracter, frecuencia in frecuencias.items()]

    while len(nodos) > 1:
        nodos.sort(key=lambda elemento: elemento[0])
        nodo_izq = nodos.pop(0)
        nodo_der = nodos.pop(0)
        nuevo_nodo = (nodo_izq[0] + nodo_der[0], (nodo_izq, nodo_der))
        nodos.append(nuevo_nodo)

    return nodos[0]


def imprimir_arbol_huffman(nodo, nivel=0):
    """Imprime el árbol de Huffman en formato legible."""
    frecuencia, contenido = nodo
    indentacion = '  ' * nivel
    if isinstance(contenido, tuple) and len(contenido) == 2:
        print(f"{indentacion}Nodo(suma={frecuencia})")
        imprimir_arbol_huffman(contenido[0], nivel + 1)
        imprimir_arbol_huffman(contenido[1], nivel + 1)
    else:
        print(f"{indentacion}Hoja(char={contenido}, freq={frecuencia})")


if __name__ == '__main__':
    frecuencias_ejemplo = {
        'a': 5,
        'b': 9,
        'c': 12,
        'd': 13,
        'e': 16,
        'f': 45,
    }
    arbol = construir_arbol_huffman(frecuencias_ejemplo)
    print('\nÁrbol de Huffman construido:')
    imprimir_arbol_huffman(arbol)