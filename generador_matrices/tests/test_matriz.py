"""
Pruebas unitarias para la clase Matriz
======================================

Tests para verificar el correcto funcionamiento de la clase Matriz
y todos sus métodos.

Autor: Nicolas
"""

import unittest
import sys
import os
from fractions import Fraction

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.matriz import Matriz


class TestMatriz(unittest.TestCase):
    """Pruebas unitarias para la clase Matriz."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.matriz_2x2 = Matriz(2, 2)
        self.matriz_3x3 = Matriz(3, 3)
        self.matriz_2x3 = Matriz(2, 3)
    
    def test_creacion_matriz(self):
        """Testa la creación correcta de matrices."""
        # Test dimensiones correctas
        matriz = Matriz(3, 4)
        self.assertEqual(matriz.filas, 3)
        self.assertEqual(matriz.columnas, 4)
        self.assertEqual(len(matriz.datos), 3)
        self.assertEqual(len(matriz.datos[0]), 4)
        
        # Test inicialización con ceros
        for fila in matriz.datos:
            for elemento in fila:
                self.assertEqual(elemento, 0)
    
    def test_dimensiones_invalidas(self):
        """Testa que se rechacen dimensiones inválidas."""
        with self.assertRaises(ValueError):
            Matriz(0, 5)
        
        with self.assertRaises(ValueError):
            Matriz(5, 0)
        
        with self.assertRaises(ValueError):
            Matriz(-1, 5)
        
        with self.assertRaises(ValueError):
            Matriz(101, 5)  # Mayor al límite
    
    def test_llenar_manual(self):
        """Testa el llenado manual de matrices."""
        datos = [[1, 2], [3, 4]]
        self.matriz_2x2.llenar_manual(datos)
        
        self.assertEqual(self.matriz_2x2.datos[0][0], 1)
        self.assertEqual(self.matriz_2x2.datos[0][1], 2)
        self.assertEqual(self.matriz_2x2.datos[1][0], 3)
        self.assertEqual(self.matriz_2x2.datos[1][1], 4)
    
    def test_llenar_manual_con_fracciones(self):
        """Testa el llenado con fracciones."""
        datos = [["1/2", "3/4"], ["2/3", 1]]
        self.matriz_2x2.llenar_manual(datos)
        
        self.assertEqual(self.matriz_2x2.datos[0][0], Fraction(1, 2))
        self.assertEqual(self.matriz_2x2.datos[0][1], Fraction(3, 4))
        self.assertEqual(self.matriz_2x2.datos[1][0], Fraction(2, 3))
        self.assertEqual(self.matriz_2x2.datos[1][1], 1)
    
    def test_llenar_datos_incorrectos(self):
        """Testa que se rechacen datos incorrectos."""
        # Dimensiones incorrectas
        with self.assertRaises(ValueError):
            self.matriz_2x2.llenar_manual([[1, 2, 3], [4, 5, 6]])  # 3 columnas en vez de 2
        
        with self.assertRaises(ValueError):
            self.matriz_2x2.llenar_manual([[1, 2]])  # Solo 1 fila en vez de 2
        
        # Datos no numéricos
        with self.assertRaises(ValueError):
            self.matriz_2x2.llenar_manual([[1, 2], ["abc", 4]])
    
    def test_obtener_elemento(self):
        """Testa la obtención de elementos específicos."""
        datos = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.matriz_3x3.llenar_manual(datos)
        
        self.assertEqual(self.matriz_3x3.obtener_elemento(0, 0), 1)
        self.assertEqual(self.matriz_3x3.obtener_elemento(1, 2), 6)
        self.assertEqual(self.matriz_3x3.obtener_elemento(2, 1), 8)
    
    def test_obtener_elemento_fuera_rango(self):
        """Testa que se lance excepción para índices fuera de rango."""
        with self.assertRaises(IndexError):
            self.matriz_2x2.obtener_elemento(2, 0)  # Fila fuera de rango
        
        with self.assertRaises(IndexError):
            self.matriz_2x2.obtener_elemento(0, 2)  # Columna fuera de rango
        
        with self.assertRaises(IndexError):
            self.matriz_2x2.obtener_elemento(-1, 0)  # Índice negativo
    
    def test_establecer_elemento(self):
        """Testa el establecimiento de elementos específicos."""
        self.matriz_2x2.establecer_elemento(0, 0, 10)
        self.matriz_2x2.establecer_elemento(1, 1, Fraction(1, 2))
        
        self.assertEqual(self.matriz_2x2.obtener_elemento(0, 0), 10)
        self.assertEqual(self.matriz_2x2.obtener_elemento(1, 1), Fraction(1, 2))
    
    def test_establecer_elemento_fuera_rango(self):
        """Testa que se lance excepción al establecer fuera de rango."""
        with self.assertRaises(IndexError):
            self.matriz_2x2.establecer_elemento(2, 0, 5)
        
        with self.assertRaises(IndexError):
            self.matriz_2x2.establecer_elemento(0, 2, 5)
    
    def test_es_cuadrada(self):
        """Testa la verificación de matrices cuadradas."""
        self.assertTrue(self.matriz_2x2.es_cuadrada())
        self.assertTrue(self.matriz_3x3.es_cuadrada())
        self.assertFalse(self.matriz_2x3.es_cuadrada())
    
    def test_transponer(self):
        """Testa la transposición de matrices."""
        datos = [[1, 2, 3], [4, 5, 6]]
        self.matriz_2x3.llenar_manual(datos)
        
        transpuesta = self.matriz_2x3.transponer()
        
        # Verificar dimensiones
        self.assertEqual(transpuesta.filas, 3)
        self.assertEqual(transpuesta.columnas, 2)
        
        # Verificar elementos
        self.assertEqual(transpuesta.obtener_elemento(0, 0), 1)
        self.assertEqual(transpuesta.obtener_elemento(1, 0), 2)
        self.assertEqual(transpuesta.obtener_elemento(2, 0), 3)
        self.assertEqual(transpuesta.obtener_elemento(0, 1), 4)
        self.assertEqual(transpuesta.obtener_elemento(1, 1), 5)
        self.assertEqual(transpuesta.obtener_elemento(2, 1), 6)
    
    def test_copiar(self):
        """Testa la copia de matrices."""
        datos = [[1, 2], [3, 4]]
        self.matriz_2x2.llenar_manual(datos)
        
        copia = self.matriz_2x2.copiar()
        
        # Verificar que son matrices separadas
        self.assertIsNot(copia, self.matriz_2x2)
        self.assertIsNot(copia.datos, self.matriz_2x2.datos)
        
        # Verificar que tienen los mismos elementos
        for i in range(2):
            for j in range(2):
                self.assertEqual(
                    copia.obtener_elemento(i, j),
                    self.matriz_2x2.obtener_elemento(i, j)
                )
    
    def test_son_dimensiones_compatibles(self):
        """Testa la verificación de compatibilidad de dimensiones."""
        otra_matriz_2x2 = Matriz(2, 2)
        otra_matriz_3x3 = Matriz(3, 3)
        
        self.assertTrue(self.matriz_2x2.son_dimensiones_compatibles(otra_matriz_2x2))
        self.assertTrue(self.matriz_3x3.son_dimensiones_compatibles(otra_matriz_3x3))
        self.assertFalse(self.matriz_2x2.son_dimensiones_compatibles(self.matriz_3x3))
        self.assertFalse(self.matriz_2x2.son_dimensiones_compatibles(self.matriz_2x3))
    
    def test_llenar_aleatorio(self):
        """Testa el llenado aleatorio."""
        self.matriz_3x3.llenar_aleatorio(-5, 5)
        
        # Verificar que todos los elementos están en el rango
        for fila in self.matriz_3x3.datos:
            for elemento in fila:
                self.assertGreaterEqual(elemento, -5)
                self.assertLessEqual(elemento, 5)
                self.assertIsInstance(elemento, int)
    
    def test_str_representation(self):
        """Testa la representación en string."""
        datos = [[1, 2], [3, 4]]
        self.matriz_2x2.llenar_manual(datos)
        
        str_repr = str(self.matriz_2x2)
        
        # Verificar que contiene los elementos
        self.assertIn("1", str_repr)
        self.assertIn("2", str_repr)
        self.assertIn("3", str_repr)
        self.assertIn("4", str_repr)
        self.assertIn("[", str_repr)
        self.assertIn("]", str_repr)
    
    def test_repr_representation(self):
        """Testa la representación técnica."""
        repr_str = repr(self.matriz_2x2)
        self.assertEqual(repr_str, "Matriz(2x2)")
        
        repr_str = repr(self.matriz_2x3)
        self.assertEqual(repr_str, "Matriz(2x3)")


if __name__ == '__main__':
    unittest.main()
