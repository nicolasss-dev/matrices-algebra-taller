"""
Validadores de Entrada
=====================

Funciones para validar entradas del usuario y datos de matrices.
Garantiza que los datos sean correctos antes de procesarlos.

Autor: Nicolas
"""

from fractions import Fraction


def validar_dimensiones(filas, columnas):
    """
    Valida que las dimensiones de una matriz sean correctas.
    
    Args:
        filas: Número de filas
        columnas: Número de columnas
        
    Raises:
        ValueError: Si las dimensiones no son válidas
    """
    if not isinstance(filas, int) or not isinstance(columnas, int):
        raise ValueError("Las dimensiones deben ser números enteros")
    
    if filas <= 0 or columnas <= 0:
        raise ValueError("Las dimensiones deben ser números positivos")
    
    if filas > 100 or columnas > 100:
        raise ValueError("Las dimensiones no pueden ser mayores a 100")


def validar_numero(valor):
    """
    Valida y convierte un valor a un tipo numérico apropiado.
    
    Args:
        valor: Valor a validar (str, int, float, Fraction)
        
    Returns:
        int, float, o Fraction: Valor convertido al tipo apropiado
        
    Raises:
        ValueError: Si el valor no es un número válido
    """
    if isinstance(valor, (int, float, Fraction)):
        return valor
    
    if isinstance(valor, str):
        valor = valor.strip()
        
        if valor == "":
            raise ValueError("El valor no puede estar vacío")
        
        # Verificar si es una fracción
        if '/' in valor:
            try:
                return Fraction(valor)
            except (ValueError, ZeroDivisionError) as e:
                raise ValueError(f"Fracción inválida: {valor}")
        
        # Verificar si es un entero
        try:
            return int(valor)
        except ValueError:
            pass
        
        # Verificar si es un decimal
        try:
            return float(valor)
        except ValueError:
            raise ValueError(f"Número inválido: {valor}")
    
    raise ValueError(f"Tipo de dato no soportado: {type(valor)}")


def validar_matriz_datos(datos, filas_esperadas, columnas_esperadas):
    """
    Valida que los datos de una matriz tengan la estructura correcta.
    
    Args:
        datos: Lista de listas con los datos de la matriz
        filas_esperadas (int): Número esperado de filas
        columnas_esperadas (int): Número esperado de columnas
        
    Raises:
        ValueError: Si los datos no tienen la estructura correcta
    """
    if not isinstance(datos, list):
        raise ValueError("Los datos deben ser una lista")
    
    if len(datos) != filas_esperadas:
        raise ValueError(f"Se esperaban {filas_esperadas} filas, pero se recibieron {len(datos)}")
    
    for i, fila in enumerate(datos):
        if not isinstance(fila, list):
            raise ValueError(f"La fila {i+1} debe ser una lista")
        
        if len(fila) != columnas_esperadas:
            raise ValueError(f"La fila {i+1} debe tener {columnas_esperadas} elementos, "
                           f"pero tiene {len(fila)}")
        
        for j, elemento in enumerate(fila):
            try:
                validar_numero(elemento)
            except ValueError as e:
                raise ValueError(f"Error en elemento [{i+1}][{j+1}]: {e}")


def validar_entrada_entero(entrada, min_valor=None, max_valor=None):
    """
    Valida que una entrada sea un entero dentro de un rango específico.
    
    Args:
        entrada: Valor a validar
        min_valor (int, optional): Valor mínimo permitido
        max_valor (int, optional): Valor máximo permitido
        
    Returns:
        int: Valor entero validado
        
    Raises:
        ValueError: Si la entrada no es válida
    """
    if isinstance(entrada, str):
        entrada = entrada.strip()
        if entrada == "":
            raise ValueError("La entrada no puede estar vacía")
    
    try:
        valor = int(entrada)
    except (ValueError, TypeError):
        raise ValueError(f"'{entrada}' no es un número entero válido")
    
    if min_valor is not None and valor < min_valor:
        raise ValueError(f"El valor debe ser al menos {min_valor}")
    
    if max_valor is not None and valor > max_valor:
        raise ValueError(f"El valor no puede ser mayor que {max_valor}")
    
    return valor


def validar_opcion_menu(entrada, opciones_validas):
    """
    Valida que una entrada sea una opción válida de menú.
    
    Args:
        entrada: Valor ingresado por el usuario
        opciones_validas (list): Lista de opciones válidas
        
    Returns:
        str: Opción validada
        
    Raises:
        ValueError: Si la opción no es válida
    """
    if isinstance(entrada, str):
        entrada = entrada.strip().lower()
    
    entrada_str = str(entrada).strip().lower()
    opciones_str = [str(opcion).strip().lower() for opcion in opciones_validas]
    
    if entrada_str not in opciones_str:
        opciones_mostrar = ", ".join(map(str, opciones_validas))
        raise ValueError(f"Opción inválida. Las opciones válidas son: {opciones_mostrar}")
    
    # Retornar la opción original correspondiente
    indice = opciones_str.index(entrada_str)
    return opciones_validas[indice]


def es_numero_valido(cadena):
    """
    Verifica si una cadena representa un número válido.
    
    Args:
        cadena (str): Cadena a verificar
        
    Returns:
        bool: True si es un número válido, False en caso contrario
    """
    if not isinstance(cadena, str):
        return False
    
    cadena = cadena.strip()
    if cadena == "":
        return False
    
    # Verificar fracción
    if '/' in cadena:
        try:
            Fraction(cadena)
            return True
        except (ValueError, ZeroDivisionError):
            return False
    
    # Verificar entero
    try:
        int(cadena)
        return True
    except ValueError:
        pass
    
    # Verificar decimal
    try:
        float(cadena)
        return True
    except ValueError:
        return False


def validar_rango_numerico(min_valor, max_valor):
    """
    Valida que un rango numérico sea válido.
    
    Args:
        min_valor: Valor mínimo del rango
        max_valor: Valor máximo del rango
        
    Raises:
        ValueError: Si el rango no es válido
    """
    try:
        min_num = validar_numero(min_valor)
        max_num = validar_numero(max_valor)
    except ValueError as e:
        raise ValueError(f"Error en el rango: {e}")
    
    if min_num >= max_num:
        raise ValueError("El valor mínimo debe ser menor que el valor máximo")
