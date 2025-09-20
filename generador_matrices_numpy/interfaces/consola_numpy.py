"""
Interfaz de Consola Avanzada para NumPy
======================================

Interfaz de línea de comandos optimizada para operaciones con matrices
usando NumPy con capacidades científicas avanzadas.

Autor: Nicolas
Versión: 2.0.0 (NumPy Edition)
"""

import sys
import os
import numpy as np
from typing import Dict, List, Optional, Tuple

# Importar la clase principal
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.matriz_numpy import MatrizNumPy


class InterfazConsolaNP:
    """Interfaz de consola avanzada para operaciones con matrices usando NumPy."""
    
    def __init__(self):
        """Inicializa la interfaz de consola."""
        self.matrices: Dict[str, MatrizNumPy] = {}
        self.historial_operaciones: List[str] = []
        self.precision_salida = 4
        
    def iniciar(self):
        """Inicia el bucle principal de la interfaz de consola."""
        self.mostrar_bienvenida()
        
        while True:
            try:
                self.mostrar_menu_principal()
                opcion = input("\n🎯 Selecciona una opción: ").strip()
                
                if opcion == "1":
                    self.menu_crear_matrices()
                elif opcion == "2":
                    self.menu_operaciones_basicas()
                elif opcion == "3":
                    self.menu_algebra_lineal()
                elif opcion == "4":
                    self.menu_gestionar_matrices()
                elif opcion == "0":
                    print("\n👋 ¡Gracias por usar el generador de matrices!")
                    break
                else:
                    print("❌ Opción no válida. Intenta nuevamente.")
                    
                input("\n⏵ Presiona Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                input("⏵ Presiona Enter para continuar...")
    
    def mostrar_bienvenida(self):
        """Muestra el mensaje de bienvenida."""
        print("🔬" + "="*60 + "🔬")
        print("    INTERFAZ DE CONSOLA NUMPY - MODO CIENTÍFICO")
        print("🔬" + "="*60 + "🔬")
        print()
        print("💡 Interfaz avanzada con capacidades profesionales de álgebra lineal")
        print(f"🧮 NumPy v{np.__version__} - Rendimiento optimizado")
        print("📊 Análisis, descomposiciones y visualizaciones disponibles")
        print()
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal."""
        print("\n🎯 MENÚ PRINCIPAL")
        print("="*25)
        print("1. 🏢️ Crear Matrices")
        print("2. ➕ Operaciones Básicas")
        print("3. 🧪 Álgebra Lineal")
        print("4. 📁 Gestionar Matrices")
        print("0. 🚪 Salir")
    
    def menu_crear_matrices(self):
        """Menú para crear matrices."""
        while True:
            print("\n🏗️ CREAR Y GENERAR MATRICES")
            print("="*35)
            print("1. 📝 Matriz Manual")
            print("2. 🎲 Matriz Aleatoria")
            print("3. 🔢 Matriz de Ceros")
            print("4. 1️⃣ Matriz de Unos")
            print("5. 👁️ Matriz Identidad")
            print("6. 📐 Matriz Diagonal")
            print("7. 🌊 Matrices Especiales")
            print("8. 📊 Desde Datos CSV")
            print("0. ⬅️ Volver")
            
            opcion = input("\n🎯 Opción: ").strip()
            
            if opcion == "1":
                self.crear_matriz_manual()
            elif opcion == "2":
                self.crear_matriz_aleatoria()
            elif opcion == "3":
                self.crear_matriz_ceros()
            elif opcion == "4":
                self.crear_matriz_unos()
            elif opcion == "5":
                self.crear_matriz_identidad()
            elif opcion == "6":
                self.crear_matriz_diagonal()
            elif opcion == "7":
                self.menu_matrices_especiales()
            elif opcion == "8":
                self.cargar_matriz_csv()
            elif opcion == "0":
                break
    
    def crear_matriz_manual(self):
        """Crear matriz ingresando valores manualmente."""
        try:
            nombre = input("🏷️ Nombre de la matriz: ").strip()
            if not nombre:
                print("❌ El nombre no puede estar vacío.")
                return
                
            filas = int(input("📏 Número de filas: "))
            columnas = int(input("📐 Número de columnas: "))
            
            print(f"\n📝 Ingresa los valores para matriz {filas}×{columnas}:")
            datos = []
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    while True:
                        try:
                            valor = float(input(f"  Elemento [{i+1},{j+1}]: "))
                            fila.append(valor)
                            break
                        except ValueError:
                            print("❌ Por favor, ingresa un número válido.")
                datos.append(fila)
            
            matriz = MatrizNumPy(datos)
            self.matrices[nombre] = matriz
            print(f"✅ Matriz '{nombre}' creada exitosamente!")
            matriz.mostrar(f"Matriz {nombre}")
            
            self.historial_operaciones.append(f"Creada matriz manual '{nombre}' ({filas}×{columnas})")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def crear_matriz_aleatoria(self):
        """Crear matriz con valores aleatorios."""
        try:
            nombre = input("🏷️ Nombre de la matriz: ").strip()
            if not nombre:
                print("❌ El nombre no puede estar vacío.")
                return
                
            filas = int(input("📏 Número de filas: "))
            columnas = int(input("📐 Número de columnas: "))
            min_val = float(input("📉 Valor mínimo (default -10): ") or "-10")
            max_val = float(input("📈 Valor máximo (default 10): ") or "10")
            
            seed_input = input("🎲 Semilla aleatoria (Enter para aleatorio): ").strip()
            seed = int(seed_input) if seed_input else None
            
            matriz = MatrizNumPy.crear_aleatoria(filas, columnas, min_val, max_val, seed=seed)
            self.matrices[nombre] = matriz
            
            print(f"✅ Matriz aleatoria '{nombre}' creada exitosamente!")
            matriz.mostrar(f"Matriz {nombre}")
            
            self.historial_operaciones.append(f"Creada matriz aleatoria '{nombre}' ({filas}×{columnas}, rango [{min_val}, {max_val}])")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def crear_matriz_ceros(self):
        """Crear matriz de ceros."""
        try:
            nombre = input("🏷️ Nombre de la matriz: ").strip()
            if not nombre:
                print("❌ El nombre no puede estar vacío.")
                return
                
            filas = int(input("📏 Número de filas: "))
            columnas = int(input("📐 Número de columnas: "))
            
            matriz = MatrizNumPy.crear_ceros(filas, columnas)
            self.matrices[nombre] = matriz
            
            print(f"✅ Matriz de ceros '{nombre}' creada exitosamente!")
            matriz.mostrar(f"Matriz {nombre}")
            
            self.historial_operaciones.append(f"Creada matriz de ceros '{nombre}' ({filas}×{columnas})")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def crear_matriz_unos(self):
        """Crear matriz de unos."""
        try:
            nombre = input("🏷️ Nombre de la matriz: ").strip()
            if not nombre:
                print("❌ El nombre no puede estar vacío.")
                return
                
            filas = int(input("📏 Número de filas: "))
            columnas = int(input("📐 Número de columnas: "))
            
            matriz = MatrizNumPy.crear_unos(filas, columnas)
            self.matrices[nombre] = matriz
            
            print(f"✅ Matriz de unos '{nombre}' creada exitosamente!")
            matriz.mostrar(f"Matriz {nombre}")
            
            self.historial_operaciones.append(f"Creada matriz de unos '{nombre}' ({filas}×{columnas})")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def crear_matriz_identidad(self):
        """Crear matriz identidad."""
        try:
            nombre = input("🏷️ Nombre de la matriz: ").strip()
            if not nombre:
                print("❌ El nombre no puede estar vacío.")
                return
                
            tamaño = int(input("📏 Tamaño (n×n): "))
            
            matriz = MatrizNumPy.crear_identidad(tamaño)
            self.matrices[nombre] = matriz
            
            print(f"✅ Matriz identidad '{nombre}' creada exitosamente!")
            matriz.mostrar(f"Matriz {nombre}")
            
            self.historial_operaciones.append(f"Creada matriz identidad '{nombre}' ({tamaño}×{tamaño})")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def crear_matriz_diagonal(self):
        """Crear matriz diagonal."""
        try:
            nombre = input("🏷️ Nombre de la matriz: ").strip()
            if not nombre:
                print("❌ El nombre no puede estar vacío.")
                return
            
            diagonal_str = input("📐 Valores diagonales (separados por comas): ").strip()
            diagonal = [float(x.strip()) for x in diagonal_str.split(',')]
            
            matriz = MatrizNumPy.crear_diagonal(diagonal)
            self.matrices[nombre] = matriz
            
            print(f"✅ Matriz diagonal '{nombre}' creada exitosamente!")
            matriz.mostrar(f"Matriz {nombre}")
            
            self.historial_operaciones.append(f"Creada matriz diagonal '{nombre}' con valores {diagonal}")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def menu_matrices_especiales(self):
        """Menú para matrices especiales."""
        while True:
            print("\n🌊 MATRICES ESPECIALES")
            print("="*25)
            print("1. 🌀 Matriz de Hilbert")
            print("2. 🎯 Matriz de Vandermonde")
            print("3. 📈 Matriz Toeplitz")
            print("4. 🔄 Matriz Circulante")
            print("0. ⬅️ Volver")
            
            opcion = input("\n🎯 Opción: ").strip()
            
            if opcion == "1":
                self.crear_matriz_hilbert()
            elif opcion == "2":
                self.crear_matriz_vandermonde()
            elif opcion == "0":
                break
    
    def crear_matriz_hilbert(self):
        """Crear matriz de Hilbert."""
        try:
            nombre = input("🏷️ Nombre de la matriz: ").strip()
            n = int(input("📏 Tamaño n×n: "))
            
            # Crear matriz de Hilbert H[i,j] = 1/(i+j+1)
            hilbert = np.array([[1/(i+j+1) for j in range(n)] for i in range(n)])
            matriz = MatrizNumPy(hilbert)
            
            self.matrices[nombre] = matriz
            print(f"✅ Matriz de Hilbert '{nombre}' creada exitosamente!")
            matriz.mostrar(f"Matriz de Hilbert {nombre}")
            
            # Información adicional
            print(f"💡 Las matrices de Hilbert son mal condicionadas.")
            print(f"   Número de condición: {matriz.condicion():.2e}")
            
            self.historial_operaciones.append(f"Creada matriz de Hilbert '{nombre}' ({n}×{n})")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def crear_matriz_vandermonde(self):
        """Crear matriz de Vandermonde."""
        try:
            nombre = input("🏷️ Nombre de la matriz: ").strip()
            vector_str = input("📐 Vector base (separado por comas): ").strip()
            vector = [float(x.strip()) for x in vector_str.split(',')]
            grado = int(input("📈 Grado máximo: "))
            
            # Crear matriz de Vandermonde
            vander = np.vander(vector, grado + 1)
            matriz = MatrizNumPy(vander)
            
            self.matrices[nombre] = matriz
            print(f"✅ Matriz de Vandermonde '{nombre}' creada exitosamente!")
            matriz.mostrar(f"Matriz de Vandermonde {nombre}")
            
            self.historial_operaciones.append(f"Creada matriz de Vandermonde '{nombre}' con vector {vector}")
            
        except ValueError as e:
            print(f"❌ Error en los datos: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def cargar_matriz_csv(self):
        """Cargar matriz desde archivo CSV."""
        try:
            nombre = input("🏷️ Nombre de la matriz: ").strip()
            archivo = input("📄 Ruta del archivo CSV: ").strip()
            
            if not os.path.exists(archivo):
                print("❌ Archivo no encontrado.")
                return
            
            # Cargar datos del CSV
            datos = np.loadtxt(archivo, delimiter=',')
            matriz = MatrizNumPy(datos)
            
            self.matrices[nombre] = matriz
            print(f"✅ Matriz '{nombre}' cargada exitosamente desde {archivo}!")
            matriz.mostrar(f"Matriz {nombre}")
            
            self.historial_operaciones.append(f"Cargada matriz '{nombre}' desde CSV: {archivo}")
            
        except Exception as e:
            print(f"❌ Error al cargar archivo: {e}")
    
    def menu_operaciones_basicas(self):
        """Menú para operaciones básicas."""
        if not self.matrices:
            print("❌ No hay matrices disponibles. Crea matrices primero.")
            return
            
        while True:
            print("\n➕ OPERACIONES BÁSICAS")
            print("="*25)
            print("1. ➕ Suma")
            print("2. ➖ Resta")
            print("3. ✖️ Multiplicación")
            print("4. 🔄 Transposición")
            print("5. 📊 Escalado")
            print("6. 🧮 Potencia")
            print("0. ⬅️ Volver")
            
            opcion = input("\n🎯 Opción: ").strip()
            
            if opcion == "1":
                self.operacion_suma()
            elif opcion == "2":
                self.operacion_resta()
            elif opcion == "3":
                self.operacion_multiplicacion()
            elif opcion == "4":
                self.operacion_transposicion()
            elif opcion == "5":
                self.operacion_escalado()
            elif opcion == "6":
                self.operacion_potencia()
            elif opcion == "0":
                break
    
    def seleccionar_matriz(self, mensaje="Selecciona una matriz") -> Optional[str]:
        """Permite seleccionar una matriz de las disponibles."""
        if not self.matrices:
            print("❌ No hay matrices disponibles.")
            return None
        
        print(f"\n📋 {mensaje}:")
        nombres = list(self.matrices.keys())
        for i, nombre in enumerate(nombres, 1):
            matriz = self.matrices[nombre]
            print(f"{i}. {nombre} ({matriz.shape[0]}×{matriz.shape[1]})")
        
        try:
            seleccion = int(input("🎯 Número de matriz: ")) - 1
            if 0 <= seleccion < len(nombres):
                return nombres[seleccion]
            else:
                print("❌ Selección no válida.")
                return None
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
            return None
    
    def operacion_suma(self):
        """Realizar suma de matrices."""
        try:
            print("\n➕ SUMA DE MATRICES")
            matriz_a = self.seleccionar_matriz("Primera matriz")
            if not matriz_a:
                return
            
            matriz_b = self.seleccionar_matriz("Segunda matriz")
            if not matriz_b:
                return
            
            nombre_resultado = input("🏷️ Nombre para el resultado: ").strip()
            if not nombre_resultado:
                nombre_resultado = f"{matriz_a}+{matriz_b}"
            
            resultado = self.matrices[matriz_a] + self.matrices[matriz_b]
            self.matrices[nombre_resultado] = resultado
            
            print(f"✅ Suma completada exitosamente!")
            resultado.mostrar(f"Resultado: {nombre_resultado} = {matriz_a} + {matriz_b}")
            
            self.historial_operaciones.append(f"Suma: {nombre_resultado} = {matriz_a} + {matriz_b}")
            
        except Exception as e:
            print(f"❌ Error en suma: {e}")
    
    def operacion_resta(self):
        """Realizar resta de matrices."""
        try:
            print("\n➖ RESTA DE MATRICES")
            matriz_a = self.seleccionar_matriz("Primera matriz")
            if not matriz_a:
                return
            
            matriz_b = self.seleccionar_matriz("Segunda matriz")
            if not matriz_b:
                return
            
            nombre_resultado = input("🏷️ Nombre para el resultado: ").strip()
            if not nombre_resultado:
                nombre_resultado = f"{matriz_a}-{matriz_b}"
            
            resultado = self.matrices[matriz_a] - self.matrices[matriz_b]
            self.matrices[nombre_resultado] = resultado
            
            print(f"✅ Resta completada exitosamente!")
            resultado.mostrar(f"Resultado: {nombre_resultado} = {matriz_a} - {matriz_b}")
            
            self.historial_operaciones.append(f"Resta: {nombre_resultado} = {matriz_a} - {matriz_b}")
            
        except Exception as e:
            print(f"❌ Error en resta: {e}")
    
    def operacion_multiplicacion(self):
        """Realizar multiplicación de matrices."""
        try:
            print("\n✖️ MULTIPLICACIÓN DE MATRICES")
            matriz_a = self.seleccionar_matriz("Primera matriz")
            if not matriz_a:
                return
            
            matriz_b = self.seleccionar_matriz("Segunda matriz")
            if not matriz_b:
                return
            
            nombre_resultado = input("🏷️ Nombre para el resultado: ").strip()
            if not nombre_resultado:
                nombre_resultado = f"{matriz_a}*{matriz_b}"
            
            resultado = self.matrices[matriz_a] @ self.matrices[matriz_b]
            self.matrices[nombre_resultado] = resultado
            
            print(f"✅ Multiplicación completada exitosamente!")
            resultado.mostrar(f"Resultado: {nombre_resultado} = {matriz_a} × {matriz_b}")
            
            self.historial_operaciones.append(f"Multiplicación: {nombre_resultado} = {matriz_a} × {matriz_b}")
            
        except Exception as e:
            print(f"❌ Error en multiplicación: {e}")
    
    def operacion_transposicion(self):
        """Realizar transposición de matriz."""
        try:
            print("\n🔄 TRANSPOSICIÓN DE MATRIZ")
            matriz_nombre = self.seleccionar_matriz("Matriz a transponer")
            if not matriz_nombre:
                return
            
            nombre_resultado = input("🏷️ Nombre para el resultado: ").strip()
            if not nombre_resultado:
                nombre_resultado = f"{matriz_nombre}_T"
            
            resultado = self.matrices[matriz_nombre].transponer()
            self.matrices[nombre_resultado] = resultado
            
            print(f"✅ Transposición completada exitosamente!")
            resultado.mostrar(f"Resultado: {nombre_resultado} = {matriz_nombre}ᵀ")
            
            self.historial_operaciones.append(f"Transposición: {nombre_resultado} = {matriz_nombre}ᵀ")
            
        except Exception as e:
            print(f"❌ Error en transposición: {e}")
    
    def operacion_escalado(self):
        """Realizar escalado de matriz."""
        try:
            print("\n📊 ESCALADO DE MATRIZ")
            matriz_nombre = self.seleccionar_matriz("Matriz a escalar")
            if not matriz_nombre:
                return
            
            escalar = float(input("🔢 Factor de escalado: "))
            
            nombre_resultado = input("🏷️ Nombre para el resultado: ").strip()
            if not nombre_resultado:
                nombre_resultado = f"{matriz_nombre}*{escalar}"
            
            resultado = self.matrices[matriz_nombre] * escalar
            self.matrices[nombre_resultado] = resultado
            
            print(f"✅ Escalado completado exitosamente!")
            resultado.mostrar(f"Resultado: {nombre_resultado} = {escalar} × {matriz_nombre}")
            
            self.historial_operaciones.append(f"Escalado: {nombre_resultado} = {escalar} × {matriz_nombre}")
            
        except ValueError as e:
            print(f"❌ Error en el valor del escalar: {e}")
        except Exception as e:
            print(f"❌ Error en escalado: {e}")
    
    def operacion_potencia(self):
        """Realizar potencia de matriz."""
        try:
            print("\n🧮 POTENCIA DE MATRIZ")
            matriz_nombre = self.seleccionar_matriz("Matriz base (debe ser cuadrada)")
            if not matriz_nombre:
                return
            
            matriz = self.matrices[matriz_nombre]
            if not matriz.es_cuadrada():
                print("❌ La matriz debe ser cuadrada para calcular potencias.")
                return
            
            exponente = int(input("🔢 Exponente: "))
            
            nombre_resultado = input("🏷️ Nombre para el resultado: ").strip()
            if not nombre_resultado:
                nombre_resultado = f"{matriz_nombre}^{exponente}"
            
            resultado = matriz.potencia(exponente)
            self.matrices[nombre_resultado] = resultado
            
            print(f"✅ Potencia completada exitosamente!")
            resultado.mostrar(f"Resultado: {nombre_resultado} = {matriz_nombre}^{exponente}")
            
            self.historial_operaciones.append(f"Potencia: {nombre_resultado} = {matriz_nombre}^{exponente}")
            
        except ValueError as e:
            print(f"❌ Error en el exponente: {e}")
        except Exception as e:
            print(f"❌ Error en potencia: {e}")
    
    def menu_algebra_lineal(self):
        """Menú para álgebra lineal avanzada."""
        if not self.matrices:
            print("❌ No hay matrices disponibles. Crea matrices primero.")
            return
            
        while True:
            print("\n🧪 ÁLGEBRA LINEAL AVANZADA")
            print("="*30)
            print("1. 🔢 Determinante")
            print("2. ↩️ Inversa")
            print("3. 🌟 Eigenvalores y Eigenvectores")
            print("4. 📐 Descomposición SVD")
            print("5. 🔺 Descomposición QR")
            print("6. 💎 Descomposición de Cholesky")
            print("7. 🧮 Resolver Sistema Lineal")
            print("8. 📏 Normas")
            print("0. ⬅️ Volver")
            
            opcion = input("\n🎯 Opción: ").strip()
            
            if opcion == "1":
                self.calcular_determinante()
            elif opcion == "2":
                self.calcular_inversa()
            elif opcion == "3":
                self.calcular_eigen()
            elif opcion == "4":
                self.descomposicion_svd()
            elif opcion == "5":
                self.descomposicion_qr()
            elif opcion == "6":
                self.descomposicion_cholesky()
            elif opcion == "7":
                self.resolver_sistema_lineal()
            elif opcion == "8":
                self.calcular_normas()
            elif opcion == "0":
                break
    
    def calcular_determinante(self):
        """Calcular determinante de una matriz."""
        try:
            print("\n🔢 DETERMINANTE")
            matriz_nombre = self.seleccionar_matriz("Matriz (debe ser cuadrada)")
            if not matriz_nombre:
                return
            
            matriz = self.matrices[matriz_nombre]
            if not matriz.es_cuadrada():
                print("❌ La matriz debe ser cuadrada para calcular el determinante.")
                return
            
            det = matriz.determinante()
            print(f"✅ Determinante de '{matriz_nombre}': {det:.{self.precision_salida}f}")
            
            # Interpretación
            if abs(det) < 1e-10:
                print("💡 La matriz es singular (no invertible)")
            elif abs(det) > 1:
                print("💡 La matriz expande volúmenes")
            else:
                print("💡 La matriz contrae volúmenes")
            
            self.historial_operaciones.append(f"Calculado determinante de '{matriz_nombre}': {det:.{self.precision_salida}f}")
            
        except Exception as e:
            print(f"❌ Error al calcular determinante: {e}")
    
    def calcular_inversa(self):
        """Calcular inversa de una matriz."""
        try:
            print("\n↩️ MATRIZ INVERSA")
            matriz_nombre = self.seleccionar_matriz("Matriz (debe ser cuadrada y no singular)")
            if not matriz_nombre:
                return
            
            matriz = self.matrices[matriz_nombre]
            if not matriz.es_cuadrada():
                print("❌ La matriz debe ser cuadrada para calcular la inversa.")
                return
            
            nombre_resultado = input(f"🏷️ Nombre para la inversa (default: {matriz_nombre}_inv): ").strip()
            if not nombre_resultado:
                nombre_resultado = f"{matriz_nombre}_inv"
            
            inversa = matriz.inversa()
            self.matrices[nombre_resultado] = inversa
            
            print(f"✅ Inversa calculada exitosamente!")
            inversa.mostrar(f"Inversa: {nombre_resultado} = {matriz_nombre}⁻¹")
            
            # Verificación
            producto = matriz @ inversa
            error = np.max(np.abs(producto.datos - np.eye(matriz.shape[0])))
            print(f"🔍 Error de verificación (A × A⁻¹ - I): {error:.2e}")
            
            self.historial_operaciones.append(f"Calculada inversa: {nombre_resultado} = {matriz_nombre}⁻¹")
            
        except Exception as e:
            print(f"❌ Error al calcular inversa: {e}")
    
    def calcular_eigen(self):
        """Calcular eigenvalores y eigenvectores."""
        try:
            print("\n🌟 EIGENVALORES Y EIGENVECTORES")
            matriz_nombre = self.seleccionar_matriz("Matriz (debe ser cuadrada)")
            if not matriz_nombre:
                return
            
            matriz = self.matrices[matriz_nombre]
            if not matriz.es_cuadrada():
                print("❌ La matriz debe ser cuadrada para calcular eigenvalores.")
                return
            
            print("🔍 Calculando eigenvalores y eigenvectores...")
            eigenvals, eigenvecs = matriz.eigen()
            
            print(f"\n✅ Eigenvalores de '{matriz_nombre}':")
            for i, val in enumerate(eigenvals):
                if np.isreal(val):
                    print(f"  λ_{i+1} = {val.real:.{self.precision_salida}f}")
                else:
                    print(f"  λ_{i+1} = {val.real:.{self.precision_salida}f} + {val.imag:.{self.precision_salida}f}i")
            
            # Guardar eigenvectores como matrices separadas si se desea
            guardar = input("\n💾 ¿Guardar eigenvectores como matriz? (s/n): ").strip().lower()
            if guardar == 's':
                nombre_eigenvecs = input(f"🏷️ Nombre para eigenvectores (default: {matriz_nombre}_eigenvecs): ").strip()
                if not nombre_eigenvecs:
                    nombre_eigenvecs = f"{matriz_nombre}_eigenvecs"
                self.matrices[nombre_eigenvecs] = MatrizNumPy(eigenvecs)
                print(f"✅ Eigenvectores guardados como '{nombre_eigenvecs}'")
            
            self.historial_operaciones.append(f"Calculados eigenvalores de '{matriz_nombre}'")
            
        except Exception as e:
            print(f"❌ Error al calcular eigenvalores: {e}")
    
    def descomposicion_svd(self):
        """Descomposición en valores singulares."""
        try:
            print("\n📐 DESCOMPOSICIÓN SVD")
            matriz_nombre = self.seleccionar_matriz("Matriz para descomponer")
            if not matriz_nombre:
                return
            
            matriz = self.matrices[matriz_nombre]
            
            print("🔍 Calculando descomposición SVD...")
            U, s, Vt = matriz.svd()
            
            print(f"\n✅ SVD de '{matriz_nombre}' completada:")
            print(f"  - U: {U.shape[0]}×{U.shape[1]}")
            print(f"  - σ (valores singulares): {len(s)} valores")
            print(f"  - V^T: {Vt.shape[0]}×{Vt.shape[1]}")
            
            print(f"\n📊 Valores singulares:")
            for i, val in enumerate(s):
                print(f"  σ_{i+1} = {val:.{self.precision_salida}f}")
            
            # Análisis del rango y condición
            tolerancia = max(matriz.shape) * np.finfo(float).eps * s[0]
            rango_numerico = np.sum(s > tolerancia)
            condicion = s[0] / s[-1] if s[-1] > 0 else np.inf
            
            print(f"\n🔍 Análisis:")
            print(f"  - Rango numérico: {rango_numerico}")
            print(f"  - Número de condición: {condicion:.2e}")
            
            # Opción de guardar componentes
            guardar = input("\n💾 ¿Guardar matrices U, S, V^T? (s/n): ").strip().lower()
            if guardar == 's':
                self.matrices[f"{matriz_nombre}_U"] = U
                self.matrices[f"{matriz_nombre}_S"] = MatrizNumPy(np.diag(s))
                self.matrices[f"{matriz_nombre}_Vt"] = Vt
                print(f"✅ Matrices SVD guardadas como '{matriz_nombre}_U', '{matriz_nombre}_S', '{matriz_nombre}_Vt'")
            
            self.historial_operaciones.append(f"SVD de '{matriz_nombre}': rango {rango_numerico}, cond {condicion:.2e}")
            
        except Exception as e:
            print(f"❌ Error en SVD: {e}")
    
    def descomposicion_qr(self):
        """Descomposición QR."""
        try:
            print("\n🔺 DESCOMPOSICIÓN QR")
            matriz_nombre = self.seleccionar_matriz("Matriz para descomponer")
            if not matriz_nombre:
                return
            
            matriz = self.matrices[matriz_nombre]
            
            print("🔍 Calculando descomposición QR...")
            Q, R = matriz.qr()
            
            print(f"\n✅ QR de '{matriz_nombre}' completada:")
            print(f"  - Q (ortogonal): {Q.shape[0]}×{Q.shape[1]}")
            print(f"  - R (triangular superior): {R.shape[0]}×{R.shape[1]}")
            
            # Verificar ortogonalidad de Q
            QtQ = Q.transponer() @ Q
            error_ortogonal = np.max(np.abs(QtQ.datos - np.eye(Q.shape[1])))
            print(f"🔍 Error de ortogonalidad Q^T × Q - I: {error_ortogonal:.2e}")
            
            # Opción de guardar componentes
            guardar = input("\n💾 ¿Guardar matrices Q y R? (s/n): ").strip().lower()
            if guardar == 's':
                self.matrices[f"{matriz_nombre}_Q"] = Q
                self.matrices[f"{matriz_nombre}_R"] = R
                print(f"✅ Matrices QR guardadas como '{matriz_nombre}_Q' y '{matriz_nombre}_R'")
            
            self.historial_operaciones.append(f"QR de '{matriz_nombre}': error ortogonal {error_ortogonal:.2e}")
            
        except Exception as e:
            print(f"❌ Error en QR: {e}")
    
    def descomposicion_cholesky(self):
        """Descomposición de Cholesky."""
        try:
            print("\n💎 DESCOMPOSICIÓN DE CHOLESKY")
            matriz_nombre = self.seleccionar_matriz("Matriz (debe ser simétrica definida positiva)")
            if not matriz_nombre:
                return
            
            matriz = self.matrices[matriz_nombre]
            
            if not matriz.es_cuadrada():
                print("❌ La matriz debe ser cuadrada.")
                return
                
            if not matriz.es_simetrica():
                print("❌ La matriz debe ser simétrica.")
                return
                
            if not matriz.es_definida_positiva():
                print("❌ La matriz debe ser definida positiva.")
                return
            
            print("🔍 Calculando descomposición de Cholesky...")
            L = matriz.cholesky()
            
            print(f"\n✅ Cholesky de '{matriz_nombre}' completada:")
            print(f"  - L (triangular inferior): {L.shape[0]}×{L.shape[1]}")
            
            L.mostrar(f"Matriz L de Cholesky")
            
            # Verificación
            LLt = L @ L.transponer()
            error = np.max(np.abs(LLt.datos - matriz.datos))
            print(f"🔍 Error de verificación L × L^T - A: {error:.2e}")
            
            # Opción de guardar
            guardar = input("\n💾 ¿Guardar matriz L? (s/n): ").strip().lower()
            if guardar == 's':
                nombre_L = input(f"🏷️ Nombre para L (default: {matriz_nombre}_L): ").strip()
                if not nombre_L:
                    nombre_L = f"{matriz_nombre}_L"
                self.matrices[nombre_L] = L
                print(f"✅ Matriz L guardada como '{nombre_L}'")
            
            self.historial_operaciones.append(f"Cholesky de '{matriz_nombre}': error {error:.2e}")
            
        except Exception as e:
            print(f"❌ Error en Cholesky: {e}")
    
    def resolver_sistema_lineal(self):
        """Resolver sistema de ecuaciones lineales."""
        try:
            print("\n🧮 RESOLVER SISTEMA LINEAL Ax = b")
            
            print("\nSeleccionar matriz A (coeficientes):")
            matriz_A_nombre = self.seleccionar_matriz("Matriz de coeficientes A")
            if not matriz_A_nombre:
                return
                
            matriz_A = self.matrices[matriz_A_nombre]
            
            # Opción para el vector b
            print("\n📋 Vector independiente b:")
            print("1. Crear vector manualmente")
            print("2. Usar matriz existente como vector")
            
            opcion_b = input("🎯 Opción: ").strip()
            
            if opcion_b == "1":
                # Crear vector b manualmente
                n = matriz_A.shape[0]
                print(f"📝 Ingresa {n} valores para el vector b:")
                b_valores = []
                for i in range(n):
                    val = float(input(f"  b[{i+1}]: "))
                    b_valores.append(val)
                b = np.array(b_valores).reshape(-1, 1)
                
            elif opcion_b == "2":
                # Usar matriz existente
                matriz_b_nombre = self.seleccionar_matriz("Vector b")
                if not matriz_b_nombre:
                    return
                matriz_b = self.matrices[matriz_b_nombre]
                b = matriz_b.datos.reshape(-1, 1) if matriz_b.datos.ndim == 1 else matriz_b.datos
                
            else:
                print("❌ Opción no válida.")
                return
            
            print("🔍 Resolviendo sistema...")
            x = matriz_A.resolver_sistema(MatrizNumPy(b))
            
            print(f"\n✅ Solución encontrada:")
            x.mostrar("Solución x")
            
            # Verificación
            Ax = matriz_A @ x
            residuo = np.max(np.abs(Ax.datos - b))
            print(f"🔍 Residuo ||Ax - b||_∞: {residuo:.2e}")
            
            # Opción de guardar
            guardar = input("\n💾 ¿Guardar solución? (s/n): ").strip().lower()
            if guardar == 's':
                nombre_x = input("🏷️ Nombre para la solución: ").strip()
                if nombre_x:
                    self.matrices[nombre_x] = x
                    print(f"✅ Solución guardada como '{nombre_x}'")
            
            self.historial_operaciones.append(f"Sistema resuelto: A={matriz_A_nombre}, residuo={residuo:.2e}")
            
        except Exception as e:
            print(f"❌ Error al resolver sistema: {e}")
    
    def calcular_normas(self):
        """Calcular diferentes normas de una matriz."""
        try:
            print("\n📏 NORMAS DE MATRIZ")
            matriz_nombre = self.seleccionar_matriz("Matriz")
            if not matriz_nombre:
                return
            
            matriz = self.matrices[matriz_nombre]
            
            print(f"\n✅ Normas de '{matriz_nombre}':")
            
            # Norma de Frobenius
            norma_fro = matriz.norma('fro')
            print(f"  - Frobenius: {norma_fro:.{self.precision_salida}f}")
            
            # Norma espectral (2-norma)
            norma_2 = matriz.norma(2)
            print(f"  - Espectral (2): {norma_2:.{self.precision_salida}f}")
            
            # Norma infinito
            norma_inf = matriz.norma(np.inf)
            print(f"  - Infinito: {norma_inf:.{self.precision_salida}f}")
            
            # Norma 1
            norma_1 = matriz.norma(1)
            print(f"  - 1-norma: {norma_1:.{self.precision_salida}f}")
            
            # Número de condición (si es cuadrada)
            if matriz.es_cuadrada():
                cond = matriz.condicion()
                print(f"  - Número de condición: {cond:.2e}")
                
                if cond > 1e12:
                    print("    ⚠️ Matriz muy mal condicionada")
                elif cond > 1e6:
                    print("    ⚠️ Matriz mal condicionada") 
                else:
                    print("    ✅ Matriz bien condicionada")
            
            self.historial_operaciones.append(f"Normas de '{matriz_nombre}': Fro={norma_fro:.3f}, 2={norma_2:.3f}")
            
        except Exception as e:
            print(f"❌ Error al calcular normas: {e}")
    
    def menu_gestionar_matrices(self):
        """Menú para gestionar matrices."""
        while True:
            print("\n📁 GESTIONAR MATRICES")
            print("="*25)
            print("1. 📋 Listar Matrices")
            print("2. 👁️ Ver Matriz")
            print("3. 🏷️ Renombrar Matriz")
            print("4. 📋 Copiar Matriz")
            print("5. 🗑️ Eliminar Matriz")
            print("6. 🧹 Limpiar Todas")
            print("0. ⬅️ Volver")
            
            opcion = input("\n🎯 Opción: ").strip()
            
            if opcion == "1":
                self.listar_matrices()
            elif opcion == "2":
                self.ver_matriz()
            elif opcion == "3":
                self.renombrar_matriz()
            elif opcion == "4":
                self.copiar_matriz()
            elif opcion == "5":
                self.eliminar_matriz()
            elif opcion == "6":
                self.limpiar_matrices()
            elif opcion == "0":
                break
    
    def listar_matrices(self):
        """Listar todas las matrices disponibles."""
        print("\n📋 MATRICES DISPONIBLES")
        print("="*30)
        
        if not self.matrices:
            print("❌ No hay matrices disponibles.")
            return
        
        for i, (nombre, matriz) in enumerate(self.matrices.items(), 1):
            filas, columnas = matriz.shape
            tipo = "Cuadrada" if filas == columnas else "Rectangular"
            memoria = matriz.datos.nbytes
            
            print(f"{i:2d}. 🔹 {nombre}")
            print(f"     📏 Dimensiones: {filas}×{columnas} ({tipo})")
            print(f"     💾 Memoria: {memoria} bytes")
            print(f"     🔢 Tipo: {matriz.datos.dtype}")
            print()
    
    def ver_matriz(self):
        """Ver una matriz específica."""
        print("\n👁️ VER MATRIZ")
        matriz_nombre = self.seleccionar_matriz("Matriz a visualizar")
        if not matriz_nombre:
            return
        
        matriz = self.matrices[matriz_nombre]
        matriz.mostrar(f"Matriz {matriz_nombre}")
        
        self.historial_operaciones.append(f"Visualizada '{matriz_nombre}'")
    
    def renombrar_matriz(self):
        """Renombrar una matriz."""
        try:
            print("\n🏷️ RENOMBRAR MATRIZ")
            matriz_nombre = self.seleccionar_matriz("Matriz a renombrar")
            if not matriz_nombre:
                return
            
            nuevo_nombre = input("🆕 Nuevo nombre: ").strip()
            if not nuevo_nombre:
                print("❌ El nuevo nombre no puede estar vacío.")
                return
            
            if nuevo_nombre in self.matrices:
                print("❌ Ya existe una matriz con ese nombre.")
                return
            
            # Renombrar
            self.matrices[nuevo_nombre] = self.matrices.pop(matriz_nombre)
            
            print(f"✅ Matriz renombrada de '{matriz_nombre}' a '{nuevo_nombre}'")
            self.historial_operaciones.append(f"Renombrada '{matriz_nombre}' → '{nuevo_nombre}'")
            
        except Exception as e:
            print(f"❌ Error al renombrar: {e}")
    
    def copiar_matriz(self):
        """Copiar una matriz."""
        try:
            print("\n📋 COPIAR MATRIZ")
            matriz_nombre = self.seleccionar_matriz("Matriz a copiar")
            if not matriz_nombre:
                return
            
            nuevo_nombre = input("🆕 Nombre de la copia: ").strip()
            if not nuevo_nombre:
                print("❌ El nombre de la copia no puede estar vacío.")
                return
            
            if nuevo_nombre in self.matrices:
                print("❌ Ya existe una matriz con ese nombre.")
                return
            
            # Copiar
            matriz_original = self.matrices[matriz_nombre]
            self.matrices[nuevo_nombre] = MatrizNumPy(matriz_original.datos.copy())
            
            print(f"✅ Matriz copiada: '{matriz_nombre}' → '{nuevo_nombre}'")
            self.historial_operaciones.append(f"Copiada '{matriz_nombre}' → '{nuevo_nombre}'")
            
        except Exception as e:
            print(f"❌ Error al copiar: {e}")
    
    def eliminar_matriz(self):
        """Eliminar una matriz."""
        try:
            print("\n🗑️ ELIMINAR MATRIZ")
            matriz_nombre = self.seleccionar_matriz("Matriz a eliminar")
            if not matriz_nombre:
                return
            
            confirmacion = input(f"⚠️ ¿Estás seguro de eliminar '{matriz_nombre}'? (s/n): ").strip().lower()
            if confirmacion != 's':
                print("❌ Eliminación cancelada.")
                return
            
            del self.matrices[matriz_nombre]
            
            print(f"✅ Matriz '{matriz_nombre}' eliminada exitosamente.")
            self.historial_operaciones.append(f"Eliminada '{matriz_nombre}'")
            
        except Exception as e:
            print(f"❌ Error al eliminar: {e}")
    
    def limpiar_matrices(self):
        """Limpiar todas las matrices."""
        try:
            print("\n🧹 LIMPIAR TODAS LAS MATRICES")
            
            if not self.matrices:
                print("❌ No hay matrices para limpiar.")
                return
            
            num_matrices = len(self.matrices)
            confirmacion = input(f"⚠️ ¿Eliminar todas las {num_matrices} matrices? (s/n): ").strip().lower()
            if confirmacion != 's':
                print("❌ Limpieza cancelada.")
                return
            
            self.matrices.clear()
            
            print(f"✅ Todas las matrices eliminadas ({num_matrices} matrices).")
            self.historial_operaciones.append(f"Limpiadas {num_matrices} matrices")
            
        except Exception as e:
            print(f"❌ Error al limpiar: {e}")
    
