"""
Utilidades y Funciones Auxiliares
=================================

Funciones de apoyo para el manejo de matrices y formateo de datos.
Incluye utilidades para entrada/salida y conversiones.

Autor: Nicolas
"""

from fractions import Fraction
import os
import sys


def formatear_numero(numero):
    """
    Formatea un número para mostrarlo de manera legible.
    
    Args:
        numero: Número a formatear (int, float, Fraction)
        
    Returns:
        str: Número formateado como string
    """
    if isinstance(numero, Fraction):
        if numero.denominator == 1:
            return str(numero.numerator)
        else:
            return f"{numero.numerator}/{numero.denominator}"
    
    elif isinstance(numero, float):
        # Si es un número entero disfrazado de float, mostrarlo como entero
        if numero.is_integer():
            return str(int(numero))
        else:
            # Formatear con máximo 6 decimales, eliminando ceros innecesarios
            return f"{numero:.6f}".rstrip('0').rstrip('.')
    
    else:
        return str(numero)


def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    Compatible con Windows, Linux y macOS.
    """
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux y macOS
        os.system('clear')


def pausar():
    """
    Pausa la ejecución hasta que el usuario presione Enter.
    """
    input("\nPresiona Enter para continuar...")


def mostrar_separador(titulo="", ancho=50):
    """
    Muestra un separador visual con título opcional.
    
    Args:
        titulo (str): Título a mostrar en el separador
        ancho (int): Ancho del separador
    """
    if titulo:
        print(f"\n{'='*ancho}")
        print(f"{titulo:^{ancho}}")
        print('='*ancho)
    else:
        print('='*ancho)


def centrar_texto(texto, ancho=50):
    """
    Centra un texto en un ancho específico.
    
    Args:
        texto (str): Texto a centrar
        ancho (int): Ancho total disponible
        
    Returns:
        str: Texto centrado
    """
    return f"{texto:^{ancho}}"


def solicitar_numero(mensaje, tipo_numero="cualquiera"):
    """
    Solicita un número al usuario con validación.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        tipo_numero (str): Tipo de número esperado ("entero", "decimal", "fraccion", "cualquiera")
        
    Returns:
        int, float, o Fraction: Número ingresado por el usuario
    """
    from .validadores import validar_numero, es_numero_valido
    
    while True:
        try:
            entrada = input(f"{mensaje}: ").strip()
            
            if entrada == "":
                print("❌ No puedes dejar este campo vacío.")
                continue
            
            if tipo_numero == "entero":
                return int(entrada)
            elif tipo_numero == "decimal":
                return float(entrada)
            elif tipo_numero == "fraccion":
                if '/' not in entrada:
                    print("❌ Debes ingresar una fracción (ejemplo: 3/4)")
                    continue
                return Fraction(entrada)
            else:  # cualquiera
                return validar_numero(entrada)
                
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Por favor intenta de nuevo.")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada por el usuario.")
            sys.exit(0)


def solicitar_entero(mensaje, min_valor=None, max_valor=None):
    """
    Solicita un número entero al usuario con validación de rango.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        min_valor (int, optional): Valor mínimo permitido
        max_valor (int, optional): Valor máximo permitido
        
    Returns:
        int: Número entero validado
    """
    from .validadores import validar_entrada_entero
    
    while True:
        try:
            entrada = input(f"{mensaje}: ").strip()
            return validar_entrada_entero(entrada, min_valor, max_valor)
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Por favor intenta de nuevo.")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada por el usuario.")
            sys.exit(0)


def solicitar_opcion(mensaje, opciones_validas):
    """
    Solicita una opción al usuario de una lista de opciones válidas.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        opciones_validas (list): Lista de opciones válidas
        
    Returns:
        str: Opción seleccionada por el usuario
    """
    from .validadores import validar_opcion_menu
    
    while True:
        try:
            entrada = input(f"{mensaje}: ").strip()
            return validar_opcion_menu(entrada, opciones_validas)
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Por favor intenta de nuevo.")
        except KeyboardInterrupt:
            print("\n\n👋 Operación cancelada por el usuario.")
            sys.exit(0)


def mostrar_lista_numerada(items, titulo="Opciones"):
    """
    Muestra una lista numerada de elementos.
    
    Args:
        items (list): Lista de elementos a mostrar
        titulo (str): Título de la lista
    """
    print(f"\n{titulo}:")
    print("-" * len(titulo + ":"))
    
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
    print()


def confirmar_accion(mensaje="¿Deseas continuar?"):
    """
    Solicita confirmación al usuario para una acción.
    
    Args:
        mensaje (str): Mensaje de confirmación
        
    Returns:
        bool: True si el usuario confirma, False en caso contrario
    """
    try:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        return respuesta in ['s', 'sí', 'si', 'yes', 'y']
    except KeyboardInterrupt:
        print("\n\n👋 Operación cancelada por el usuario.")
        return False


def convertir_a_fraccion_si_posible(numero):
    """
    Convierte un número decimal a fracción si es posible representarlo exactamente.
    
    Args:
        numero: Número a convertir
        
    Returns:
        Fraction o número original: Fracción si es posible, número original si no
    """
    if isinstance(numero, (int, Fraction)):
        return numero
    
    if isinstance(numero, float):
        try:
            fraccion = Fraction(numero).limit_denominator(10000)
            # Solo convertir si la representación es exacta o muy cercana
            if abs(float(fraccion) - numero) < 1e-10:
                return fraccion
        except:
            pass
    
    return numero


def obtener_info_sistema():
    """
    Obtiene información básica del sistema.
    
    Returns:
        dict: Información del sistema
    """
    return {
        'python_version': sys.version,
        'platform': sys.platform,
        'os_name': os.name
    }


def crear_menu_simple(titulo, opciones):
    """
    Crea y muestra un menú simple.
    
    Args:
        titulo (str): Título del menú
        opciones (list): Lista de opciones del menú
        
    Returns:
        int: Índice de la opción seleccionada (0-based)
    """
    mostrar_separador(titulo)
    mostrar_lista_numerada(opciones)
    
    while True:
        try:
            seleccion = solicitar_entero("Selecciona una opción", 1, len(opciones))
            return seleccion - 1  # Convertir a 0-based
        except ValueError:
            continue


def formatear_matriz_como_texto(matriz):
    """
    Convierte una matriz en una representación de texto limpia.
    
    Args:
        matriz (Matriz): Matriz a formatear
        
    Returns:
        str: Representación de texto de la matriz
    """
    if not matriz or not matriz.datos:
        return "Matriz vacía"
    
    # Calcular el ancho máximo necesario
    max_ancho = 0
    for fila in matriz.datos:
        for elemento in fila:
            ancho = len(formatear_numero(elemento))
            max_ancho = max(max_ancho, ancho)
    
    max_ancho = max(max_ancho, 4)  # Ancho mínimo
    
    # Construir la representación
    lineas = []
    for fila in matriz.datos:
        elementos_formateados = []
        for elemento in fila:
            elem_str = formatear_numero(elemento)
            elementos_formateados.append(f"{elem_str:>{max_ancho}}")
        
        lineas.append("[ " + "  ".join(elementos_formateados) + " ]")
    
    return "\n".join(lineas)
