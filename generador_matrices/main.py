#!/usr/bin/env python3
"""
Generador de Matrices - Programa Principal
==========================================

Punto de entrada principal del programa.
Permite al usuario elegir entre interfaz de consola o gráfica.

Autor: Nicolas
Versión: 1.0.0
"""

import sys
import os

# Agregar el directorio actual al path para importaciones
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from interfaces.consola import InterfazConsola
from interfaces.grafica import InterfazGrafica


def mostrar_menu_principal():
    """Muestra el menú principal de selección de interfaz."""
    print("="*50)
    print("    GENERADOR DE MATRICES")
    print("="*50)
    print()
    print("Selecciona el tipo de interfaz:")
    print("1. Interfaz de Consola (CLI)")
    print("2. Interfaz Gráfica (GUI)")
    print("3. Salir")
    print()


def main():
    """Función principal del programa."""
    try:
        while True:
            mostrar_menu_principal()
            
            try:
                opcion = input("Ingresa tu opción (1-3): ").strip()
                
                if opcion == "1":
                    print("\n🚀 Iniciando interfaz de consola...\n")
                    interfaz_consola = InterfazConsola()
                    interfaz_consola.iniciar()
                    
                elif opcion == "2":
                    print("\n🖥️ Iniciando interfaz gráfica...\n")
                    interfaz_grafica = InterfazGrafica()
                    interfaz_grafica.iniciar()
                    
                elif opcion == "3":
                    print("\n👋 ¡Gracias por usar el Generador de Matrices!")
                    print("¡Hasta la vista! 🚀\n")
                    break
                    
                else:
                    print("\n❌ Opción no válida. Por favor selecciona 1, 2 o 3.")
                    input("Presiona Enter para continuar...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego!")
                break
                
            except Exception as e:
                print(f"\n❌ Error inesperado: {e}")
                input("Presiona Enter para continuar...")
                
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
    
    except Exception as e:
        print(f"\n❌ Error crítico: {e}")
        print("El programa se cerrará.")


if __name__ == "__main__":
    main()
