"""
Interfaz Gráfica Avanzada para NumPy
===================================

Interfaz gráfica de usuario optimizada para operaciones con matrices
usando NumPy, tkinter y matplotlib con capacidades científicas avanzadas.

Autor: Nicolas
Versión: 2.0.0 (NumPy Edition)
"""

import sys
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import numpy as np
from typing import Dict, List, Optional, Tuple

# Importar la clase principal
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.matriz_numpy import MatrizNumPy



class InterfazGraficaNP:
    """Interfaz gráfica avanzada para operaciones con matrices usando NumPy."""
    
    def __init__(self):
        """Inicializa la interfaz gráfica."""
        self.matrices: Dict[str, MatrizNumPy] = {}
        self.ventana_principal = None
        self.historial_operaciones: List[str] = []
        
    def iniciar(self):
        """Inicia la interfaz gráfica."""
        self.crear_ventana_principal()
        self.ventana_principal.mainloop()
    
    def crear_ventana_principal(self):
        """Crea la ventana principal de la aplicación."""
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Generador de Matrices con NumPy - Interfaz Gráfica")
        self.ventana_principal.geometry("1200x800")
        self.ventana_principal.resizable(True, True)
        
        # Configurar estilo
        style = ttk.Style()
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Heading.TLabel', font=('Arial', 12, 'bold'))
        
        self.crear_menu_principal()
        self.crear_interfaz_principal()
    
    def crear_menu_principal(self):
        """Crea la barra de menús."""
        menubar = tk.Menu(self.ventana_principal)
        self.ventana_principal.config(menu=menubar)
        
        # Menú Archivo
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="📁 Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="🆕 Nueva Matriz", command=self.nueva_matriz_dialogo)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="📂 Cargar CSV", command=self.cargar_csv)
        menu_archivo.add_command(label="💾 Guardar CSV", command=self.guardar_csv)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="🚪 Salir", command=self.ventana_principal.quit)
        
        # Menú Operaciones
        menu_ops = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="🧮 Operaciones", menu=menu_ops)
        menu_ops.add_command(label="➕ Suma", command=lambda: self.operacion_matrices("suma"))
        menu_ops.add_command(label="➖ Resta", command=lambda: self.operacion_matrices("resta"))
        menu_ops.add_command(label="✖️ Multiplicación", command=lambda: self.operacion_matrices("multiplicacion"))
        menu_ops.add_command(label="🔄 Transposición", command=self.transponer_matriz)
        
        # Menú Análisis
        menu_analisis = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="🔍 Análisis", menu=menu_analisis)
        menu_analisis.add_command(label="🔢 Determinante", command=self.calcular_determinante)
        menu_analisis.add_command(label="↩️ Inversa", command=self.calcular_inversa)
        
        # Menú Ayuda
        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="❓ Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="📖 Manual", command=self.mostrar_ayuda)
        menu_ayuda.add_command(label="ℹ️ Acerca de", command=self.mostrar_acerca_de)
    
    def crear_interfaz_principal(self):
        """Crea la interfaz principal."""
        # Frame principal
        main_frame = ttk.Frame(self.ventana_principal, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.ventana_principal.columnconfigure(0, weight=1)
        self.ventana_principal.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, text="🚀 Generador de Matrices con NumPy", style='Title.TLabel')
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Panel izquierdo - Lista de matrices
        panel_izquierdo = ttk.LabelFrame(main_frame, text="📋 Matrices Disponibles", padding="10")
        panel_izquierdo.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Lista de matrices
        self.lista_matrices = tk.Listbox(panel_izquierdo, height=15, width=30)
        self.lista_matrices.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.lista_matrices.bind('<<ListboxSelect>>', self.seleccionar_matriz)
        
        # Scrollbar para lista
        scrollbar = ttk.Scrollbar(panel_izquierdo, orient="vertical")
        scrollbar.grid(row=0, column=2, sticky=(tk.N, tk.S))
        self.lista_matrices.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lista_matrices.yview)
        
        # Botones de gestión
        btn_frame = ttk.Frame(panel_izquierdo)
        btn_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky=(tk.W, tk.E))
        
        ttk.Button(btn_frame, text="🆕 Nueva", command=self.nueva_matriz_dialogo).grid(row=0, column=0, padx=2)
        ttk.Button(btn_frame, text="🗑️ Eliminar", command=self.eliminar_matriz).grid(row=0, column=1, padx=2)
        ttk.Button(btn_frame, text="👁️ Ver", command=self.ver_matriz).grid(row=0, column=2, padx=2)
        
        # Panel derecho - Visualización y operaciones
        panel_derecho = ttk.LabelFrame(main_frame, text="🔍 Visualización y Operaciones", padding="10")
        panel_derecho.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        panel_derecho.columnconfigure(0, weight=1)
        panel_derecho.rowconfigure(1, weight=1)
        
        # Información de matriz seleccionada
        self.info_label = ttk.Label(panel_derecho, text="Selecciona una matriz para ver información", style='Heading.TLabel')
        self.info_label.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Área de texto para mostrar matriz
        self.texto_matriz = scrolledtext.ScrolledText(panel_derecho, height=20, width=60, font=('Courier', 10))
        self.texto_matriz.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Panel de operaciones rápidas
        ops_frame = ttk.LabelFrame(panel_derecho, text="⚡ Operaciones Rápidas", padding="5")
        ops_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Botones de operaciones
        ttk.Button(ops_frame, text="🔢 Determinante", command=self.calcular_determinante).grid(row=0, column=0, padx=5, pady=2)
        ttk.Button(ops_frame, text="↩️ Inversa", command=self.calcular_inversa).grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(ops_frame, text="🔄 Transponer", command=self.transponer_matriz).grid(row=0, column=2, padx=5, pady=2)
        
        # Barra de estado
        self.status_bar = ttk.Label(main_frame, text="✅ Listo - NumPy v" + np.__version__, relief=tk.SUNKEN)
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.actualizar_lista_matrices()
    
    def actualizar_lista_matrices(self):
        """Actualiza la lista de matrices en la interfaz."""
        self.lista_matrices.delete(0, tk.END)
        for nombre, matriz in self.matrices.items():
            info = f"{nombre} ({matriz.shape[0]}×{matriz.shape[1]})"
            self.lista_matrices.insert(tk.END, info)
    
    def seleccionar_matriz(self, event):
        """Maneja la selección de una matriz en la lista."""
        seleccion = self.lista_matrices.curselection()
        if seleccion:
            index = seleccion[0]
            nombres = list(self.matrices.keys())
            if index < len(nombres):
                nombre_matriz = nombres[index]
                self.mostrar_matriz_seleccionada(nombre_matriz)
    
    def mostrar_matriz_seleccionada(self, nombre):
        """Muestra la matriz seleccionada en el área de texto."""
        if nombre in self.matrices:
            matriz = self.matrices[nombre]
            
            # Actualizar información
            info = f"📊 {nombre} - {matriz.shape[0]}×{matriz.shape[1]} - {matriz.datos.dtype}"
            if matriz.es_cuadrada():
                info += " (Cuadrada)"
            self.info_label.config(text=info)
            
            # Mostrar matriz en el área de texto
            self.texto_matriz.delete('1.0', tk.END)
            
            # Crear representación de la matriz
            contenido = f"Matriz: {nombre}\n"
            contenido += f"Dimensiones: {matriz.shape[0]}×{matriz.shape[1]}\n"
            contenido += f"Tipo: {matriz.datos.dtype}\n"
            contenido += "="*50 + "\n\n"
            
            # Formatear la matriz para visualización
            if matriz.shape[0] <= 20 and matriz.shape[1] <= 20:  # Solo mostrar si no es muy grande
                contenido += str(matriz.datos)
            else:
                contenido += f"Matriz demasiado grande para visualizar completa.\n"
                contenido += f"Primeras 5×5 elementos:\n"
                contenido += str(matriz.datos[:5, :5])
                if matriz.shape[0] > 5 or matriz.shape[1] > 5:
                    contenido += "\n..."
            
            self.texto_matriz.insert('1.0', contenido)
    
    def nueva_matriz_dialogo(self):
        """Abre diálogo para crear nueva matriz."""
        dialogo = tk.Toplevel(self.ventana_principal)
        dialogo.title("🆕 Nueva Matriz")
        dialogo.geometry("400x500")
        dialogo.resizable(False, False)
        dialogo.transient(self.ventana_principal)
        dialogo.grab_set()
        
        # Centrar diálogo
        dialogo.geometry("+%d+%d" % (
            self.ventana_principal.winfo_rootx() + 100,
            self.ventana_principal.winfo_rooty() + 100
        ))
        
        main_frame = ttk.Frame(dialogo, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Nombre de la matriz
        ttk.Label(main_frame, text="🏷️ Nombre de la matriz:", font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        nombre_entry = ttk.Entry(main_frame, width=30)
        nombre_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Tipo de matriz
        ttk.Label(main_frame, text="📝 Tipo de matriz:", font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        tipo_var = tk.StringVar(value="manual")
        
        tipos_frame = ttk.Frame(main_frame)
        tipos_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Radiobutton(tipos_frame, text="📝 Manual", variable=tipo_var, value="manual").pack(anchor=tk.W)
        ttk.Radiobutton(tipos_frame, text="🎲 Aleatoria", variable=tipo_var, value="aleatoria").pack(anchor=tk.W)
        ttk.Radiobutton(tipos_frame, text="🔢 Ceros", variable=tipo_var, value="ceros").pack(anchor=tk.W)
        ttk.Radiobutton(tipos_frame, text="1️⃣ Unos", variable=tipo_var, value="unos").pack(anchor=tk.W)
        ttk.Radiobutton(tipos_frame, text="👁️ Identidad", variable=tipo_var, value="identidad").pack(anchor=tk.W)
        
        # Dimensiones
        dim_frame = ttk.Frame(main_frame)
        dim_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(dim_frame, text="📏 Filas:").grid(row=0, column=0, sticky=tk.W)
        filas_entry = ttk.Entry(dim_frame, width=10)
        filas_entry.grid(row=0, column=1, padx=(10, 20))
        filas_entry.insert(0, "3")
        
        ttk.Label(dim_frame, text="📐 Columnas:").grid(row=0, column=2, sticky=tk.W)
        columnas_entry = ttk.Entry(dim_frame, width=10)
        columnas_entry.grid(row=0, column=3, padx=(10, 0))
        columnas_entry.insert(0, "3")
        
        # Parámetros adicionales para matriz aleatoria
        params_frame = ttk.LabelFrame(main_frame, text="⚙️ Parámetros adicionales")
        params_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(params_frame, text="Min:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        min_entry = ttk.Entry(params_frame, width=10)
        min_entry.grid(row=0, column=1, padx=5, pady=5)
        min_entry.insert(0, "-10")
        
        ttk.Label(params_frame, text="Max:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        max_entry = ttk.Entry(params_frame, width=10)
        max_entry.grid(row=0, column=3, padx=5, pady=5)
        max_entry.insert(0, "10")
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(20, 0))
        
        def crear_matriz():
            try:
                nombre = nombre_entry.get().strip()
                if not nombre:
                    messagebox.showerror("Error", "El nombre no puede estar vacío")
                    return
                
                if nombre in self.matrices:
                    messagebox.showerror("Error", "Ya existe una matriz con ese nombre")
                    return
                
                filas = int(filas_entry.get())
                columnas = int(columnas_entry.get())
                tipo = tipo_var.get()
                
                if filas <= 0 or columnas <= 0:
                    messagebox.showerror("Error", "Las dimensiones deben ser positivas")
                    return
                
                # Crear matriz según el tipo
                if tipo == "manual":
                    self.crear_matriz_manual_dialogo(nombre, filas, columnas, dialogo)
                    return  # No cerrar aún para matriz manual
                elif tipo == "aleatoria":
                    min_val = float(min_entry.get())
                    max_val = float(max_entry.get())
                    matriz = MatrizNumPy.crear_aleatoria(filas, columnas, min_val, max_val)
                elif tipo == "ceros":
                    matriz = MatrizNumPy.crear_ceros(filas, columnas)
                elif tipo == "unos":
                    matriz = MatrizNumPy.crear_unos(filas, columnas)
                elif tipo == "identidad":
                    if filas != columnas:
                        messagebox.showerror("Error", "La matriz identidad debe ser cuadrada")
                        return
                    matriz = MatrizNumPy.crear_identidad(filas)
                
                self.matrices[nombre] = matriz
                self.actualizar_lista_matrices()
                self.historial_operaciones.append(f"Creada matriz '{nombre}' ({filas}×{columnas})")
                self.status_bar.config(text=f"✅ Matriz '{nombre}' creada exitosamente")
                dialogo.destroy()
                
            except ValueError as e:
                messagebox.showerror("Error", f"Error en los datos: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Error inesperado: {e}")
        
        ttk.Button(btn_frame, text="✅ Crear", command=crear_matriz).pack(side=tk.RIGHT, padx=(10, 0))
        ttk.Button(btn_frame, text="❌ Cancelar", command=dialogo.destroy).pack(side=tk.RIGHT)
    
    def crear_matriz_manual_dialogo(self, nombre, filas, columnas, dialogo_padre):
        """Diálogo para crear matriz manual."""
        dialogo_padre.destroy()
        
        dialogo = tk.Toplevel(self.ventana_principal)
        dialogo.title(f"📝 Matriz Manual: {nombre}")
        dialogo.geometry("600x500")
        dialogo.resizable(True, True)
        dialogo.transient(self.ventana_principal)
        dialogo.grab_set()
        
        main_frame = ttk.Frame(dialogo, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text=f"Ingresa valores para matriz {filas}×{columnas}:", 
                 font=('Arial', 12, 'bold')).pack(pady=(0, 10))
        
        # Frame para entradas
        entradas_frame = ttk.Frame(main_frame)
        entradas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Crear grid de entradas
        entradas = []
        for i in range(filas):
            fila_entradas = []
            for j in range(columnas):
                entry = ttk.Entry(entradas_frame, width=8)
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, "0")
                fila_entradas.append(entry)
            entradas.append(fila_entradas)
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(20, 0))
        
        def crear_matriz_manual():
            try:
                datos = []
                for fila in entradas:
                    fila_datos = []
                    for entry in fila:
                        valor = float(entry.get() or "0")
                        fila_datos.append(valor)
                    datos.append(fila_datos)
                
                matriz = MatrizNumPy(datos)
                self.matrices[nombre] = matriz
                self.actualizar_lista_matrices()
                self.historial_operaciones.append(f"Creada matriz manual '{nombre}' ({filas}×{columnas})")
                self.status_bar.config(text=f"✅ Matriz manual '{nombre}' creada exitosamente")
                dialogo.destroy()
                
            except ValueError as e:
                messagebox.showerror("Error", f"Error en los datos: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Error inesperado: {e}")
        
        ttk.Button(btn_frame, text="✅ Crear Matriz", command=crear_matriz_manual).pack(side=tk.RIGHT, padx=(10, 0))
        ttk.Button(btn_frame, text="❌ Cancelar", command=dialogo.destroy).pack(side=tk.RIGHT)
    
    def eliminar_matriz(self):
        """Elimina la matriz seleccionada."""
        seleccion = self.lista_matrices.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una matriz para eliminar")
            return
        
        index = seleccion[0]
        nombres = list(self.matrices.keys())
        if index < len(nombres):
            nombre = nombres[index]
            
            respuesta = messagebox.askyesno("Confirmar", f"¿Eliminar matriz '{nombre}'?")
            if respuesta:
                del self.matrices[nombre]
                self.actualizar_lista_matrices()
                self.texto_matriz.delete('1.0', tk.END)
                self.info_label.config(text="Selecciona una matriz para ver información")
                self.historial_operaciones.append(f"Eliminada matriz '{nombre}'")
                self.status_bar.config(text=f"✅ Matriz '{nombre}' eliminada")
    
    def ver_matriz(self):
        """Muestra detalles de la matriz seleccionada."""
        seleccion = self.lista_matrices.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una matriz para ver")
            return
        
        index = seleccion[0]
        nombres = list(self.matrices.keys())
        if index < len(nombres):
            nombre = nombres[index]
            self.mostrar_matriz_seleccionada(nombre)
    
    def obtener_matriz_seleccionada(self):
        """Obtiene el nombre de la matriz seleccionada."""
        seleccion = self.lista_matrices.curselection()
        if not seleccion:
            return None
        
        index = seleccion[0]
        nombres = list(self.matrices.keys())
        if index < len(nombres):
            return nombres[index]
        return None
    
    def calcular_determinante(self):
        """Calcula el determinante de la matriz seleccionada."""
        nombre = self.obtener_matriz_seleccionada()
        if not nombre:
            messagebox.showwarning("Advertencia", "Selecciona una matriz")
            return
        
        matriz = self.matrices[nombre]
        if not matriz.es_cuadrada():
            messagebox.showerror("Error", "La matriz debe ser cuadrada para calcular el determinante")
            return
        
        try:
            det = matriz.determinante()
            messagebox.showinfo("Determinante", f"Determinante de '{nombre}': {det:.6f}")
            self.historial_operaciones.append(f"Calculado determinante de '{nombre}': {det:.6f}")
            self.status_bar.config(text=f"✅ Determinante calculado: {det:.6f}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular determinante: {e}")
    
    def calcular_inversa(self):
        """Calcula la inversa de la matriz seleccionada."""
        nombre = self.obtener_matriz_seleccionada()
        if not nombre:
            messagebox.showwarning("Advertencia", "Selecciona una matriz")
            return
        
        matriz = self.matrices[nombre]
        if not matriz.es_cuadrada():
            messagebox.showerror("Error", "La matriz debe ser cuadrada para calcular la inversa")
            return
        
        try:
            # Pedir nombre para la inversa
            nombre_inversa = tk.simpledialog.askstring("Nombre", f"Nombre para la inversa de '{nombre}':")
            if not nombre_inversa:
                nombre_inversa = f"{nombre}_inv"
            
            if nombre_inversa in self.matrices:
                messagebox.showerror("Error", "Ya existe una matriz con ese nombre")
                return
            
            inversa = matriz.inversa()
            self.matrices[nombre_inversa] = inversa
            self.actualizar_lista_matrices()
            
            messagebox.showinfo("Inversa", f"Inversa calculada y guardada como '{nombre_inversa}'")
            self.historial_operaciones.append(f"Calculada inversa de '{nombre}' → '{nombre_inversa}'")
            self.status_bar.config(text=f"✅ Inversa calculada: '{nombre_inversa}'")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular inversa: {e}")
    
    def transponer_matriz(self):
        """Transpone la matriz seleccionada."""
        nombre = self.obtener_matriz_seleccionada()
        if not nombre:
            messagebox.showwarning("Advertencia", "Selecciona una matriz")
            return
        
        try:
            # Pedir nombre para la transpuesta
            nombre_transpuesta = tk.simpledialog.askstring("Nombre", f"Nombre para la transpuesta de '{nombre}':")
            if not nombre_transpuesta:
                nombre_transpuesta = f"{nombre}_T"
            
            if nombre_transpuesta in self.matrices:
                messagebox.showerror("Error", "Ya existe una matriz con ese nombre")
                return
            
            matriz = self.matrices[nombre]
            transpuesta = matriz.transponer()
            self.matrices[nombre_transpuesta] = transpuesta
            self.actualizar_lista_matrices()
            
            messagebox.showinfo("Transposición", f"Transpuesta calculada y guardada como '{nombre_transpuesta}'")
            self.historial_operaciones.append(f"Transpuesta de '{nombre}' → '{nombre_transpuesta}'")
            self.status_bar.config(text=f"✅ Transpuesta calculada: '{nombre_transpuesta}'")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al transponer: {e}")
    
    def operacion_matrices(self, operacion):
        """Realiza operaciones entre dos matrices."""
        if len(self.matrices) < 2:
            messagebox.showwarning("Advertencia", "Se necesitan al menos 2 matrices")
            return
        
        # Crear diálogo de selección
        dialogo = tk.Toplevel(self.ventana_principal)
        dialogo.title(f"🧮 {operacion.capitalize()}")
        dialogo.geometry("400x300")
        dialogo.resizable(False, False)
        dialogo.transient(self.ventana_principal)
        dialogo.grab_set()
        
        main_frame = ttk.Frame(dialogo, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Selección de matrices
        ttk.Label(main_frame, text="Primera matriz:", font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        matriz1_var = tk.StringVar()
        combo1 = ttk.Combobox(main_frame, textvariable=matriz1_var, state="readonly", width=30)
        combo1['values'] = list(self.matrices.keys())
        combo1.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(main_frame, text="Segunda matriz:", font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        matriz2_var = tk.StringVar()
        combo2 = ttk.Combobox(main_frame, textvariable=matriz2_var, state="readonly", width=30)
        combo2['values'] = list(self.matrices.keys())
        combo2.pack(fill=tk.X, pady=(0, 15))
        
        # Nombre resultado
        ttk.Label(main_frame, text="Nombre del resultado:", font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        resultado_entry = ttk.Entry(main_frame, width=30)
        resultado_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(20, 0))
        
        def realizar_operacion():
            try:
                nombre1 = matriz1_var.get()
                nombre2 = matriz2_var.get()
                nombre_resultado = resultado_entry.get().strip()
                
                if not nombre1 or not nombre2:
                    messagebox.showerror("Error", "Selecciona ambas matrices")
                    return
                
                if not nombre_resultado:
                    nombre_resultado = f"{nombre1}_{operacion}_{nombre2}"
                
                if nombre_resultado in self.matrices:
                    messagebox.showerror("Error", "Ya existe una matriz con ese nombre")
                    return
                
                matriz1 = self.matrices[nombre1]
                matriz2 = self.matrices[nombre2]
                
                if operacion == "suma":
                    resultado = matriz1 + matriz2
                elif operacion == "resta":
                    resultado = matriz1 - matriz2
                elif operacion == "multiplicacion":
                    resultado = matriz1 @ matriz2
                
                self.matrices[nombre_resultado] = resultado
                self.actualizar_lista_matrices()
                
                messagebox.showinfo("Éxito", f"{operacion.capitalize()} completada: '{nombre_resultado}'")
                self.historial_operaciones.append(f"{operacion.capitalize()}: {nombre_resultado} = {nombre1} {'+' if operacion=='suma' else '-' if operacion=='resta' else '×'} {nombre2}")
                self.status_bar.config(text=f"✅ {operacion.capitalize()} completada: '{nombre_resultado}'")
                dialogo.destroy()
                
            except Exception as e:
                messagebox.showerror("Error", f"Error en {operacion}: {e}")
        
        ttk.Button(btn_frame, text=f"✅ {operacion.capitalize()}", command=realizar_operacion).pack(side=tk.RIGHT, padx=(10, 0))
        ttk.Button(btn_frame, text="❌ Cancelar", command=dialogo.destroy).pack(side=tk.RIGHT)
    
    def cargar_csv(self):
        """Carga matriz desde archivo CSV."""
        archivo = filedialog.askopenfilename(
            title="Cargar matriz desde CSV",
            filetypes=[("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")]
        )
        
        if archivo:
            try:
                nombre = tk.simpledialog.askstring("Nombre", "Nombre para la matriz cargada:")
                if not nombre:
                    return
                
                if nombre in self.matrices:
                    messagebox.showerror("Error", "Ya existe una matriz con ese nombre")
                    return
                
                datos = np.loadtxt(archivo, delimiter=',')
                matriz = MatrizNumPy(datos)
                self.matrices[nombre] = matriz
                self.actualizar_lista_matrices()
                
                messagebox.showinfo("Éxito", f"Matriz '{nombre}' cargada exitosamente")
                self.historial_operaciones.append(f"Cargada matriz '{nombre}' desde: {archivo}")
                self.status_bar.config(text=f"✅ Matriz '{nombre}' cargada desde CSV")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar archivo: {e}")
    
    def guardar_csv(self):
        """Guarda matriz seleccionada como CSV."""
        nombre = self.obtener_matriz_seleccionada()
        if not nombre:
            messagebox.showwarning("Advertencia", "Selecciona una matriz para guardar")
            return
        
        archivo = filedialog.asksaveasfilename(
            title="Guardar matriz como CSV",
            defaultextension=".csv",
            filetypes=[("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")],
            initialname=f"{nombre}.csv"
        )
        
        if archivo:
            try:
                matriz = self.matrices[nombre]
                np.savetxt(archivo, matriz.datos, delimiter=',', fmt='%.6f')
                
                messagebox.showinfo("Éxito", f"Matriz '{nombre}' guardada exitosamente")
                self.historial_operaciones.append(f"Guardada matriz '{nombre}' en: {archivo}")
                self.status_bar.config(text=f"✅ Matriz '{nombre}' guardada como CSV")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar archivo: {e}")
    
    def mostrar_ayuda(self):
        """Muestra la ayuda del programa."""
        ayuda_texto = """
🚀 GENERADOR DE MATRICES CON NUMPY - AYUDA

📚 FUNCIONALIDADES PRINCIPALES:

🏗️ CREACIÓN DE MATRICES:
• Manual: Ingresa valores uno por uno
• Aleatoria: Valores aleatorios en rango especificado
• Especiales: Ceros, unos, identidad

🧮 OPERACIONES:
• Suma, resta, multiplicación de matrices
• Transposición
• Determinante e inversa
• Eigenvalores

📊 VISUALIZACIÓN:
• Heatmaps de matrices
• Gráficos de eigenvalores
• Histogramas de valores

💾 ARCHIVOS:
• Cargar matrices desde CSV
• Guardar matrices como CSV

🎯 CONSEJOS:
• Para operaciones como determinante e inversa, usa matrices cuadradas
• Las visualizaciones requieren matplotlib
• Los heatmaps son útiles para matrices grandes

🚀 ¡NumPy acelera los cálculos hasta 1000x vs Python puro!
        """
        
        dialogo = tk.Toplevel(self.ventana_principal)
        dialogo.title("❓ Ayuda")
        dialogo.geometry("600x500")
        dialogo.resizable(True, True)
        
        texto = scrolledtext.ScrolledText(dialogo, wrap=tk.WORD, font=('Arial', 10))
        texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        texto.insert('1.0', ayuda_texto)
        texto.config(state=tk.DISABLED)
    
    def mostrar_acerca_de(self):
        """Muestra información sobre el programa."""
        mensaje = f"""
🚀 Generador de Matrices con NumPy
Versión 2.0.0 (NumPy Edition)

🔬 Desarrollado por: Nicolas
📅 Año: 2024
🧮 Powered by NumPy v{np.__version__}

💡 Interfaz gráfica avanzada para operaciones 
   con matrices usando NumPy y tkinter.

🌟 Capacidades científicas profesionales
   de álgebra lineal y visualización.

❤️ ¡Gracias por usar nuestro software!
        """
        
        messagebox.showinfo("ℹ️ Acerca de", mensaje)


# Importar simpledialog para algunas funciones
import tkinter.simpledialog
