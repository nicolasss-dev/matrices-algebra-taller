#!/usr/bin/env python3
"""
Ejemplo con Fracciones - Generador de Matrices
==============================================

Demuestra el trabajo con fracciones en matrices.
Ideal para cálculos exactos sin errores de punto flotante.

Autor: Nicolas
"""

import sys
import os
from fractions import Fraction

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.matriz import Matriz
from src.operaciones import *
from src.utilidades import mostrar_separador


def ejemplo_fracciones_basicas():
    """Demuestra el uso básico de fracciones en matrices."""
    mostrar_separador("FRACCIONES EN MATRICES")
    
    print("Las fracciones permiten cálculos exactos sin errores de redondeo.")
    print("Ejemplo: 1/3 + 1/3 + 1/3 = 1 (exacto)\\n")
    
    # Crear matriz con fracciones
    matriz_fracciones = Matriz(2, 3)
    datos = [
        ["1/2", "1/3", "1/4"],
        ["2/3", "3/4", "5/6"]
    ]
    matriz_fracciones.llenar_manual(datos)
    matriz_fracciones.mostrar("Matriz con Fracciones")
    
    # Mostrar algunos elementos específicos
    print("Elementos específicos:")
    print(f"  Elemento [0][0] = {matriz_fracciones.obtener_elemento(0, 0)}")
    print(f"  Elemento [1][2] = {matriz_fracciones.obtener_elemento(1, 2)}")


def ejemplo_operaciones_fracciones():
    """Demuestra operaciones entre matrices con fracciones."""
    mostrar_separador("OPERACIONES CON FRACCIONES")
    
    # Crear dos matrices con fracciones
    matriz_a = Matriz(2, 2)
    matriz_a.llenar_manual([["1/2", "1/3"], ["1/4", "1/5"]])
    matriz_a.mostrar("Matriz A")
    
    matriz_b = Matriz(2, 2)
    matriz_b.llenar_manual([["1/6", "1/7"], ["1/8", "1/9"]])
    matriz_b.mostrar("Matriz B")
    
    # Suma de fracciones
    print("\\n--- SUMA DE FRACCIONES ---")
    suma = sumar_matrices(matriz_a, matriz_b)
    suma.mostrar("A + B")
    
    # Verificar manualmente: 1/2 + 1/6 = 3/6 + 1/6 = 4/6 = 2/3
    print("Verificación: 1/2 + 1/6 = 3/6 + 1/6 = 4/6 = 2/3")
    print(f"Resultado computado: {suma.obtener_elemento(0, 0)}")


def ejemplo_multiplicacion_fracciones():
    """Demuestra la multiplicación con fracciones."""
    mostrar_separador("MULTIPLICACIÓN CON FRACCIONES")
    
    # Matriz para multiplicar
    matriz = Matriz(2, 2)
    matriz.llenar_manual([["1/2", "2/3"], ["3/4", "4/5"]])
    matriz.mostrar("Matriz Original")
    
    # Multiplicar por fracción
    print("\\n--- MULTIPLICACIÓN POR 3/2 ---")
    resultado = multiplicar_por_escalar(matriz, Fraction(3, 2))
    resultado.mostrar("Matriz × 3/2")
    
    # Verificar: (1/2) × (3/2) = 3/4
    print("Verificación: (1/2) × (3/2) = 3/4")
    print(f"Resultado computado: {resultado.obtener_elemento(0, 0)}")


def ejemplo_sistema_ecuaciones():
    """Demuestra resolución aproximada de un sistema simple con fracciones."""
    mostrar_separador("SISTEMA DE ECUACIONES (Ejemplo educativo)")
    
    print("Sistema de ecuaciones:")
    print("  2x + 3y = 7")
    print("  4x + 6y = 14")
    print()
    print("En forma matricial: A × X = B")
    print("Donde A es la matriz de coeficientes, X el vector de incógnitas, B el vector resultado.")
    
    # Matriz de coeficientes
    matriz_coef = Matriz(2, 2)
    matriz_coef.llenar_manual([[2, 3], [4, 6]])
    matriz_coef.mostrar("Matriz de Coeficientes (A)")
    
    # Convertir a fracciones para cálculos exactos
    print("\\n--- CONVERSIÓN A FRACCIONES ---")
    matriz_coef_frac = Matriz(2, 2)
    matriz_coef_frac.llenar_manual([["2/1", "3/1"], ["4/1", "6/1"]])
    matriz_coef_frac.mostrar("Matriz A (con fracciones)")
    
    print("\\nNota: Este sistema tiene infinitas soluciones porque la segunda")
    print("ecuación es el doble de la primera (4x + 6y = 2(2x + 3y) = 2×7 = 14)")


def ejemplo_precision_fracciones():
    """Demuestra la precisión de fracciones vs decimales."""
    mostrar_separador("PRECISIÓN: FRACCIONES VS DECIMALES")
    
    print("Comparación de precisión entre fracciones y decimales:")
    print()
    
    # Con fracciones (exacto)
    print("--- CON FRACCIONES (Exacto) ---")
    matriz_frac = Matriz(1, 3)
    matriz_frac.llenar_manual([["1/3", "1/3", "1/3"]])
    matriz_frac.mostrar("Tres tercios")
    
    suma_frac = matriz_frac.obtener_elemento(0, 0) + matriz_frac.obtener_elemento(0, 1) + matriz_frac.obtener_elemento(0, 2)
    print(f"Suma de fracciones: {suma_frac}")
    print(f"¿Es igual a 1? {suma_frac == 1}")
    
    # Con decimales (aproximado)
    print("\\n--- CON DECIMALES (Aproximado) ---")
    matriz_dec = Matriz(1, 3)
    matriz_dec.llenar_manual([[0.3333333, 0.3333333, 0.3333333]])
    matriz_dec.mostrar("Tres tercios (decimal)")
    
    suma_dec = matriz_dec.obtener_elemento(0, 0) + matriz_dec.obtener_elemento(0, 1) + matriz_dec.obtener_elemento(0, 2)
    print(f"Suma de decimales: {suma_dec}")
    print(f"¿Es igual a 1? {suma_dec == 1}")
    print(f"Diferencia con 1: {abs(1 - suma_dec)}")


def ejemplo_conversion_fracciones():
    """Demuestra la conversión entre fracciones y decimales."""
    mostrar_separador("CONVERSIÓN ENTRE TIPOS")
    
    print("Ejemplos de conversión automática:")
    
    # Crear matriz mixta
    matriz_mixta = Matriz(3, 3)
    datos_mixtos = [
        [1, "1/2", 0.5],           # entero, fracción, decimal
        ["3/4", 0.75, Fraction(3, 4)],  # fracción, decimal, objeto Fraction
        [2, "2/1", 2.0]            # entero, fracción equivalente, decimal
    ]
    matriz_mixta.llenar_manual(datos_mixtos)
    matriz_mixta.mostrar("Matriz con Tipos Mixtos")
    
    print("\\nNota: Observa cómo se representan los diferentes tipos:")
    print("  - Enteros se muestran como enteros")
    print("  - Fracciones se muestran en forma de fracción")
    print("  - Decimales se muestran como decimales")
    print("  - Fracciones equivalentes a enteros se simplifican")


def ejemplo_fracciones_avanzadas():
    """Demuestra operaciones avanzadas con fracciones."""
    mostrar_separador("OPERACIONES AVANZADAS CON FRACCIONES")
    
    # Crear matriz con fracciones complejas
    matriz = Matriz(2, 2)
    matriz.llenar_manual([["22/7", "355/113"], ["1/137", "8/13"]])  # π aproximado, constante estructura fina, otros
    matriz.mostrar("Matriz con Fracciones Especiales")
    
    print("\\nFracciones especiales usadas:")
    print("  22/7 ≈ π (aproximación clásica de pi)")
    print("  355/113 ≈ π (aproximación muy precisa de pi)")
    print("  1/137 ≈ constante de estructura fina")
    print("  8/13 ≈ número áureo - 1")
    
    # Potencia de la matriz
    try:
        print("\\n--- POTENCIA DE LA MATRIZ ---")
        potencia = potencia_matriz(matriz, 2)
        potencia.mostrar("Matriz²")
    except Exception as e:
        print(f"Nota: {e}")
    
    # Determinante aproximado (no implementado, solo para demostración)
    print("\\nNota: Para cálculos más avanzados como determinantes o inversa,")
    print("las fracciones mantienen la precisión exacta durante todo el proceso.")


def main():
    """Función principal que ejecuta todos los ejemplos."""
    print("🔢 EJEMPLOS CON FRACCIONES - GENERADOR DE MATRICES")
    print("=" * 60)
    print("Este ejemplo demuestra el poder de las fracciones para cálculos exactos.")
    print("¡Perfecto para matemáticas simbólicas y evitar errores de redondeo!\\n")
    
    try:
        ejemplo_fracciones_basicas()
        input("\\n⏵ Presiona Enter para continuar con operaciones...")
        
        ejemplo_operaciones_fracciones()
        input("\\n⏵ Presiona Enter para continuar con multiplicación...")
        
        ejemplo_multiplicacion_fracciones()
        input("\\n⏵ Presiona Enter para ver un ejemplo de sistema de ecuaciones...")
        
        ejemplo_sistema_ecuaciones()
        input("\\n⏵ Presiona Enter para comparar precisión...")
        
        ejemplo_precision_fracciones()
        input("\\n⏵ Presiona Enter para ver conversiones...")
        
        ejemplo_conversion_fracciones()
        input("\\n⏵ Presiona Enter para ejemplos avanzados...")
        
        ejemplo_fracciones_avanzadas()
        
        mostrar_separador("¡EJEMPLOS CON FRACCIONES COMPLETADOS!")
        print("🎯 Ventajas de las fracciones:")
        print("   ✓ Precisión exacta (sin errores de redondeo)")
        print("   ✓ Representación natural de números racionales")
        print("   ✓ Ideales para matemática simbólica")
        print("   ✓ Simplificación automática")
        print("\\n🔗 Casos de uso recomendados:")
        print("   • Cálculos financieros exactos")
        print("   • Matemática educativa")
        print("   • Álgebra simbólica")
        print("   • Cuando la precisión es crítica")
        
    except KeyboardInterrupt:
        print("\\n\\n👋 ¡Ejemplo interrumpido por el usuario!")
    except Exception as e:
        print(f"\\n❌ Error durante el ejemplo: {e}")


if __name__ == "__main__":
    main()
