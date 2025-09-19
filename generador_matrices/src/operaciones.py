"""
Operaciones Matemáticas con Matrices
===================================

Implementación de operaciones matemáticas básicas para matrices.
Incluye suma, resta, multiplicación y operaciones auxiliares.

Autor: Nicolas
"""

from .matriz import Matriz


def sumar_matrices(matriz_a, matriz_b):
    """
    Suma dos matrices del mismo tamaño.
    
    Args:
        matriz_a (Matriz): Primera matriz
        matriz_b (Matriz): Segunda matriz
        
    Returns:
        Matriz: Resultado de la suma
        
    Raises:
        ValueError: Si las dimensiones no son compatibles
    """
    if not matriz_a.son_dimensiones_compatibles(matriz_b):
        raise ValueError(f"Las matrices deben tener las mismas dimensiones. "
                        f"Matriz A: {matriz_a.filas}x{matriz_a.columnas}, "
                        f"Matriz B: {matriz_b.filas}x{matriz_b.columnas}")
    
    resultado = Matriz(matriz_a.filas, matriz_a.columnas)
    
    for i in range(matriz_a.filas):
        for j in range(matriz_a.columnas):
            resultado.datos[i][j] = matriz_a.datos[i][j] + matriz_b.datos[i][j]
    
    return resultado


def restar_matrices(matriz_a, matriz_b):
    """
    Resta dos matrices del mismo tamaño (A - B).
    
    Args:
        matriz_a (Matriz): Primera matriz (minuendo)
        matriz_b (Matriz): Segunda matriz (sustraendo)
        
    Returns:
        Matriz: Resultado de la resta
        
    Raises:
        ValueError: Si las dimensiones no son compatibles
    """
    if not matriz_a.son_dimensiones_compatibles(matriz_b):
        raise ValueError(f"Las matrices deben tener las mismas dimensiones. "
                        f"Matriz A: {matriz_a.filas}x{matriz_a.columnas}, "
                        f"Matriz B: {matriz_b.filas}x{matriz_b.columnas}")
    
    resultado = Matriz(matriz_a.filas, matriz_a.columnas)
    
    for i in range(matriz_a.filas):
        for j in range(matriz_a.columnas):
            resultado.datos[i][j] = matriz_a.datos[i][j] - matriz_b.datos[i][j]
    
    return resultado


def multiplicar_matrices(matriz_a, matriz_b):
    """
    Multiplica dos matrices (A × B).
    El número de columnas de A debe ser igual al número de filas de B.
    
    Args:
        matriz_a (Matriz): Primera matriz
        matriz_b (Matriz): Segunda matriz
        
    Returns:
        Matriz: Resultado de la multiplicación
        
    Raises:
        ValueError: Si las dimensiones no son compatibles para multiplicación
    """
    if matriz_a.columnas != matriz_b.filas:
        raise ValueError(f"Para multiplicar matrices, el número de columnas de la primera "
                        f"debe ser igual al número de filas de la segunda. "
                        f"Matriz A: {matriz_a.filas}x{matriz_a.columnas}, "
                        f"Matriz B: {matriz_b.filas}x{matriz_b.columnas}")
    
    resultado = Matriz(matriz_a.filas, matriz_b.columnas)
    
    for i in range(matriz_a.filas):
        for j in range(matriz_b.columnas):
            suma = 0
            for k in range(matriz_a.columnas):
                suma += matriz_a.datos[i][k] * matriz_b.datos[k][j]
            resultado.datos[i][j] = suma
    
    return resultado


def multiplicar_por_escalar(matriz, escalar):
    """
    Multiplica una matriz por un escalar.
    
    Args:
        matriz (Matriz): Matriz a multiplicar
        escalar (int, float, Fraction): Valor escalar
        
    Returns:
        Matriz: Resultado de la multiplicación por escalar
    """
    resultado = matriz.copiar()
    
    for i in range(resultado.filas):
        for j in range(resultado.columnas):
            resultado.datos[i][j] = resultado.datos[i][j] * escalar
    
    return resultado


def potencia_matriz(matriz, exponente):
    """
    Calcula la potencia de una matriz cuadrada.
    
    Args:
        matriz (Matriz): Matriz cuadrada base
        exponente (int): Exponente (debe ser positivo)
        
    Returns:
        Matriz: Resultado de la potenciación
        
    Raises:
        ValueError: Si la matriz no es cuadrada o el exponente no es válido
    """
    if not matriz.es_cuadrada():
        raise ValueError("La matriz debe ser cuadrada para calcular potencias")
    
    if not isinstance(exponente, int) or exponente < 0:
        raise ValueError("El exponente debe ser un entero no negativo")
    
    if exponente == 0:
        return crear_matriz_identidad(matriz.filas)
    
    if exponente == 1:
        return matriz.copiar()
    
    resultado = matriz.copiar()
    for _ in range(exponente - 1):
        resultado = multiplicar_matrices(resultado, matriz)
    
    return resultado


def crear_matriz_identidad(tamaño):
    """
    Crea una matriz identidad del tamaño especificado.
    
    Args:
        tamaño (int): Tamaño de la matriz identidad (n×n)
        
    Returns:
        Matriz: Matriz identidad
    """
    matriz_identidad = Matriz(tamaño, tamaño)
    
    for i in range(tamaño):
        for j in range(tamaño):
            if i == j:
                matriz_identidad.datos[i][j] = 1
            else:
                matriz_identidad.datos[i][j] = 0
    
    return matriz_identidad


def crear_matriz_ceros(filas, columnas):
    """
    Crea una matriz de ceros.
    
    Args:
        filas (int): Número de filas
        columnas (int): Número de columnas
        
    Returns:
        Matriz: Matriz de ceros
    """
    return Matriz(filas, columnas)  # Por defecto se inicializa con ceros


def crear_matriz_unos(filas, columnas):
    """
    Crea una matriz de unos.
    
    Args:
        filas (int): Número de filas
        columnas (int): Número de columnas
        
    Returns:
        Matriz: Matriz de unos
    """
    matriz_unos = Matriz(filas, columnas)
    
    for i in range(filas):
        for j in range(columnas):
            matriz_unos.datos[i][j] = 1
    
    return matriz_unos


def son_matrices_iguales(matriz_a, matriz_b, tolerancia=1e-10):
    """
    Verifica si dos matrices son iguales (con tolerancia para números flotantes).
    
    Args:
        matriz_a (Matriz): Primera matriz
        matriz_b (Matriz): Segunda matriz
        tolerancia (float): Tolerancia para comparación de números flotantes
        
    Returns:
        bool: True si las matrices son iguales, False en caso contrario
    """
    if not matriz_a.son_dimensiones_compatibles(matriz_b):
        return False
    
    for i in range(matriz_a.filas):
        for j in range(matriz_a.columnas):
            diferencia = abs(float(matriz_a.datos[i][j]) - float(matriz_b.datos[i][j]))
            if diferencia > tolerancia:
                return False
    
    return True
