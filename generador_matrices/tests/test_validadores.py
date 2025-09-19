"""
Pruebas unitarias para validadores
=================================

Tests para verificar el correcto funcionamiento de todas las
funciones de validación.

Autor: Nicolas
"""

import unittest
import sys
import os
from fractions import Fraction

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.validadores import *


class TestValidadores(unittest.TestCase):
    """Pruebas unitarias para validadores."""
    
    def test_validar_dimensiones_correctas(self):
        """Testa validación de dimensiones correctas."""
        # Estas no deberían lanzar excepciones
        validar_dimensiones(1, 1)
        validar_dimensiones(5, 10)
        validar_dimensiones(100, 100)
    
    def test_validar_dimensiones_incorrectas(self):
        """Testa validación de dimensiones incorrectas."""
        with self.assertRaises(ValueError):
            validar_dimensiones(0, 5)
        
        with self.assertRaises(ValueError):
            validar_dimensiones(5, 0)
        
        with self.assertRaises(ValueError):
            validar_dimensiones(-1, 5)
        
        with self.assertRaises(ValueError):
            validar_dimensiones(101, 5)
        
        with self.assertRaises(ValueError):
            validar_dimensiones("5", 5)
    
    def test_validar_numero_enteros(self):
        """Testa validación de números enteros."""
        self.assertEqual(validar_numero(5), 5)
        self.assertEqual(validar_numero("10"), 10)
        self.assertEqual(validar_numero("-3"), -3)
        self.assertEqual(validar_numero("0"), 0)
    
    def test_validar_numero_decimales(self):
        """Testa validación de números decimales."""
        self.assertEqual(validar_numero(5.5), 5.5)
        self.assertEqual(validar_numero("3.14"), 3.14)
        self.assertEqual(validar_numero("-2.5"), -2.5)
    
    def test_validar_numero_fracciones(self):
        """Testa validación de fracciones."""
        self.assertEqual(validar_numero("1/2"), Fraction(1, 2))
        self.assertEqual(validar_numero("3/4"), Fraction(3, 4))
        self.assertEqual(validar_numero("-2/3"), Fraction(-2, 3))
    
    def test_validar_numero_invalidos(self):
        """Testa rechazo de números inválidos."""
        with self.assertRaises(ValueError):
            validar_numero("abc")
        
        with self.assertRaises(ValueError):
            validar_numero("")
        
        with self.assertRaises(ValueError):
            validar_numero("1/0")  # División por cero
        
        with self.assertRaises(ValueError):
            validar_numero(None)
    
    def test_validar_matriz_datos_correctos(self):
        """Testa validación de datos correctos para matriz."""
        datos = [[1, 2, 3], [4, 5, 6]]
        # No debería lanzar excepción
        validar_matriz_datos(datos, 2, 3)
    
    def test_validar_matriz_datos_incorrectos(self):
        """Testa rechazo de datos incorrectos."""
        # Número incorrecto de filas
        with self.assertRaises(ValueError):
            validar_matriz_datos([[1, 2]], 2, 2)
        
        # Número incorrecto de columnas
        with self.assertRaises(ValueError):
            validar_matriz_datos([[1, 2, 3], [4, 5]], 2, 3)
        
        # No es una lista
        with self.assertRaises(ValueError):
            validar_matriz_datos("not a list", 2, 2)
        
        # Fila no es lista
        with self.assertRaises(ValueError):
            validar_matriz_datos([1, 2], 2, 1)
        
        # Elemento inválido
        with self.assertRaises(ValueError):
            validar_matriz_datos([[1, "abc"]], 1, 2)
    
    def test_validar_entrada_entero(self):
        """Testa validación de enteros."""
        self.assertEqual(validar_entrada_entero("5"), 5)
        self.assertEqual(validar_entrada_entero(10), 10)
        self.assertEqual(validar_entrada_entero("-3"), -3)
    
    def test_validar_entrada_entero_con_rango(self):
        """Testa validación de enteros con rango."""
        self.assertEqual(validar_entrada_entero("5", 1, 10), 5)
        
        with self.assertRaises(ValueError):
            validar_entrada_entero("0", 1, 10)  # Muy pequeño
        
        with self.assertRaises(ValueError):
            validar_entrada_entero("15", 1, 10)  # Muy grande
    
    def test_validar_entrada_entero_invalido(self):
        """Testa rechazo de enteros inválidos."""
        with self.assertRaises(ValueError):
            validar_entrada_entero("3.5")
        
        with self.assertRaises(ValueError):
            validar_entrada_entero("abc")
        
        with self.assertRaises(ValueError):
            validar_entrada_entero("")
    
    def test_validar_opcion_menu(self):
        """Testa validación de opciones de menú."""
        opciones = ["1", "2", "3", "salir"]
        
        self.assertEqual(validar_opcion_menu("1", opciones), "1")
        self.assertEqual(validar_opcion_menu("SALIR", opciones), "salir")
        self.assertEqual(validar_opcion_menu(" 2 ", opciones), "2")
    
    def test_validar_opcion_menu_invalida(self):
        """Testa rechazo de opciones inválidas."""
        opciones = ["1", "2", "3"]
        
        with self.assertRaises(ValueError):
            validar_opcion_menu("4", opciones)
        
        with self.assertRaises(ValueError):
            validar_opcion_menu("abc", opciones)
    
    def test_es_numero_valido(self):
        """Testa verificación de números válidos."""
        self.assertTrue(es_numero_valido("5"))
        self.assertTrue(es_numero_valido("3.14"))
        self.assertTrue(es_numero_valido("-2"))
        self.assertTrue(es_numero_valido("1/2"))
        
        self.assertFalse(es_numero_valido("abc"))
        self.assertFalse(es_numero_valido(""))
        self.assertFalse(es_numero_valido("1/0"))
        self.assertFalse(es_numero_valido(None))
    
    def test_validar_rango_numerico(self):
        """Testa validación de rangos numéricos."""
        # Rango válido
        validar_rango_numerico(1, 10)
        validar_rango_numerico(-5, 5)
        validar_rango_numerico("1", "10")
        
        # Rango inválido
        with self.assertRaises(ValueError):
            validar_rango_numerico(10, 1)  # min >= max
        
        with self.assertRaises(ValueError):
            validar_rango_numerico(5, 5)   # min == max
        
        with self.assertRaises(ValueError):
            validar_rango_numerico("abc", 10)  # min inválido


if __name__ == '__main__':
    unittest.main()
