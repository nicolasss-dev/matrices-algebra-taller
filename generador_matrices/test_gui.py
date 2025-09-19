#!/usr/bin/env python3
"""
Prueba directa de la interfaz gráfica
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from interfaces.grafica import InterfazGrafica
    
    print("🧪 PRUEBA DE INTERFAZ GRÁFICA")
    print("=" * 50)
    
    gui = InterfazGrafica()
    
    # Crear algunas matrices de prueba
    print("Creando matrices de prueba...")
    
    from src.matriz import Matriz
    
    # Matriz A
    matriz_a = Matriz(2, 2)
    matriz_a.llenar_manual([[1, 2], [3, 4]])
    gui.matrices["Matriz_A"] = matriz_a
    gui.contador_matrices += 1
    
    # Matriz B  
    matriz_b = Matriz(2, 2)
    matriz_b.llenar_manual([[5, 6], [7, 8]])
    gui.matrices["Matriz_B"] = matriz_b
    gui.contador_matrices += 1
    
    # Matriz C (3x3)
    matriz_c = Matriz(3, 3)
    matriz_c.llenar_manual([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    gui.matrices["Identidad_3x3"] = matriz_c
    gui.contador_matrices += 1
    
    print(f"✅ Creadas {len(gui.matrices)} matrices de prueba:")
    for nombre, matriz in gui.matrices.items():
        print(f"  - {nombre}: {matriz.filas}×{matriz.columnas}")
    
    print("\n🚀 Iniciando interfaz gráfica...")
    print("📝 Nota: Ahora las operaciones muestran el resultado automáticamente!")
    
    gui.iniciar()
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nUsando versión básica...")
    
    import tkinter as tk
    from tkinter import messagebox
    
    root = tk.Tk()
    root.title("Generador de Matrices - Prueba")
    root.geometry("400x200")
    
    label = tk.Label(root, text="Generador de Matrices\n(Versión de Prueba)", 
                    font=("Arial", 14, "bold"))
    label.pack(pady=20)
    
    tk.Label(root, text="Si ves esta ventana, tkinter funciona correctamente.").pack(pady=10)
    
    def cerrar():
        messagebox.showinfo("Info", "¡La interfaz gráfica básica funciona!")
        root.quit()
    
    tk.Button(root, text="Cerrar", command=cerrar, pady=5).pack(pady=20)
    
    root.mainloop()
