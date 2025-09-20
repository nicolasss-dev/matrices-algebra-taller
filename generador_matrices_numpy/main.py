#!/usr/bin/env python3
"""
Generador de Matrices con NumPy - Programa Principal
===================================================

Programa simple para operaciones básicas con matrices usando NumPy.
Ofrece interfaces de consola y gráfica.

Autor: Nicolas
Versión: 2.0.0 (NumPy Edition)
"""

import sys
import os
import numpy as np

# Agregar el directorio actual al path para importaciones
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Verificar dependencias críticas
try:
    import numpy as np
    NUMPY_VERSION = np.__version__
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    print("❌ ERROR CRÍTICO: NumPy no está instalado.")
    print("Este proyecto requiere NumPy para funcionar.")
    print("\n📦 Para instalar NumPy:")
    print("   pip install numpy")
    sys.exit(1)

# Importar interfaces cuando NumPy esté disponible
if HAS_NUMPY:
    try:
        from interfaces.consola_numpy import InterfazConsolaNP
        from interfaces.grafica_numpy import InterfazGraficaNP
    except ImportError as e:
        print(f"⚠️ Error al importar interfaces: {e}")
        print("Usando modo de compatibilidad...")
        InterfazConsolaNP = None
        InterfazGraficaNP = None


def mostrar_banner():
    """Muestra el banner de inicio del programa."""
    print("🔢" + "="*50 + "🔢")
    print("    GENERADOR DE MATRICES CON NUMPY")
    print("🔢" + "="*50 + "🔢")
    print()
    print(f"🧮 NumPy v{NUMPY_VERSION} - Operaciones con matrices")
    print()


def mostrar_menu_principal():
    """Muestra el menú principal de selección de interfaz."""
    print("🎯 Selecciona el tipo de interfaz:")
    print("1. 💻 Interfaz de Consola (CLI)")
    print("2. 🖥️ Interfaz Gráfica (GUI)")
    print("3. 🚪 Salir")
    print()




def main():
    """Función principal del programa."""
    try:
        mostrar_banner()
        
        while True:
            mostrar_menu_principal()
            
            try:
                opcion = input("🎯 Ingresa tu opción (1-3): ").strip()
                
                if opcion == "1":
                    print("\n💻 Iniciando interfaz de consola...\n")
                    if InterfazConsolaNP:
                        interfaz_consola = InterfazConsolaNP()
                        interfaz_consola.iniciar()
                    else:
                        print("❌ Interfaz de consola no disponible")
                        
                elif opcion == "2":
                    print("\n🖥️ Iniciando interfaz gráfica...\n")
                    if InterfazGraficaNP:
                        interfaz_grafica = InterfazGraficaNP()
                        interfaz_grafica.iniciar()
                    else:
                        print("❌ Interfaz gráfica no disponible")
                        
                elif opcion == "3":
                    print("\n👋 ¡Gracias por usar el Generador de Matrices!")
                    print("✨ ¡Hasta luego!\n")
                    break
                    
                else:
                    print("\n❌ Opción no válida. Por favor selecciona 1-3.")
                    input("⏵ Presiona Enter para continuar...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego!")
                break
                
            except Exception as e:
                print(f"\n❌ Error inesperado: {e}")
                input("⏵ Presiona Enter para continuar...")
                
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
    
    except Exception as e:
        print(f"\n❌ Error crítico: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
