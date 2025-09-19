"""
Interfaz de Consola
==================

Interfaz de línea de comandos para el generador de matrices.
Proporciona un menú interactivo para todas las funcionalidades.

Autor: Nicolas
"""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.matriz import Matriz
from src.operaciones import *
from src.utilidades import *


class InterfazConsola:
    """
    Clase que maneja la interfaz de línea de comandos.
    """
    
    def __init__(self):
        """Inicializa la interfaz de consola."""
        self.matrices = {}  # Diccionario para almacenar matrices creadas
        self.contador_matrices = 0
    
    
    def iniciar(self):
        """Inicia la interfaz de consola."""
        limpiar_pantalla()
        self.mostrar_bienvenida()
        
        while True:
            try:
                self.mostrar_menu_principal()
                opcion = input("Selecciona una opción: ").strip()
                
                if opcion == "1":
                    self.crear_matriz()
                elif opcion == "2":
                    self.listar_matrices()
                elif opcion == "3":
                    self.operaciones_matrices()
                elif opcion == "4":
                    self.mostrar_matriz()
                elif opcion == "5":
                    self.eliminar_matriz()
                elif opcion == "6":
                    self.limpiar_todas_matrices()
                elif opcion == "0":
                    self.despedida()
                    break
                else:
                    print("❌ Opción no válida. Por favor selecciona una opción del menú.")
                    pausar()
            
            except KeyboardInterrupt:
                print("\\n\\n👋 ¡Hasta luego!")
                break
            except Exception as e:
                print(f"\\n❌ Error inesperado: {e}")
                pausar()
    
    
    def mostrar_bienvenida(self):
        """Muestra el mensaje de bienvenida."""
        mostrar_separador("GENERADOR DE MATRICES - CONSOLA", 60)
        print("¡Bienvenido al generador de matrices!")
        print("Aquí puedes crear, manipular y operar con matrices de forma fácil.")
        print()
    
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal de opciones."""
        print("\\n" + "="*50)
        print("MENÚ PRINCIPAL")
        print("="*50)
        print("1. Crear nueva matriz")
        print("2. Listar matrices existentes")
        print("3. Operaciones con matrices")
        print("4. Mostrar matriz específica")
        print("5. Eliminar matriz")
        print("6. Limpiar todas las matrices")
        print("0. Salir")
        print("="*50)
    
    
    def crear_matriz(self):
        """Crea una nueva matriz."""
        try:
            limpiar_pantalla()
            mostrar_separador("CREAR NUEVA MATRIZ")
            
            # Solicitar dimensiones
            filas = solicitar_entero("Número de filas", 1, 10)
            columnas = solicitar_entero("Número de columnas", 1, 10)
            
            # Crear matriz
            matriz = Matriz(filas, columnas)
            
            # Elegir método de llenado
            print("\\n¿Cómo deseas llenar la matriz?")
            print("1. Ingresar elementos manualmente")
            print("2. Llenar con números aleatorios")
            print("3. Crear matriz de ceros")
            print("4. Crear matriz de unos")
            
            metodo = solicitar_entero("Selecciona el método", 1, 4)
            
            if metodo == 1:
                print()
                matriz.llenar_interactivo()
            elif metodo == 2:
                min_val = solicitar_entero("Valor mínimo para números aleatorios", -100, 100)
                max_val = solicitar_entero("Valor máximo para números aleatorios", min_val, 100)
                matriz.llenar_aleatorio(min_val, max_val)
            elif metodo == 3:
                # Ya está llena de ceros por defecto
                pass
            elif metodo == 4:
                for i in range(matriz.filas):
                    for j in range(matriz.columnas):
                        matriz.datos[i][j] = 1
            
            # Guardar matriz
            self.contador_matrices += 1
            nombre = f"Matriz_{self.contador_matrices}"
            self.matrices[nombre] = matriz
            
            # Mostrar resultado
            print(f"\n✅ Matriz '{nombre}' creada exitosamente:")
            matriz.mostrar(nombre)
            
        except Exception as e:
            print(f"❌ Error al crear la matriz: {e}")
        
        pausar()
    
    
    def listar_matrices(self):
        """Lista todas las matrices existentes."""
        limpiar_pantalla()
        mostrar_separador("MATRICES EXISTENTES")
        
        if not self.matrices:
            print("📝 No hay matrices creadas aún.")
            print("Crea una nueva matriz desde el menú principal.")
        else:
            print(f"Total de matrices: {len(self.matrices)}\n")
            
            for nombre, matriz in self.matrices.items():
                print(f"🔹 {nombre} ({matriz.filas}x{matriz.columnas})")
                if matriz.filas <= 5 and matriz.columnas <= 5:  # Solo mostrar si es pequeña
                    matriz.mostrar()
                else:
                    print("   (Matriz muy grande para mostrar aquí)")
                print()
        
        pausar()
    
    
    def mostrar_matriz(self):
        """Muestra una matriz específica."""
        if not self.matrices:
            print("❌ No hay matrices disponibles.")
            pausar()
            return
        
        limpiar_pantalla()
        mostrar_separador("MOSTRAR MATRIZ")
        
        print("Matrices disponibles:")
        nombres = list(self.matrices.keys())
        mostrar_lista_numerada(nombres, "Matrices")
        
        try:
            indice = solicitar_entero("Selecciona la matriz a mostrar", 1, len(nombres))
            nombre = nombres[indice - 1]
            matriz = self.matrices[nombre]
            
            print()
            matriz.mostrar(nombre)
            print(f"Dimensiones: {matriz.filas}x{matriz.columnas}")
            print(f"Es cuadrada: {'Sí' if matriz.es_cuadrada() else 'No'}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
        
        pausar()
    
    
    def operaciones_matrices(self):
        """Menú de operaciones con matrices."""
        if len(self.matrices) < 1:
            print("❌ Necesitas al menos una matriz para realizar operaciones.")
            pausar()
            return
        
        limpiar_pantalla()
        mostrar_separador("OPERACIONES CON MATRICES")
        
        print("Operaciones disponibles:")
        print("1. Sumar matrices")
        print("2. Restar matrices")  
        print("3. Multiplicar matrices")
        print("4. Multiplicar por escalar")
        print("5. Transponer matriz")
        print("6. Copiar matriz")
        print("0. Volver al menú principal")
        
        try:
            opcion = solicitar_entero("Selecciona la operación", 0, 6)
            
            if opcion == 0:
                return
            elif opcion in [1, 2, 3]:
                self.operacion_dos_matrices(opcion)
            elif opcion == 4:
                self.multiplicar_por_escalar()
            elif opcion == 5:
                self.transponer_matriz()
            elif opcion == 6:
                self.copiar_matriz()
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        pausar()
    
    
    def operacion_dos_matrices(self, tipo_operacion):
        """Realiza operaciones que requieren dos matrices."""
        if len(self.matrices) < 2:
            print("❌ Necesitas al menos dos matrices para esta operación.")
            pausar()
            return
        
        limpiar_pantalla()
        
        # Mostrar qué operación se va a realizar
        operaciones = {1: "SUMA", 2: "RESTA", 3: "MULTIPLICACIÓN"}
        mostrar_separador(f"{operaciones[tipo_operacion]} DE MATRICES")
        
        nombres = list(self.matrices.keys())
        
        print("\nSelecciona la primera matriz:")
        mostrar_lista_numerada(nombres, "Matrices disponibles")
        indice1 = solicitar_entero("Primera matriz", 1, len(nombres))
        
        print("\nSelecciona la segunda matriz:")
        mostrar_lista_numerada(nombres, "Matrices disponibles")
        indice2 = solicitar_entero("Segunda matriz", 1, len(nombres))
        
        matriz1 = self.matrices[nombres[indice1 - 1]]
        matriz2 = self.matrices[nombres[indice2 - 1]]
        
        try:
            if tipo_operacion == 1:  # Suma
                resultado = sumar_matrices(matriz1, matriz2)
                operacion_nombre = "Suma"
            elif tipo_operacion == 2:  # Resta
                resultado = restar_matrices(matriz1, matriz2)
                operacion_nombre = "Resta"
            elif tipo_operacion == 3:  # Multiplicación
                resultado = multiplicar_matrices(matriz1, matriz2)
                operacion_nombre = "Multiplicación"
            
            # Guardar resultado
            self.contador_matrices += 1
            nombre_resultado = f"Resultado_{self.contador_matrices}"
            self.matrices[nombre_resultado] = resultado
            
            print(f"\n✅ {operacion_nombre} realizada exitosamente:")
            resultado.mostrar(f"{operacion_nombre} - {nombre_resultado}")
            
        except ValueError as e:
            print(f"❌ Error en la operación: {e}")
    
    
    def multiplicar_por_escalar(self):
        """Multiplica una matriz por un escalar."""
        limpiar_pantalla()
        mostrar_separador("MULTIPLICACIÓN POR ESCALAR")
        
        nombres = list(self.matrices.keys())
        
        print("\nSelecciona la matriz:")
        mostrar_lista_numerada(nombres, "Matrices disponibles")
        indice = solicitar_entero("Matriz", 1, len(nombres))
        
        matriz = self.matrices[nombres[indice - 1]]
        escalar = solicitar_numero("Ingresa el valor escalar")
        
        try:
            resultado = multiplicar_por_escalar(matriz, escalar)
            
            self.contador_matrices += 1
            nombre_resultado = f"Escalar_{self.contador_matrices}"
            self.matrices[nombre_resultado] = resultado
            
            print(f"\n✅ Multiplicación por escalar realizada:")
            resultado.mostrar(f"Multiplicación por {escalar} - {nombre_resultado}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    
    def transponer_matriz(self):
        """Calcula la transpuesta de una matriz."""
        limpiar_pantalla()
        mostrar_separador("TRANSPONER MATRIZ")
        
        nombres = list(self.matrices.keys())
        
        print("\nSelecciona la matriz a transponer:")
        mostrar_lista_numerada(nombres, "Matrices disponibles")
        indice = solicitar_entero("Matriz", 1, len(nombres))
        
        matriz = self.matrices[nombres[indice - 1]]
        
        try:
            resultado = matriz.transponer()
            
            self.contador_matrices += 1
            nombre_resultado = f"Transpuesta_{self.contador_matrices}"
            self.matrices[nombre_resultado] = resultado
            
            print(f"\n✅ Matriz transpuesta creada:")
            resultado.mostrar(f"Transpuesta - {nombre_resultado}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    
    def copiar_matriz(self):
        """Crea una copia de una matriz."""
        limpiar_pantalla()
        mostrar_separador("COPIAR MATRIZ")
        
        nombres = list(self.matrices.keys())
        
        print("\nSelecciona la matriz a copiar:")
        mostrar_lista_numerada(nombres, "Matrices disponibles")
        indice = solicitar_entero("Matriz", 1, len(nombres))
        
        matriz = self.matrices[nombres[indice - 1]]
        
        try:
            resultado = matriz.copiar()
            
            self.contador_matrices += 1
            nombre_resultado = f"Copia_{self.contador_matrices}"
            self.matrices[nombre_resultado] = resultado
            
            print(f"\n✅ Matriz copiada:")
            resultado.mostrar(f"Copia - {nombre_resultado}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    
    def eliminar_matriz(self):
        """Elimina una matriz específica."""
        if not self.matrices:
            print("❌ No hay matrices para eliminar.")
            pausar()
            return
        
        limpiar_pantalla()
        mostrar_separador("ELIMINAR MATRIZ")
        
        nombres = list(self.matrices.keys())
        print("Selecciona la matriz a eliminar:")
        mostrar_lista_numerada(nombres, "Matrices disponibles")
        
        try:
            indice = solicitar_entero("Matriz a eliminar", 1, len(nombres))
            nombre = nombres[indice - 1]
            
            if confirmar_accion(f"¿Seguro que deseas eliminar '{nombre}'?"):
                del self.matrices[nombre]
                print(f"✅ Matriz '{nombre}' eliminada exitosamente.")
            else:
                print("❌ Operación cancelada.")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        pausar()
    
    
    def limpiar_todas_matrices(self):
        """Elimina todas las matrices."""
        if not self.matrices:
            print("❌ No hay matrices para limpiar.")
            pausar()
            return
        
        if confirmar_accion(f"¿Seguro que deseas eliminar todas las {len(self.matrices)} matrices?"):
            self.matrices.clear()
            self.contador_matrices = 0
            print("✅ Todas las matrices han sido eliminadas.")
        else:
            print("❌ Operación cancelada.")
        
        pausar()
    
    
    def despedida(self):
        """Muestra el mensaje de despedida."""
        limpiar_pantalla()
        mostrar_separador("¡HASTA LUEGO!", 60)
        print("Gracias por usar el Generador de Matrices.")
        print("¡Esperamos verte pronto! 🚀")
        print()
