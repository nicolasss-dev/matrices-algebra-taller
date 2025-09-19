"""
Clase principal Matriz
=====================

Implementación de la clase Matriz con todas sus operaciones básicas.
Maneja matrices de números enteros, decimales y fracciones.

Autor: Nicolas
"""

from fractions import Fraction
from .validadores import validar_dimensiones, validar_numero, validar_matriz_datos
from .utilidades import formatear_numero


class Matriz:
    """
    Clase que representa una matriz matemática.
    
    Atributos:
        filas (int): Número de filas de la matriz
        columnas (int): Número de columnas de la matriz
        datos (list): Lista de listas que contiene los elementos de la matriz
    """
    
    def __init__(self, filas, columnas):
        """
        Inicializa una nueva matriz con las dimensiones especificadas.
        
        Args:
            filas (int): Número de filas
            columnas (int): Número de columnas
            
        Raises:
            ValueError: Si las dimensiones no son válidas
        """
        validar_dimensiones(filas, columnas)
        
        self.filas = filas
        self.columnas = columnas
        self.datos = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    
    def llenar_manual(self, datos):
        """
        Llena la matriz con datos proporcionados manualmente.
        
        Args:
            datos (list): Lista de listas con los elementos de la matriz
            
        Raises:
            ValueError: Si los datos no son válidos para las dimensiones de la matriz
        """
        validar_matriz_datos(datos, self.filas, self.columnas)
        
        for i in range(self.filas):
            for j in range(self.columnas):
                valor = datos[i][j]
                if isinstance(valor, str) and '/' in valor:
                    self.datos[i][j] = Fraction(valor)
                else:
                    self.datos[i][j] = validar_numero(valor)
    
    
    def llenar_interactivo(self):
        """
        Llena la matriz de forma interactiva pidiendo cada elemento al usuario.
        """
        print(f"Ingresa los elementos de la matriz {self.filas}x{self.columnas}:")
        
        for i in range(self.filas):
            for j in range(self.columnas):
                while True:
                    try:
                        entrada = input(f"Elemento [{i+1}][{j+1}]: ").strip()
                        
                        if '/' in entrada:
                            valor = Fraction(entrada)
                        else:
                            valor = validar_numero(entrada)
                            
                        self.datos[i][j] = valor
                        break
                        
                    except ValueError as e:
                        print(f"❌ Error: {e}")
                        print("Por favor ingresa un número válido.")
    
    
    def llenar_aleatorio(self, min_valor=-10, max_valor=10):
        """
        Llena la matriz con números aleatorios en un rango específico.
        
        Args:
            min_valor (int): Valor mínimo para los números aleatorios
            max_valor (int): Valor máximo para los números aleatorios
        """
        import random
        
        for i in range(self.filas):
            for j in range(self.columnas):
                self.datos[i][j] = random.randint(min_valor, max_valor)
    
    
    def obtener_elemento(self, fila, columna):
        """
        Obtiene un elemento específico de la matriz.
        
        Args:
            fila (int): Índice de la fila (0-based)
            columna (int): Índice de la columna (0-based)
            
        Returns:
            El elemento en la posición especificada
            
        Raises:
            IndexError: Si los índices están fuera de rango
        """
        if not (0 <= fila < self.filas):
            raise IndexError(f"Índice de fila {fila} fuera de rango [0, {self.filas-1}]")
        if not (0 <= columna < self.columnas):
            raise IndexError(f"Índice de columna {columna} fuera de rango [0, {self.columnas-1}]")
            
        return self.datos[fila][columna]
    
    
    def establecer_elemento(self, fila, columna, valor):
        """
        Establece un elemento específico en la matriz.
        
        Args:
            fila (int): Índice de la fila (0-based)
            columna (int): Índice de la columna (0-based)
            valor: Valor a establecer
            
        Raises:
            IndexError: Si los índices están fuera de rango
            ValueError: Si el valor no es válido
        """
        if not (0 <= fila < self.filas):
            raise IndexError(f"Índice de fila {fila} fuera de rango [0, {self.filas-1}]")
        if not (0 <= columna < self.columnas):
            raise IndexError(f"Índice de columna {columna} fuera de rango [0, {self.columnas-1}]")
        
        if isinstance(valor, str) and '/' in valor:
            self.datos[fila][columna] = Fraction(valor)
        else:
            self.datos[fila][columna] = validar_numero(valor)
    
    
    def mostrar(self, titulo="Matriz"):
        """
        Muestra la matriz de forma formateada en la consola.
        
        Args:
            titulo (str): Título a mostrar arriba de la matriz
        """
        print(f"\n{titulo}:")
        print("-" * len(titulo + ":"))
        
        # Calcular el ancho máximo para el formato
        max_ancho = 0
        for fila in self.datos:
            for elemento in fila:
                ancho = len(str(formatear_numero(elemento)))
                max_ancho = max(max_ancho, ancho)
        
        max_ancho = max(max_ancho, 4)  # Ancho mínimo de 4
        
        # Mostrar la matriz
        for fila in self.datos:
            elementos_formateados = []
            for elemento in fila:
                elem_str = str(formatear_numero(elemento))
                elementos_formateados.append(f"{elem_str:>{max_ancho}}")
            
            print("[ " + "  ".join(elementos_formateados) + " ]")
        print()
    
    
    def es_cuadrada(self):
        """
        Verifica si la matriz es cuadrada.
        
        Returns:
            bool: True si la matriz es cuadrada, False en caso contrario
        """
        return self.filas == self.columnas
    
    
    def transponer(self):
        """
        Calcula la matriz transpuesta.
        
        Returns:
            Matriz: Nueva matriz que es la transpuesta de la actual
        """
        matriz_transpuesta = Matriz(self.columnas, self.filas)
        
        for i in range(self.filas):
            for j in range(self.columnas):
                matriz_transpuesta.datos[j][i] = self.datos[i][j]
        
        return matriz_transpuesta
    
    
    def copiar(self):
        """
        Crea una copia exacta de la matriz.
        
        Returns:
            Matriz: Nueva matriz idéntica a la actual
        """
        nueva_matriz = Matriz(self.filas, self.columnas)
        
        for i in range(self.filas):
            for j in range(self.columnas):
                nueva_matriz.datos[i][j] = self.datos[i][j]
        
        return nueva_matriz
    
    
    def son_dimensiones_compatibles(self, otra_matriz):
        """
        Verifica si las dimensiones son compatibles con otra matriz.
        
        Args:
            otra_matriz (Matriz): Otra matriz para comparar
            
        Returns:
            bool: True si las dimensiones son iguales
        """
        return (self.filas == otra_matriz.filas and 
                self.columnas == otra_matriz.columnas)
    
    
    def __str__(self):
        """
        Representación en string de la matriz.
        
        Returns:
            str: Representación de la matriz
        """
        resultado = []
        for fila in self.datos:
            elementos = [str(formatear_numero(elemento)) for elemento in fila]
            resultado.append("[ " + "  ".join(elementos) + " ]")
        
        return "\n".join(resultado)
    
    
    def __repr__(self):
        """
        Representación para desarrolladores.
        
        Returns:
            str: Representación técnica de la matriz
        """
        return f"Matriz({self.filas}x{self.columnas})"
