#!/usr/bin/env python3
"""
Ejemplo de Operaciones Avanzadas - Generador de Matrices
========================================================

Demuestra operaciones complejas y casos de uso avanzados.
Incluye ejemplos prácticos y demostraciones matemáticas.

Autor: Nicolas
"""

import sys
import os
from fractions import Fraction

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.matriz import Matriz
from src.operaciones import *
from src.utilidades import mostrar_separador, confirmar_accion


def ejemplo_cadenas_operaciones():
    """Demuestra cadenas de operaciones complejas."""
    mostrar_separador("CADENAS DE OPERACIONES")
    
    print("Ejemplo: (A + B) × C - D × 2")
    print()
    
    # Crear matrices
    A = Matriz(2, 2)
    A.llenar_manual([[1, 2], [3, 4]])
    A.mostrar("Matriz A")
    
    B = Matriz(2, 2)
    B.llenar_manual([[2, 1], [1, 2]])
    B.mostrar("Matriz B")
    
    C = Matriz(2, 2)
    C.llenar_manual([[1, 0], [0, 1]])  # Matriz identidad
    C.mostrar("Matriz C (Identidad)")
    
    D = Matriz(2, 2)
    D.llenar_manual([[1, 1], [1, 1]])
    D.mostrar("Matriz D")
    
    # Realizar operaciones paso a paso
    print("\\n--- PASO 1: A + B ---")
    suma_AB = sumar_matrices(A, B)
    suma_AB.mostrar("A + B")
    
    print("\\n--- PASO 2: (A + B) × C ---")
    producto1 = multiplicar_matrices(suma_AB, C)
    producto1.mostrar("(A + B) × C")
    
    print("\\n--- PASO 3: D × 2 ---")
    D_por_2 = multiplicar_por_escalar(D, 2)
    D_por_2.mostrar("D × 2")
    
    print("\\n--- PASO 4: RESULTADO FINAL ---")
    resultado = restar_matrices(producto1, D_por_2)
    resultado.mostrar("(A + B) × C - D × 2")


def ejemplo_potencias_matrices():
    """Demuestra cálculos de potencias de matrices."""
    mostrar_separador("POTENCIAS DE MATRICES")
    
    print("Calculando potencias de una matriz de rotación 2D (90°)")
    
    # Matriz de rotación 90° (aproximada con enteros)
    matriz_rot = Matriz(2, 2)
    matriz_rot.llenar_manual([[0, -1], [1, 0]])
    matriz_rot.mostrar("Matriz de Rotación 90°")
    
    print("\\nCalculando potencias sucesivas:")
    
    for i in range(1, 5):
        print(f"\\n--- POTENCIA {i} ---")
        potencia = potencia_matriz(matriz_rot, i)
        potencia.mostrar(f"Rotación^{i}")
        
        if i == 1:
            print("Rotación 90°")
        elif i == 2:
            print("Rotación 180°")
        elif i == 3:
            print("Rotación 270°")
        elif i == 4:
            print("Rotación 360° = Matriz Identidad")


def ejemplo_matrices_especiales():
    """Demuestra creación y propiedades de matrices especiales."""
    mostrar_separador("MATRICES ESPECIALES")
    
    print("1. Matriz Identidad y sus propiedades:")
    identidad = crear_matriz_identidad(3)
    identidad.mostrar("Identidad 3×3")
    
    # Propiedad: A × I = A
    A = Matriz(3, 3)
    A.llenar_aleatorio(1, 9)
    A.mostrar("Matriz A (aleatoria)")
    
    producto_AI = multiplicar_matrices(A, identidad)
    producto_AI.mostrar("A × I")
    
    print(f"¿A × I = A? {son_matrices_iguales(A, producto_AI)}")
    
    print("\\n2. Matriz de Unos:")
    unos = crear_matriz_unos(2, 3)
    unos.mostrar("Matriz de Unos 2×3")
    
    print("\\n3. Matriz de Ceros:")
    ceros = crear_matriz_ceros(3, 2)
    ceros.mostrar("Matriz de Ceros 3×2")
    
    # Propiedad: A + 0 = A
    print("\\n--- PROPIEDAD: A + 0 = A ---")
    ceros_2x2 = crear_matriz_ceros(3, 3)
    suma_con_cero = sumar_matrices(A, ceros_2x2)
    print(f"¿A + 0 = A? {son_matrices_iguales(A, suma_con_cero)}")


def ejemplo_transformaciones_geometricas():
    """Demuestra transformaciones geométricas usando matrices."""
    mostrar_separador("TRANSFORMACIONES GEOMÉTRICAS")
    
    print("Simulando transformaciones 2D con matrices 2×2")
    print("Punto original: (1, 0) - representado como vector columna\\n")
    
    # Punto como matriz columna
    punto = Matriz(2, 1)
    punto.llenar_manual([[1], [0]])
    punto.mostrar("Punto Original (1, 0)")
    
    print("\\n1. Escalado por factor 2:")
    matriz_escala = Matriz(2, 2)
    matriz_escala.llenar_manual([[2, 0], [0, 2]])
    matriz_escala.mostrar("Matriz de Escalado")
    
    punto_escalado = multiplicar_matrices(matriz_escala, punto)
    punto_escalado.mostrar("Punto Escalado")
    
    print("\\n2. Reflexión sobre el eje X:")
    matriz_reflexion = Matriz(2, 2)
    matriz_reflexion.llenar_manual([[1, 0], [0, -1]])
    matriz_reflexion.mostrar("Matriz de Reflexión")
    
    punto_reflejado = multiplicar_matrices(matriz_reflexion, punto)
    punto_reflejado.mostrar("Punto Reflejado")
    
    print("\\n3. Cizallamiento (Shear):")
    matriz_cizalla = Matriz(2, 2)
    matriz_cizalla.llenar_manual([[1, 1], [0, 1]])
    matriz_cizalla.mostrar("Matriz de Cizallamiento")
    
    punto_cizallado = multiplicar_matrices(matriz_cizalla, punto)
    punto_cizallado.mostrar("Punto Cizallado")


def ejemplo_analisis_sistema():
    """Demuestra análisis de un sistema de ecuaciones lineales."""
    mostrar_separador("ANÁLISIS DE SISTEMA DE ECUACIONES")
    
    print("Sistema de ecuaciones lineales 3×3:")
    print("  2x + 3y + z = 10")
    print("  x + 4y + 2z = 13") 
    print("  3x + y + 3z = 14")
    print()
    
    # Matriz de coeficientes
    A = Matriz(3, 3)
    A.llenar_manual([[2, 3, 1], [1, 4, 2], [3, 1, 3]])
    A.mostrar("Matriz de Coeficientes (A)")
    
    # Vector de constantes (como matriz columna)
    b = Matriz(3, 1)
    b.llenar_manual([[10], [13], [14]])
    b.mostrar("Vector de Constantes (b)")
    
    print("\\nPara resolver Ax = b, necesitaríamos calcular x = A⁻¹b")
    print("(La inversión de matrices no está implementada en esta versión)")
    
    # Análisis con fracciones para mayor precisión
    print("\\n--- CONVERSIÓN A FRACCIONES PARA ANÁLISIS EXACTO ---")
    A_frac = Matriz(3, 3)
    A_frac.llenar_manual([["2/1", "3/1", "1/1"], 
                          ["1/1", "4/1", "2/1"], 
                          ["3/1", "1/1", "3/1"]])
    A_frac.mostrar("Matriz A (fracciones)")


def ejemplo_operaciones_grandes():
    """Demuestra operaciones con matrices más grandes."""
    mostrar_separador("OPERACIONES CON MATRICES GRANDES")
    
    print("Trabajando con matrices 5×5 (más grandes)")
    
    # Crear matrices grandes
    print("\\n1. Creando matrices 5×5 aleatorias:")
    A_grande = Matriz(5, 5)
    A_grande.llenar_aleatorio(-3, 3)
    print("Matriz A (5×5) - generada aleatoriamente")
    
    B_grande = Matriz(5, 5)
    B_grande.llenar_aleatorio(-2, 2)
    print("Matriz B (5×5) - generada aleatoriamente")
    
    if confirmar_accion("¿Mostrar las matrices grandes?"):
        A_grande.mostrar("Matriz A")
        B_grande.mostrar("Matriz B")
    
    print("\\n2. Suma de matrices grandes:")
    suma_grande = sumar_matrices(A_grande, B_grande)
    if confirmar_accion("¿Mostrar el resultado de A + B?"):
        suma_grande.mostrar("A + B")
    
    print("\\n3. Multiplicación de matrices grandes:")
    print("Calculando A × B (operación más costosa)...")
    producto_grande = multiplicar_matrices(A_grande, B_grande)
    print("✓ Multiplicación completada")
    
    if confirmar_accion("¿Mostrar el resultado de A × B?"):
        producto_grande.mostrar("A × B")
    
    print(f"\\nEstadísticas:")
    print(f"  Dimensiones resultantes: {producto_grande.filas}×{producto_grande.columnas}")
    print(f"  Total de elementos: {producto_grande.filas * producto_grande.columnas}")


def ejemplo_precision_acumulada():
    """Demuestra la acumulación de errores en operaciones repetidas."""
    mostrar_separador("ANÁLISIS DE PRECISIÓN")
    
    print("Comparando precisión: enteros vs decimales vs fracciones")
    print("Operación repetida: ((matriz / 3) × 3) repetida varias veces\\n")
    
    # Con enteros
    print("--- CON ENTEROS ---")
    matriz_int = Matriz(2, 2)
    matriz_int.llenar_manual([[3, 6], [9, 12]])
    matriz_int.mostrar("Original (enteros)")
    
    resultado_int = matriz_int.copiar()
    for i in range(3):
        # División entera puede causar pérdida
        temp = multiplicar_por_escalar(resultado_int, Fraction(1, 3))
        resultado_int = multiplicar_por_escalar(temp, 3)
    
    resultado_int.mostrar("Después de 3 ciclos (int)")
    
    # Con fracciones (exacto)
    print("\\n--- CON FRACCIONES ---")
    matriz_frac = Matriz(2, 2)
    matriz_frac.llenar_manual([["3/1", "6/1"], ["9/1", "12/1"]])
    matriz_frac.mostrar("Original (fracciones)")
    
    resultado_frac = matriz_frac.copiar()
    for i in range(3):
        temp = multiplicar_por_escalar(resultado_frac, Fraction(1, 3))
        resultado_frac = multiplicar_por_escalar(temp, 3)
    
    resultado_frac.mostrar("Después de 3 ciclos (fracciones)")
    
    print("\\nObservación: Las fracciones mantienen la precisión exacta")
    print("mientras que otros tipos pueden acumular errores.")


def main():
    """Función principal que ejecuta todos los ejemplos."""
    print("🚀 EJEMPLOS AVANZADOS - GENERADOR DE MATRICES")
    print("=" * 60)
    print("Demostraciones de casos de uso complejos y operaciones avanzadas.")
    print("Perfecto para entender el potencial completo de la biblioteca.\\n")
    
    ejemplos = [
        ("Cadenas de operaciones", ejemplo_cadenas_operaciones),
        ("Potencias de matrices", ejemplo_potencias_matrices),
        ("Matrices especiales", ejemplo_matrices_especiales),
        ("Transformaciones geométricas", ejemplo_transformaciones_geometricas),
        ("Análisis de sistemas", ejemplo_analisis_sistema),
        ("Operaciones con matrices grandes", ejemplo_operaciones_grandes),
        ("Análisis de precisión", ejemplo_precision_acumulada)
    ]
    
    try:
        for i, (titulo, funcion) in enumerate(ejemplos, 1):
            print(f"\\n🔹 Ejemplo {i}/{len(ejemplos)}: {titulo}")
            if confirmar_accion("¿Ejecutar este ejemplo?"):
                funcion()
            
            if i < len(ejemplos):
                input("\\n⏵ Presiona Enter para continuar...")
        
        mostrar_separador("¡EJEMPLOS AVANZADOS COMPLETADOS!")
        print("🎯 Has explorado capacidades avanzadas de la biblioteca:")
        print("   ✓ Operaciones complejas encadenadas")
        print("   ✓ Potencias y matrices especiales")
        print("   ✓ Aplicaciones geométricas")
        print("   ✓ Análisis numérico")
        print("   ✓ Manejo de matrices grandes")
        print("   ✓ Consideraciones de precisión")
        print("\\n🔗 Próximos pasos sugeridos:")
        print("   • Implementar algoritmos más avanzados")
        print("   • Explorar aplicaciones en machine learning")
        print("   • Desarrollar solvers para sistemas lineales")
        print("   • Optimizar para matrices muy grandes")
        
    except KeyboardInterrupt:
        print("\\n\\n👋 ¡Ejemplos interrumpidos por el usuario!")
    except Exception as e:
        print(f"\\n❌ Error durante los ejemplos: {e}")


if __name__ == "__main__":
    main()
