#!/usr/bin/env python3
"""
Ejemplo Básico - Generador de Matrices
=====================================

Demuestra el uso básico de la clase Matriz y operaciones simples.
Este ejemplo te ayudará a entender cómo usar la biblioteca.

Autor: Nicolas
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.matriz import Matriz
from src.operaciones import *
from src.utilidades import mostrar_separador


def ejemplo_creacion_matrices():
    """Demuestra la creación de matrices."""
    mostrar_separador("CREACIÓN DE MATRICES")
    
    print("1. Creando una matriz 3x3 con ceros:")
    matriz_ceros = Matriz(3, 3)
    matriz_ceros.mostrar("Matriz de Ceros")
    
    print("2. Creando una matriz 2x3 con datos específicos:")
    matriz_datos = Matriz(2, 3)
    datos = [[1, 2, 3], [4, 5, 6]]
    matriz_datos.llenar_manual(datos)
    matriz_datos.mostrar("Matriz con Datos")
    
    print("3. Creando una matriz 3x3 con números aleatorios:")
    matriz_aleatoria = Matriz(3, 3)
    matriz_aleatoria.llenar_aleatorio(-5, 5)
    matriz_aleatoria.mostrar("Matriz Aleatoria")


def ejemplo_operaciones_basicas():
    """Demuestra operaciones básicas con matrices."""
    mostrar_separador("OPERACIONES BÁSICAS")
    
    # Crear matrices para operar
    print("Creando matrices para las operaciones:")
    
    matriz_a = Matriz(2, 2)
    matriz_a.llenar_manual([[1, 2], [3, 4]])
    matriz_a.mostrar("Matriz A")
    
    matriz_b = Matriz(2, 2)
    matriz_b.llenar_manual([[5, 6], [7, 8]])
    matriz_b.mostrar("Matriz B")
    
    # Suma
    print("\\n--- SUMA DE MATRICES ---")
    suma = sumar_matrices(matriz_a, matriz_b)
    suma.mostrar("A + B")
    
    # Resta
    print("\\n--- RESTA DE MATRICES ---")
    resta = restar_matrices(matriz_b, matriz_a)
    resta.mostrar("B - A")
    
    # Multiplicación por escalar
    print("\\n--- MULTIPLICACIÓN POR ESCALAR ---")
    escalar = multiplicar_por_escalar(matriz_a, 3)
    escalar.mostrar("A × 3")


def ejemplo_multiplicacion_matrices():
    """Demuestra la multiplicación de matrices."""
    mostrar_separador("MULTIPLICACIÓN DE MATRICES")
    
    print("Para multiplicar matrices A×B, las columnas de A deben")
    print("ser iguales a las filas de B.\\n")
    
    # Crear matrices compatibles para multiplicación
    matriz_2x3 = Matriz(2, 3)
    matriz_2x3.llenar_manual([[1, 2, 3], [4, 5, 6]])
    matriz_2x3.mostrar("Matriz 2×3")
    
    matriz_3x2 = Matriz(3, 2)
    matriz_3x2.llenar_manual([[7, 8], [9, 10], [11, 12]])
    matriz_3x2.mostrar("Matriz 3×2")
    
    # Multiplicación
    producto = multiplicar_matrices(matriz_2x3, matriz_3x2)
    producto.mostrar("Producto (2×3) × (3×2) = (2×2)")
    
    print("Verificación del primer elemento (fila 1, columna 1):")
    print("1×7 + 2×9 + 3×11 = 7 + 18 + 33 = 58")


def ejemplo_propiedades_matrices():
    """Demuestra propiedades y operaciones especiales."""
    mostrar_separador("PROPIEDADES Y OPERACIONES ESPECIALES")
    
    # Matriz cuadrada
    print("1. Matriz cuadrada y su transpuesta:")
    matriz_cuadrada = Matriz(3, 3)
    matriz_cuadrada.llenar_manual([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matriz_cuadrada.mostrar("Matriz Original")
    
    print(f"¿Es cuadrada? {matriz_cuadrada.es_cuadrada()}")
    
    transpuesta = matriz_cuadrada.transponer()
    transpuesta.mostrar("Matriz Transpuesta")
    
    # Matriz identidad
    print("\\n2. Matriz identidad:")
    identidad = crear_matriz_identidad(3)
    identidad.mostrar("Matriz Identidad 3×3")
    
    # Potencia de matriz
    print("\\n3. Potencia de matriz:")
    matriz_pequeña = Matriz(2, 2)
    matriz_pequeña.llenar_manual([[2, 1], [0, 2]])
    matriz_pequeña.mostrar("Matriz Base")
    
    potencia = potencia_matriz(matriz_pequeña, 2)
    potencia.mostrar("Matriz Base²")


def ejemplo_tipos_numericos():
    """Demuestra el uso de diferentes tipos numéricos."""
    mostrar_separador("TIPOS NUMÉRICOS SOPORTADOS")
    
    print("La biblioteca soporta enteros, decimales y fracciones:")
    
    # Matriz con diferentes tipos
    matriz_mixta = Matriz(2, 3)
    datos_mixtos = [
        [1, 2.5, "1/2"],      # entero, decimal, fracción
        ["3/4", -1, 3.14]     # fracción, entero, decimal
    ]
    matriz_mixta.llenar_manual(datos_mixtos)
    matriz_mixta.mostrar("Matriz con Tipos Mixtos")
    
    # Operación con fracción
    print("\\nMultiplicación por fracción (1/2):")
    from fractions import Fraction
    resultado = multiplicar_por_escalar(matriz_mixta, Fraction(1, 2))
    resultado.mostrar("Resultado × 1/2")


def ejemplo_comparacion_matrices():
    """Demuestra la comparación entre matrices."""
    mostrar_separador("COMPARACIÓN DE MATRICES")
    
    # Matrices iguales
    matriz_1 = Matriz(2, 2)
    matriz_1.llenar_manual([[1, 2], [3, 4]])
    
    matriz_2 = Matriz(2, 2)
    matriz_2.llenar_manual([[1, 2], [3, 4]])
    
    matriz_3 = Matriz(2, 2)
    matriz_3.llenar_manual([[1, 2], [3, 5]])  # Diferente
    
    matriz_1.mostrar("Matriz 1")
    matriz_2.mostrar("Matriz 2")
    matriz_3.mostrar("Matriz 3")
    
    print(f"¿Matriz 1 == Matriz 2? {son_matrices_iguales(matriz_1, matriz_2)}")
    print(f"¿Matriz 1 == Matriz 3? {son_matrices_iguales(matriz_1, matriz_3)}")


def main():
    """Función principal que ejecuta todos los ejemplos."""
    print("🎯 EJEMPLOS BÁSICOS - GENERADOR DE MATRICES")
    print("=" * 60)
    print("Este ejemplo demuestra las funcionalidades básicas de la biblioteca.")
    print("¡Observa los resultados y aprende cómo usar cada función!\\n")
    
    try:
        ejemplo_creacion_matrices()
        input("\\n⏵ Presiona Enter para continuar con operaciones básicas...")
        
        ejemplo_operaciones_basicas()
        input("\\n⏵ Presiona Enter para continuar con multiplicación de matrices...")
        
        ejemplo_multiplicacion_matrices()
        input("\\n⏵ Presiona Enter para continuar con propiedades especiales...")
        
        ejemplo_propiedades_matrices()
        input("\\n⏵ Presiona Enter para continuar con tipos numéricos...")
        
        ejemplo_tipos_numericos()
        input("\\n⏵ Presiona Enter para continuar con comparación de matrices...")
        
        ejemplo_comparacion_matrices()
        
        mostrar_separador("¡EJEMPLO COMPLETADO!")
        print("🎉 Has visto todas las funcionalidades básicas.")
        print("🔗 Prueba también los otros ejemplos:")
        print("   - ejemplo_fracciones.py")
        print("   - ejemplo_operaciones.py")
        print("\\n🚀 ¡Ahora puedes usar la biblioteca en tus propios proyectos!")
        
    except KeyboardInterrupt:
        print("\\n\\n👋 ¡Ejemplo interrumpido por el usuario!")
    except Exception as e:
        print(f"\\n❌ Error durante el ejemplo: {e}")


if __name__ == "__main__":
    main()
