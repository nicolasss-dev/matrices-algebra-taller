"""
Pruebas unitarias para operaciones con matrices
==============================================

Tests para verificar el correcto funcionamiento de todas las
operaciones matemáticas con matrices.

Autor: Nicolas
"""

import unittest
import sys
import os
from fractions import Fraction

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.matriz import Matriz
from src.operaciones import *


class TestOperaciones(unittest.TestCase):
    """Pruebas unitarias para operaciones con matrices."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        # Matrices de prueba
        self.matriz_2x2_a = Matriz(2, 2)
        self.matriz_2x2_a.llenar_manual([[1, 2], [3, 4]])
        
        self.matriz_2x2_b = Matriz(2, 2)
        self.matriz_2x2_b.llenar_manual([[5, 6], [7, 8]])
        
        self.matriz_2x3 = Matriz(2, 3)
        self.matriz_2x3.llenar_manual([[1, 2, 3], [4, 5, 6]])
        
        self.matriz_3x2 = Matriz(3, 2)
        self.matriz_3x2.llenar_manual([[1, 2], [3, 4], [5, 6]])
    
    def test_sumar_matrices(self):
        """Testa la suma de matrices."""
        resultado = sumar_matrices(self.matriz_2x2_a, self.matriz_2x2_b)
        
        self.assertEqual(resultado.obtener_elemento(0, 0), 6)  # 1 + 5
        self.assertEqual(resultado.obtener_elemento(0, 1), 8)  # 2 + 6
        self.assertEqual(resultado.obtener_elemento(1, 0), 10) # 3 + 7
        self.assertEqual(resultado.obtener_elemento(1, 1), 12) # 4 + 8
    
    def test_sumar_matrices_incompatibles(self):
        """Testa suma con matrices de dimensiones incompatibles."""
        with self.assertRaises(ValueError):
            sumar_matrices(self.matriz_2x2_a, self.matriz_2x3)
    
    def test_restar_matrices(self):
        """Testa la resta de matrices."""
        resultado = restar_matrices(self.matriz_2x2_b, self.matriz_2x2_a)
        
        self.assertEqual(resultado.obtener_elemento(0, 0), 4)  # 5 - 1
        self.assertEqual(resultado.obtener_elemento(0, 1), 4)  # 6 - 2
        self.assertEqual(resultado.obtener_elemento(1, 0), 4)  # 7 - 3
        self.assertEqual(resultado.obtener_elemento(1, 1), 4)  # 8 - 4
    
    def test_multiplicar_matrices(self):
        """Testa la multiplicación de matrices."""
        resultado = multiplicar_matrices(self.matriz_2x3, self.matriz_3x2)
        
        # Resultado debe ser 2x2
        self.assertEqual(resultado.filas, 2)
        self.assertEqual(resultado.columnas, 2)
        
        # Verificar elementos: [1,2,3] × [[1,2],[3,4],[5,6]]
        self.assertEqual(resultado.obtener_elemento(0, 0), 22)  # 1×1 + 2×3 + 3×5
        self.assertEqual(resultado.obtener_elemento(0, 1), 28)  # 1×2 + 2×4 + 3×6
        self.assertEqual(resultado.obtener_elemento(1, 0), 49)  # 4×1 + 5×3 + 6×5
        self.assertEqual(resultado.obtener_elemento(1, 1), 64)  # 4×2 + 5×4 + 6×6
    
    def test_multiplicar_matrices_incompatibles(self):
        """Testa multiplicación con matrices incompatibles."""
        with self.assertRaises(ValueError):
            multiplicar_matrices(self.matriz_2x2_a, self.matriz_2x3)
    
    def test_multiplicar_por_escalar(self):
        """Testa la multiplicación por escalar."""
        resultado = multiplicar_por_escalar(self.matriz_2x2_a, 3)
        
        self.assertEqual(resultado.obtener_elemento(0, 0), 3)   # 1 × 3
        self.assertEqual(resultado.obtener_elemento(0, 1), 6)   # 2 × 3
        self.assertEqual(resultado.obtener_elemento(1, 0), 9)   # 3 × 3
        self.assertEqual(resultado.obtener_elemento(1, 1), 12)  # 4 × 3
    
    def test_multiplicar_por_fraccion(self):
        """Testa la multiplicación por fracción."""
        resultado = multiplicar_por_escalar(self.matriz_2x2_a, Fraction(1, 2))
        
        self.assertEqual(resultado.obtener_elemento(0, 0), Fraction(1, 2))
        self.assertEqual(resultado.obtener_elemento(0, 1), Fraction(1, 1))
        self.assertEqual(resultado.obtener_elemento(1, 0), Fraction(3, 2))
        self.assertEqual(resultado.obtener_elemento(1, 1), Fraction(2, 1))
    
    def test_potencia_matriz(self):
        """Testa la potenciación de matrices."""
        # Potencia 0 (matriz identidad)
        resultado = potencia_matriz(self.matriz_2x2_a, 0)
        self.assertEqual(resultado.obtener_elemento(0, 0), 1)
        self.assertEqual(resultado.obtener_elemento(0, 1), 0)
        self.assertEqual(resultado.obtener_elemento(1, 0), 0)
        self.assertEqual(resultado.obtener_elemento(1, 1), 1)
        
        # Potencia 1 (matriz original)
        resultado = potencia_matriz(self.matriz_2x2_a, 1)
        self.assertTrue(son_matrices_iguales(resultado, self.matriz_2x2_a))
        
        # Potencia 2
        resultado = potencia_matriz(self.matriz_2x2_a, 2)
        esperado = multiplicar_matrices(self.matriz_2x2_a, self.matriz_2x2_a)
        self.assertTrue(son_matrices_iguales(resultado, esperado))
    
    def test_potencia_matriz_no_cuadrada(self):
        """Testa potencia con matriz no cuadrada."""
        with self.assertRaises(ValueError):
            potencia_matriz(self.matriz_2x3, 2)
    
    def test_crear_matriz_identidad(self):
        """Testa la creación de matriz identidad."""
        identidad = crear_matriz_identidad(3)
        
        # Verificar dimensiones
        self.assertEqual(identidad.filas, 3)
        self.assertEqual(identidad.columnas, 3)
        
        # Verificar elementos diagonales
        for i in range(3):
            for j in range(3):
                if i == j:
                    self.assertEqual(identidad.obtener_elemento(i, j), 1)
                else:
                    self.assertEqual(identidad.obtener_elemento(i, j), 0)
    
    def test_crear_matriz_ceros(self):
        """Testa la creación de matriz de ceros."""
        ceros = crear_matriz_ceros(2, 3)
        
        self.assertEqual(ceros.filas, 2)
        self.assertEqual(ceros.columnas, 3)
        
        for i in range(2):
            for j in range(3):
                self.assertEqual(ceros.obtener_elemento(i, j), 0)
    
    def test_crear_matriz_unos(self):
        """Testa la creación de matriz de unos."""
        unos = crear_matriz_unos(2, 2)
        
        for i in range(2):
            for j in range(2):
                self.assertEqual(unos.obtener_elemento(i, j), 1)
    
    def test_son_matrices_iguales(self):
        """Testa la comparación de matrices."""
        # Matrices iguales
        otra_matriz = Matriz(2, 2)
        otra_matriz.llenar_manual([[1, 2], [3, 4]])
        self.assertTrue(son_matrices_iguales(self.matriz_2x2_a, otra_matriz))
        
        # Matrices diferentes
        self.assertFalse(son_matrices_iguales(self.matriz_2x2_a, self.matriz_2x2_b))
        
        # Dimensiones diferentes
        self.assertFalse(son_matrices_iguales(self.matriz_2x2_a, self.matriz_2x3))
    
    def test_son_matrices_iguales_con_tolerancia(self):
        """Testa comparación con tolerancia para flotantes."""
        matriz_float = Matriz(2, 2)
        matriz_float.llenar_manual([[1.0000001, 2], [3, 4]])
        
        # Con tolerancia por defecto debería ser igual
        self.assertTrue(son_matrices_iguales(self.matriz_2x2_a, matriz_float))
        
        # Con tolerancia muy pequeña debería ser diferente
        self.assertFalse(son_matrices_iguales(self.matriz_2x2_a, matriz_float, 1e-10))


if __name__ == '__main__':
    unittest.main()
