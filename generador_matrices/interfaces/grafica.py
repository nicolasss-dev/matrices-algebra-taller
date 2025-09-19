"""
Interfaz Gráfica
================

Interfaz gráfica usando Tkinter para el generador de matrices.
Proporciona una GUI intuitiva para todas las funcionalidades.

Autor: Nicolas
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.matriz import Matriz
from src.operaciones import *
from src.utilidades import formatear_numero


class InterfazGrafica:
    """
    Clase que maneja la interfaz gráfica usando Tkinter.
    """
    
    def __init__(self):
        """Inicializa la interfaz gráfica."""
        self.root = None
        self.matrices = {}
        self.contador_matrices = 0
        
        # Variables para la GUI (se inicializarán después de crear root)
        self.filas_var = None
        self.columnas_var = None
        self.matriz_seleccionada = None
        self.metodo_var = None
        
        # Widgets principales
        self.lista_matrices = None
        self.texto_matriz = None
    
    
    def iniciar(self):
        """Inicia la interfaz gráfica."""
        try:
            # Verificar si tkinter está disponible
            import tkinter.ttk
            self.crear_ventana_principal()
            self.root.mainloop()
        except ImportError:
            print("❌ Error: tkinter no está disponible.")
            print("En Windows, tkinter debería estar incluido con Python.")
            print("Si el problema persiste, reinstala Python con tkinter habilitado.")
        except Exception as e:
            print(f"❌ Error al iniciar la interfaz gráfica: {e}")
            print("Intentando solución alternativa...")
            try:
                # Intentar con configuración básica
                self.iniciar_basico()
            except Exception as e2:
                print(f"❌ Error crítico: {e2}")
                print("Por favor, usa la interfaz de consola (opción 1 en el menú principal).")
    
    
    def iniciar_basico(self):
        """Versión básica de la interfaz gráfica como respaldo."""
        self.root = tk.Tk()
        self.root.title("Generador de Matrices - Básico")
        self.root.geometry("400x300")
        
        # Variables básicas
        self.filas_var = tk.StringVar(value="2")
        self.columnas_var = tk.StringVar(value="2")
        
        # Interfaz muy simple
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(frame, text="Generador de Matrices", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(frame, text="Versión Básica", font=("Arial", 10)).pack()
        
        tk.Label(frame, text="\nEsta es una versión simplificada.").pack()
        tk.Label(frame, text="Para la experiencia completa, usa la interfaz de consola.").pack()
        
        tk.Button(frame, text="Cerrar", command=self.root.quit, pady=5).pack(pady=20)
        
        self.root.mainloop()
    
    
    def crear_ventana_principal(self):
        """Crea la ventana principal de la aplicación."""
        self.root = tk.Tk()
        self.root.title("Generador de Matrices - Interfaz Gráfica")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        # Inicializar variables Tkinter ahora que tenemos root
        self.filas_var = tk.StringVar(value="3")
        self.columnas_var = tk.StringVar(value="3")
        self.matriz_seleccionada = tk.StringVar()
        self.metodo_var = tk.StringVar(value="manual")
        
        # Configurar el estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        # Crear el notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Crear las pestañas
        self.crear_pestaña_crear()
        self.crear_pestaña_matrices()
        self.crear_pestaña_operaciones()
        self.crear_pestaña_acerca_de()
        
        # Crear la barra de estado
        self.crear_barra_estado()
        
        # Configurar el protocolo de cierre
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)
        
        self.actualizar_barra_estado("Listo")
    
    
    def crear_pestaña_crear(self):
        """Crea la pestaña para crear nuevas matrices."""
        frame_crear = ttk.Frame(self.notebook)
        self.notebook.add(frame_crear, text="Crear Matriz")
        
        # Frame principal
        main_frame = ttk.Frame(frame_crear)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        titulo = ttk.Label(main_frame, text="Crear Nueva Matriz", font=("Arial", 16, "bold"))
        titulo.pack(pady=(0, 20))
        
        # Frame para dimensiones
        dim_frame = ttk.LabelFrame(main_frame, text="Dimensiones", padding=10)
        dim_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Filas
        ttk.Label(dim_frame, text="Filas:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        filas_spin = ttk.Spinbox(dim_frame, from_=1, to=10, textvariable=self.filas_var, width=5)
        filas_spin.grid(row=0, column=1, sticky=tk.W)
        
        # Columnas
        ttk.Label(dim_frame, text="Columnas:").grid(row=0, column=2, sticky=tk.W, padx=(20, 10))
        columnas_spin = ttk.Spinbox(dim_frame, from_=1, to=10, textvariable=self.columnas_var, width=5)
        columnas_spin.grid(row=0, column=3, sticky=tk.W)
        
        # Frame para métodos de llenado
        metodo_frame = ttk.LabelFrame(main_frame, text="Método de Llenado", padding=10)
        metodo_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Radiobutton(metodo_frame, text="Llenar manualmente",
                       variable=self.metodo_var, value="manual").pack(anchor=tk.W)
        ttk.Radiobutton(metodo_frame, text="Números aleatorios (-10 a 10)", 
                       variable=self.metodo_var, value="aleatorio").pack(anchor=tk.W)
        ttk.Radiobutton(metodo_frame, text="Matriz de ceros", 
                       variable=self.metodo_var, value="ceros").pack(anchor=tk.W)
        ttk.Radiobutton(metodo_frame, text="Matriz de unos", 
                       variable=self.metodo_var, value="unos").pack(anchor=tk.W)
        
        # Botón para crear
        ttk.Button(main_frame, text="Crear Matriz", 
                  command=self.crear_matriz_gui).pack(pady=20)
    
    
    def crear_pestaña_matrices(self):
        """Crea la pestaña para listar y mostrar matrices."""
        frame_matrices = ttk.Frame(self.notebook)
        self.notebook.add(frame_matrices, text="Matrices")
        
        # Frame principal con división horizontal
        paned = ttk.PanedWindow(frame_matrices, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel izquierdo - Lista de matrices
        frame_izq = ttk.Frame(paned)
        paned.add(frame_izq, weight=1)
        
        ttk.Label(frame_izq, text="Matrices Existentes", font=("Arial", 12, "bold")).pack()
        
        # Listbox para matrices
        list_frame = ttk.Frame(frame_izq)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.lista_matrices = tk.Listbox(list_frame)
        scrollbar_list = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.lista_matrices.yview)
        self.lista_matrices.configure(yscrollcommand=scrollbar_list.set)
        
        self.lista_matrices.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_list.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind para selección
        self.lista_matrices.bind('<<ListboxSelect>>', self.on_matriz_seleccionada)
        
        # Botones
        btn_frame = ttk.Frame(frame_izq)
        btn_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(btn_frame, text="Actualizar", command=self.actualizar_lista_matrices).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_matriz_gui).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Limpiar Todo", command=self.limpiar_matrices_gui).pack(fill=tk.X, pady=2)
        
        # Panel derecho - Visualización de matriz
        frame_der = ttk.Frame(paned)
        paned.add(frame_der, weight=2)
        
        ttk.Label(frame_der, text="Vista de Matriz", font=("Arial", 12, "bold")).pack()
        
        # Área de texto para mostrar la matriz
        text_frame = ttk.Frame(frame_der)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.texto_matriz = tk.Text(text_frame, font=("Courier", 10), state=tk.DISABLED)
        scrollbar_text = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.texto_matriz.yview)
        self.texto_matriz.configure(yscrollcommand=scrollbar_text.set)
        
        self.texto_matriz.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_text.pack(side=tk.RIGHT, fill=tk.Y)
    
    
    def crear_pestaña_operaciones(self):
        """Crea la pestaña para operaciones con matrices."""
        frame_ops = ttk.Frame(self.notebook)
        self.notebook.add(frame_ops, text="Operaciones")
        
        main_frame = ttk.Frame(frame_ops)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        titulo = ttk.Label(main_frame, text="Operaciones con Matrices", font=("Arial", 16, "bold"))
        titulo.pack(pady=(0, 20))
        
        # Frame para operaciones con dos matrices
        ops_frame = ttk.LabelFrame(main_frame, text="Operaciones con Dos Matrices", padding=10)
        ops_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Button(ops_frame, text="Sumar Matrices", 
                  command=lambda: self.operacion_dos_matrices("suma")).pack(side=tk.LEFT, padx=5)
        ttk.Button(ops_frame, text="Restar Matrices", 
                  command=lambda: self.operacion_dos_matrices("resta")).pack(side=tk.LEFT, padx=5)
        ttk.Button(ops_frame, text="Multiplicar Matrices", 
                  command=lambda: self.operacion_dos_matrices("multiplicacion")).pack(side=tk.LEFT, padx=5)
        
        # Frame para operaciones con una matriz
        ops_single_frame = ttk.LabelFrame(main_frame, text="Operaciones con Una Matriz", padding=10)
        ops_single_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Button(ops_single_frame, text="Transponer", 
                  command=self.transponer_matriz_gui).pack(side=tk.LEFT, padx=5)
        ttk.Button(ops_single_frame, text="Multiplicar por Escalar", 
                  command=self.multiplicar_escalar_gui).pack(side=tk.LEFT, padx=5)
        ttk.Button(ops_single_frame, text="Copiar Matriz", 
                  command=self.copiar_matriz_gui).pack(side=tk.LEFT, padx=5)
        
        # Frame para matrices especiales
        special_frame = ttk.LabelFrame(main_frame, text="Matrices Especiales", padding=10)
        special_frame.pack(fill=tk.X)
        
        ttk.Button(special_frame, text="Matriz Identidad", 
                  command=self.crear_matriz_identidad_gui).pack(side=tk.LEFT, padx=5)
    
    
    def crear_pestaña_acerca_de(self):
        """Crea la pestaña con información sobre la aplicación."""
        frame_about = ttk.Frame(self.notebook)
        self.notebook.add(frame_about, text="Acerca de")
        
        main_frame = ttk.Frame(frame_about)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        titulo = ttk.Label(main_frame, text="Generador de Matrices", font=("Arial", 18, "bold"))
        titulo.pack(pady=(0, 10))
        
        # Información
        info_text = """
Versión: 1.0.0
Autor: Nicolas

Esta aplicación permite crear y manipular matrices de forma sencilla e intuitiva.

Características:
• Creación de matrices de cualquier tamaño (hasta 10x10)
• Operaciones matemáticas básicas
• Soporte para números enteros, decimales y fracciones
• Interfaz gráfica amigable

Instrucciones:
1. Ve a la pestaña "Crear Matriz" para crear nuevas matrices
2. Usa "Matrices" para ver y gestionar las matrices existentes
3. En "Operaciones" puedes realizar cálculos entre matrices

¡Disfruta usando el Generador de Matrices!
        """
        
        info_label = ttk.Label(main_frame, text=info_text, justify=tk.LEFT)
        info_label.pack(anchor=tk.W)
    
    
    def crear_barra_estado(self):
        """Crea la barra de estado en la parte inferior."""
        self.barra_estado = ttk.Label(self.root, text="Listo", relief=tk.SUNKEN, anchor=tk.W)
        self.barra_estado.pack(side=tk.BOTTOM, fill=tk.X)
    
    
    def actualizar_barra_estado(self, mensaje):
        """Actualiza el texto de la barra de estado."""
        self.barra_estado.config(text=mensaje)
        self.root.update()
    
    
    def crear_matriz_gui(self):
        """Crea una matriz usando la interfaz gráfica."""
        try:
            filas = int(self.filas_var.get())
            columnas = int(self.columnas_var.get())
            metodo = self.metodo_var.get()
            
            # Validar dimensiones
            if filas < 1 or filas > 10 or columnas < 1 or columnas > 10:
                messagebox.showerror("Error", "Las dimensiones deben estar entre 1 y 10")
                return
            
            # Crear matriz
            matriz = Matriz(filas, columnas)
            
            if metodo == "manual":
                if self.llenar_matriz_manual(matriz):
                    self.guardar_matriz(matriz)
                return
            elif metodo == "aleatorio":
                matriz.llenar_aleatorio(-10, 10)
            elif metodo == "ceros":
                # Ya está llena de ceros por defecto
                pass
            elif metodo == "unos":
                for i in range(filas):
                    for j in range(columnas):
                        matriz.datos[i][j] = 1
            
            self.guardar_matriz(matriz)
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa dimensiones válidas")
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear la matriz: {e}")
    
    
    def llenar_matriz_manual(self, matriz):
        """Abre una ventana para llenar la matriz manualmente."""
        ventana = tk.Toplevel(self.root)
        ventana.title("Llenar Matriz Manualmente")
        ventana.geometry("400x300")
        ventana.transient(self.root)
        ventana.grab_set()
        
        # Centrar la ventana
        ventana.geometry(f"+{self.root.winfo_rootx() + 50}+{self.root.winfo_rooty() + 50}")
        
        main_frame = ttk.Frame(ventana)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Label(main_frame, text=f"Ingresa los valores para la matriz {matriz.filas}x{matriz.columnas}:", 
                 font=("Arial", 10, "bold")).pack(pady=(0, 10))
        
        # Crear grid de entries
        entries = []
        grid_frame = ttk.Frame(main_frame)
        grid_frame.pack()
        
        for i in range(matriz.filas):
            fila_entries = []
            for j in range(matriz.columnas):
                entry = ttk.Entry(grid_frame, width=8, justify=tk.CENTER)
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, "0")  # Valor por defecto
                fila_entries.append(entry)
            entries.append(fila_entries)
        
        resultado = {"matriz_llena": False}
        
        def aceptar():
            try:
                for i in range(matriz.filas):
                    for j in range(matriz.columnas):
                        valor_str = entries[i][j].get().strip()
                        if '/' in valor_str:
                            from fractions import Fraction
                            valor = Fraction(valor_str)
                        else:
                            valor = float(valor_str) if '.' in valor_str else int(valor_str)
                        matriz.datos[i][j] = valor
                
                resultado["matriz_llena"] = True
                ventana.destroy()
                
            except Exception as e:
                messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
        
        def cancelar():
            ventana.destroy()
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="Aceptar", command=aceptar).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="Cancelar", command=cancelar).pack(side=tk.LEFT, padx=10)
        
        # Esperar a que se cierre la ventana
        self.root.wait_window(ventana)
        
        return resultado["matriz_llena"]
    
    
    def guardar_matriz(self, matriz):
        """Guarda una matriz en el diccionario y actualiza la interfaz."""
        self.contador_matrices += 1
        nombre = f"Matriz_{self.contador_matrices}"
        self.matrices[nombre] = matriz
        
        self.actualizar_lista_matrices()
        self.actualizar_barra_estado(f"Matriz '{nombre}' creada exitosamente")
        
        # Mostrar la matriz recién creada
        self.mostrar_resultado_operacion(matriz, nombre, "Creación de Matriz")
    
    
    def actualizar_lista_matrices(self):
        """Actualiza la lista de matrices en la interfaz."""
        if self.lista_matrices:
            self.lista_matrices.delete(0, tk.END)
            for nombre, matriz in self.matrices.items():
                self.lista_matrices.insert(tk.END, f"{nombre} ({matriz.filas}x{matriz.columnas})")
    
    
    def on_matriz_seleccionada(self, event):
        """Maneja la selección de una matriz en la lista."""
        selection = self.lista_matrices.curselection()
        if selection:
            indice = selection[0]
            nombres = list(self.matrices.keys())
            if indice < len(nombres):
                nombre = nombres[indice]
                matriz = self.matrices[nombre]
                self.mostrar_matriz_en_texto(matriz, nombre)
    
    
    def mostrar_matriz_en_texto(self, matriz, nombre="Matriz"):
        """Muestra una matriz en el widget de texto."""
        if self.texto_matriz:
            self.texto_matriz.config(state=tk.NORMAL)
            self.texto_matriz.delete(1.0, tk.END)
            
            texto = f"{nombre}:\n"
            texto += f"Dimensiones: {matriz.filas}x{matriz.columnas}\n"
            texto += f"Es cuadrada: {'Sí' if matriz.es_cuadrada() else 'No'}\n\n"
            
            # Formatear la matriz
            for fila in matriz.datos:
                elementos_formateados = []
                for elemento in fila:
                    elem_str = formatear_numero(elemento)
                    elementos_formateados.append(f"{elem_str:>8}")
                texto += "[ " + "  ".join(elementos_formateados) + " ]\n"
            
            self.texto_matriz.insert(tk.END, texto)
            self.texto_matriz.config(state=tk.DISABLED)
    
    
    def seleccionar_matriz(self, titulo="Seleccionar Matriz"):
        """Abre un diálogo para seleccionar una matriz."""
        if not self.matrices:
            messagebox.showerror("Error", "No hay matrices disponibles")
            return None
        
        nombres = list(self.matrices.keys())
        
        # Crear ventana de selección
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("400x300")
        
        # Centrar la ventana
        ventana.transient(self.root)
        ventana.grab_set()
        
        # Hacer que la ventana sea modal
        ventana.focus_set()
        
        # Resultado compartido
        resultado = {"matriz": None, "cancelado": False}
        
        # Frame principal
        main_frame = ttk.Frame(ventana, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="Selecciona una matriz:", 
                 font=("Arial", 12, "bold")).pack(pady=(0, 10))
        
        # Frame para la lista
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Listbox con scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, 
                           selectmode=tk.SINGLE, height=8)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)
        
        # Llenar la lista
        for i, nombre in enumerate(nombres):
            matriz = self.matrices[nombre]
            listbox.insert(tk.END, f"{nombre} ({matriz.filas}x{matriz.columnas})")
        
        # Seleccionar el primer elemento por defecto
        if nombres:
            listbox.selection_set(0)
            listbox.activate(0)
        
        def aceptar():
            selection = listbox.curselection()
            if selection:
                indice = selection[0]
                resultado["matriz"] = nombres[indice]
                ventana.quit()
                ventana.destroy()
            else:
                messagebox.showwarning("Advertencia", "Por favor selecciona una matriz")
        
        def cancelar():
            resultado["cancelado"] = True
            ventana.quit()
            ventana.destroy()
        
        def on_double_click(event):
            aceptar()
        
        # Bind para doble clic
        listbox.bind("<Double-Button-1>", on_double_click)
        
        # Frame para botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=(10, 0))
        
        ttk.Button(btn_frame, text="Aceptar", command=aceptar).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Cancelar", command=cancelar).pack(side=tk.LEFT, padx=(5, 0))
        
        # Bind para teclas
        ventana.bind("<Return>", lambda e: aceptar())
        ventana.bind("<Escape>", lambda e: cancelar())
        
        # Esperar a que termine
        ventana.mainloop()
        
        return None if resultado["cancelado"] else resultado["matriz"]
    
    
    def mostrar_resultado_operacion(self, matriz_resultado, nombre_resultado, tipo_operacion, matriz1_info=None, matriz2_info=None):
        """Muestra el resultado de una operación en una ventana separada."""
        ventana_resultado = tk.Toplevel(self.root)
        ventana_resultado.title(f"Resultado: {nombre_resultado}")
        ventana_resultado.geometry("500x400")
        ventana_resultado.transient(self.root)
        
        # Frame principal
        main_frame = ttk.Frame(ventana_resultado, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo_label = ttk.Label(main_frame, text=f"✅ {tipo_operacion} Completada", 
                               font=("Arial", 14, "bold"), foreground="green")
        titulo_label.pack(pady=(0, 10))
        
        # Nombre del resultado
        nombre_label = ttk.Label(main_frame, text=f"Resultado guardado como: '{nombre_resultado}'", 
                               font=("Arial", 12))
        nombre_label.pack(pady=(0, 15))
        
        # Información de la matriz
        info_frame = ttk.LabelFrame(main_frame, text="Información de la Matriz", padding="10")
        info_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(info_frame, text=f"Dimensiones: {matriz_resultado.filas} × {matriz_resultado.columnas}").pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Es cuadrada: {'Sí' if matriz_resultado.es_cuadrada() else 'No'}").pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Total de elementos: {matriz_resultado.filas * matriz_resultado.columnas}").pack(anchor=tk.W)
        
        # Información de matrices originales si está disponible
        if matriz1_info or matriz2_info:
            op_frame = ttk.LabelFrame(main_frame, text="Operación Realizada", padding="10")
            op_frame.pack(fill=tk.X, pady=(0, 15))
            
            if matriz1_info and matriz2_info:
                ttk.Label(op_frame, text=f"{matriz1_info} → {tipo_operacion} ← {matriz2_info}", 
                         font=("Arial", 10, "bold")).pack()
            elif matriz1_info:
                ttk.Label(op_frame, text=f"{matriz1_info} → {tipo_operacion}", 
                         font=("Arial", 10, "bold")).pack()
        
        # Matriz resultado
        matriz_frame = ttk.LabelFrame(main_frame, text="Matriz Resultado", padding="10")
        matriz_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Área de texto para la matriz
        text_frame = ttk.Frame(matriz_frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar_v = ttk.Scrollbar(text_frame, orient=tk.VERTICAL)
        scrollbar_h = ttk.Scrollbar(text_frame, orient=tk.HORIZONTAL)
        
        texto_resultado = tk.Text(text_frame, font=("Courier", 10), 
                                yscrollcommand=scrollbar_v.set,
                                xscrollcommand=scrollbar_h.set,
                                wrap=tk.NONE, state=tk.DISABLED)
        
        scrollbar_v.config(command=texto_resultado.yview)
        scrollbar_h.config(command=texto_resultado.xview)
        
        # Empaquetar widgets
        texto_resultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_h.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Llenar con el contenido de la matriz
        texto_resultado.config(state=tk.NORMAL)
        
        # Formatear la matriz
        contenido = ""
        max_ancho = 0
        for fila in matriz_resultado.datos:
            for elemento in fila:
                ancho = len(formatear_numero(elemento))
                max_ancho = max(max_ancho, ancho)
        
        max_ancho = max(max_ancho, 4)
        
        for fila in matriz_resultado.datos:
            elementos_formateados = []
            for elemento in fila:
                elem_str = formatear_numero(elemento)
                elementos_formateados.append(f"{elem_str:>{max_ancho}}")
            contenido += "[ " + "  ".join(elementos_formateados) + " ]\n"
        
        texto_resultado.insert(tk.END, contenido)
        texto_resultado.config(state=tk.DISABLED)
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=(10, 0))
        
        def ir_a_matrices():
            ventana_resultado.destroy()
            self.notebook.select(1)  # Cambiar a la pestaña de matrices
        
        def copiar_resultado():
            self.root.clipboard_clear()
            self.root.clipboard_append(contenido)
            messagebox.showinfo("Copiado", "Matriz copiada al portapapeles")
        
        ttk.Button(btn_frame, text="Ver en Lista de Matrices", command=ir_a_matrices).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text="Copiar Matriz", command=copiar_resultado).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text="Cerrar", command=ventana_resultado.destroy).pack(side=tk.LEFT)
        
        # Centrar la ventana y darle foco
        ventana_resultado.focus_set()
    
    
    def seleccionar_matriz_simple(self, titulo="Seleccionar Matriz"):
        """Versión simplificada del selector de matrices."""
        if not self.matrices:
            messagebox.showerror("Error", "No hay matrices disponibles")
            return None
        
        nombres = list(self.matrices.keys())
        opciones = []
        for nombre in nombres:
            matriz = self.matrices[nombre]
            opciones.append(f"{nombre} ({matriz.filas}x{matriz.columnas})")
        
        # Usar simpledialog para una selección rápida
        from tkinter import simpledialog
        
        mensaje = f"{titulo}\n\nMatrices disponibles:\n" + "\n".join([f"{i+1}. {op}" for i, op in enumerate(opciones)])
        
        while True:
            try:
                respuesta = simpledialog.askstring(
                    titulo,
                    mensaje + f"\n\nIngresa el número (1-{len(opciones)}):",
                    parent=self.root
                )
                
                if respuesta is None:  # Usuario canceló
                    return None
                
                indice = int(respuesta) - 1
                if 0 <= indice < len(nombres):
                    return nombres[indice]
                else:
                    messagebox.showerror("Error", f"Número inválido. Debe estar entre 1 y {len(opciones)}")
            
            except ValueError:
                messagebox.showerror("Error", "Por favor ingresa un número válido")
    
    
    def operacion_dos_matrices(self, operacion):
        """Realiza operaciones que requieren dos matrices."""
        if len(self.matrices) < 2:
            messagebox.showerror("Error", "Necesitas al menos dos matrices para esta operación")
            return
        
        # Intentar con el selector normal primero, si falla usar el simple
        try:
            matriz1_nombre = self.seleccionar_matriz("Seleccionar Primera Matriz")
        except Exception as e:
            matriz1_nombre = self.seleccionar_matriz_simple("Seleccionar Primera Matriz")
        
        if not matriz1_nombre:
            return
        
        try:
            matriz2_nombre = self.seleccionar_matriz("Seleccionar Segunda Matriz")
        except Exception as e:
            matriz2_nombre = self.seleccionar_matriz_simple("Seleccionar Segunda Matriz")
        
        if not matriz2_nombre:
            return
        
        matriz1 = self.matrices[matriz1_nombre]
        matriz2 = self.matrices[matriz2_nombre]
        
        try:
            if operacion == "suma":
                resultado = sumar_matrices(matriz1, matriz2)
                op_nombre = "Suma"
            elif operacion == "resta":
                resultado = restar_matrices(matriz1, matriz2)
                op_nombre = "Resta"
            elif operacion == "multiplicacion":
                resultado = multiplicar_matrices(matriz1, matriz2)
                op_nombre = "Multiplicación"
            
            # Guardar resultado
            self.contador_matrices += 1
            nombre_resultado = f"{op_nombre}_{self.contador_matrices}"
            self.matrices[nombre_resultado] = resultado
            
            self.actualizar_lista_matrices()
            
            # Mostrar resultado inmediatamente con información de las matrices originales
            matriz1_info = f"{matriz1_nombre} ({matriz1.filas}×{matriz1.columnas})"
            matriz2_info = f"{matriz2_nombre} ({matriz2.filas}×{matriz2.columnas})"
            self.mostrar_resultado_operacion(resultado, nombre_resultado, op_nombre, matriz1_info, matriz2_info)
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error en la operación: {e}")
    
    
    def transponer_matriz_gui(self):
        """Transpone una matriz seleccionada."""
        try:
            nombre = self.seleccionar_matriz("Seleccionar Matriz a Transponer")
        except Exception as e:
            nombre = self.seleccionar_matriz_simple("Seleccionar Matriz a Transponer")
        
        if not nombre:
            return
        
        matriz = self.matrices[nombre]
        
        try:
            resultado = matriz.transponer()
            
            self.contador_matrices += 1
            nombre_resultado = f"Transpuesta_{self.contador_matrices}"
            self.matrices[nombre_resultado] = resultado
            
            self.actualizar_lista_matrices()
            
            # Mostrar resultado inmediatamente
            matriz_info = f"{nombre} ({matriz.filas}×{matriz.columnas})"
            self.mostrar_resultado_operacion(resultado, nombre_resultado, "Transposición", matriz_info)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    
    
    def multiplicar_escalar_gui(self):
        """Multiplica una matriz por un escalar."""
        try:
            nombre = self.seleccionar_matriz("Seleccionar Matriz")
        except Exception as e:
            nombre = self.seleccionar_matriz_simple("Seleccionar Matriz")
        
        if not nombre:
            return
        
        escalar_str = simpledialog.askstring("Escalar", "Ingresa el valor escalar:")
        if not escalar_str:
            return
        
        try:
            if '/' in escalar_str:
                from fractions import Fraction
                escalar = Fraction(escalar_str)
            else:
                escalar = float(escalar_str) if '.' in escalar_str else int(escalar_str)
            
            matriz = self.matrices[nombre]
            resultado = multiplicar_por_escalar(matriz, escalar)
            
            self.contador_matrices += 1
            nombre_resultado = f"Escalar_{self.contador_matrices}"
            self.matrices[nombre_resultado] = resultado
            
            self.actualizar_lista_matrices()
            
            # Mostrar resultado inmediatamente
            matriz_info = f"{nombre} ({matriz.filas}×{matriz.columnas})"
            self.mostrar_resultado_operacion(resultado, nombre_resultado, f"Multiplicación por Escalar ({escalar})", matriz_info)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    
    
    def copiar_matriz_gui(self):
        """Crea una copia de una matriz."""
        try:
            nombre = self.seleccionar_matriz("Seleccionar Matriz a Copiar")
        except Exception as e:
            nombre = self.seleccionar_matriz_simple("Seleccionar Matriz a Copiar")
        
        if not nombre:
            return
        
        matriz = self.matrices[nombre]
        
        try:
            resultado = matriz.copiar()
            
            self.contador_matrices += 1
            nombre_resultado = f"Copia_{self.contador_matrices}"
            self.matrices[nombre_resultado] = resultado
            
            self.actualizar_lista_matrices()
            
            # Mostrar resultado inmediatamente
            matriz_info = f"{nombre} ({matriz.filas}×{matriz.columnas})"
            self.mostrar_resultado_operacion(resultado, nombre_resultado, "Copia de Matriz", matriz_info)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    
    
    def crear_matriz_identidad_gui(self):
        """Crea una matriz identidad."""
        tamaño_str = simpledialog.askstring("Matriz Identidad", "Ingresa el tamaño (n×n):")
        if not tamaño_str:
            return
        
        try:
            tamaño = int(tamaño_str)
            if tamaño < 1 or tamaño > 10:
                messagebox.showerror("Error", "El tamaño debe estar entre 1 y 10")
                return
            
            resultado = crear_matriz_identidad(tamaño)
            
            self.contador_matrices += 1
            nombre_resultado = f"Identidad_{self.contador_matrices}"
            self.matrices[nombre_resultado] = resultado
            
            self.actualizar_lista_matrices()
            
            # Mostrar resultado inmediatamente
            self.mostrar_resultado_operacion(resultado, nombre_resultado, f"Matriz Identidad {tamaño}×{tamaño}")
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero válido")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    
    
    def eliminar_matriz_gui(self):
        """Elimina una matriz seleccionada."""
        selection = self.lista_matrices.curselection()
        if not selection:
            messagebox.showerror("Error", "Selecciona una matriz para eliminar")
            return
        
        indice = selection[0]
        nombres = list(self.matrices.keys())
        if indice >= len(nombres):
            return
        
        nombre = nombres[indice]
        
        if messagebox.askyesno("Confirmar", f"¿Seguro que deseas eliminar '{nombre}'?"):
            del self.matrices[nombre]
            self.actualizar_lista_matrices()
            self.texto_matriz.config(state=tk.NORMAL)
            self.texto_matriz.delete(1.0, tk.END)
            self.texto_matriz.config(state=tk.DISABLED)
            self.actualizar_barra_estado(f"Matriz '{nombre}' eliminada")
    
    
    def limpiar_matrices_gui(self):
        """Elimina todas las matrices."""
        if not self.matrices:
            messagebox.showinfo("Info", "No hay matrices para eliminar")
            return
        
        if messagebox.askyesno("Confirmar", f"¿Seguro que deseas eliminar todas las {len(self.matrices)} matrices?"):
            self.matrices.clear()
            self.contador_matrices = 0
            self.actualizar_lista_matrices()
            self.texto_matriz.config(state=tk.NORMAL)
            self.texto_matriz.delete(1.0, tk.END)
            self.texto_matriz.config(state=tk.DISABLED)
            self.actualizar_barra_estado("Todas las matrices eliminadas")
    
    
    def cerrar_aplicacion(self):
        """Cierra la aplicación."""
        if messagebox.askyesno("Salir", "¿Seguro que deseas cerrar la aplicación?"):
            self.root.quit()
            self.root.destroy()
