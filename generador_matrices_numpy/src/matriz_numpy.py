"""
Clase MatrizNumPy - Implementación Optimizada con NumPy
======================================================

Clase principal que encapsula un array de NumPy con funcionalidades
avanzadas para álgebra lineal y análisis numérico.

Características principales:
- Operaciones vectorizadas ultra-rápidas
- Soporte para matrices de cualquier tamaño
- Funciones avanzadas de álgebra lineal
- Visualización integrada
- Compatibilidad con el ecosistema científico de Python

Autor: Nicolas
"""

import numpy as np
from typing import Union, Tuple, Optional, List, Any
from fractions import Fraction
import warnings

# Sin dependencias de matplotlib - solo operaciones básicas con matrices


class MatrizNumPy:
    """
    Clase principal para manejo de matrices usando NumPy.
    
    Encapsula un numpy.ndarray con funcionalidades adicionales específicas
    para álgebra lineal, análisis numérico y visualización.
    
    Attributes:
        datos (np.ndarray): Array de NumPy que contiene los datos de la matriz
        filas (int): Número de filas
        columnas (int): Número de columnas
        dtype (np.dtype): Tipo de datos de la matriz
    """
    
    def __init__(self, datos_o_filas: Union[List[List], np.ndarray, int], 
                 columnas: Optional[int] = None, dtype: np.dtype = np.float64, 
                 inicializar_ceros: bool = True):
        """
        Inicializa una nueva matriz con NumPy.
        
        Parameters:
            datos_o_filas: Puede ser:
                - Lista de listas con datos
                - Array de NumPy 2D
                - Número de filas (int)
            columnas (Optional[int]): Número de columnas (solo si primer parámetro es int)
            dtype (np.dtype): Tipo de datos (default: float64)
            inicializar_ceros (bool): Si inicializar con ceros (solo para constructor vacío)
            
        Raises:
            ValueError: Si las dimensiones son inválidas
        """
        if isinstance(datos_o_filas, (list, tuple)):
            # Constructor desde lista de listas
            if not datos_o_filas or not datos_o_filas[0]:
                raise ValueError("La lista no puede estar vacía")
            
            self.filas = len(datos_o_filas)
            self.columnas = len(datos_o_filas[0])
            
            # Verificar que todas las filas tengan el mismo tamaño
            for i, fila in enumerate(datos_o_filas):
                if len(fila) != self.columnas:
                    raise ValueError(f"Fila {i} tiene {len(fila)} elementos, esperaba {self.columnas}")
            
            # Determinar el tipo de datos más apropiado
            self.dtype = self._determinar_dtype(datos_o_filas) if dtype == np.float64 else dtype
            self.datos = np.array(datos_o_filas, dtype=self.dtype)
            
        elif isinstance(datos_o_filas, np.ndarray):
            # Constructor desde array de NumPy
            if datos_o_filas.ndim != 2:
                raise ValueError("El array debe ser 2D")
            self.filas, self.columnas = datos_o_filas.shape
            self.dtype = datos_o_filas.dtype if dtype == np.float64 else dtype
            self.datos = datos_o_filas.astype(self.dtype).copy()
            
        elif isinstance(datos_o_filas, int):
            # Constructor tradicional (filas, columnas)
            if columnas is None:
                raise ValueError("Debe especificar el número de columnas")
            
            self._validar_dimensiones(datos_o_filas, columnas)
            self.filas = datos_o_filas
            self.columnas = columnas
            self.dtype = dtype
            
            if inicializar_ceros:
                self.datos = np.zeros((self.filas, self.columnas), dtype=dtype)
            else:
                self.datos = np.empty((self.filas, self.columnas), dtype=dtype)
        else:
            raise ValueError("Tipo de datos no válido para el constructor")
            
    @property
    def shape(self) -> Tuple[int, int]:
        """Devuelve la forma (dimensiones) de la matriz."""
        return (self.filas, self.columnas)
    
    @classmethod
    def desde_array(cls, array: np.ndarray) -> 'MatrizNumPy':
        """
        Crea una MatrizNumPy desde un array de NumPy existente.
        
        Parameters:
            array (np.ndarray): Array de NumPy 2D
            
        Returns:
            MatrizNumPy: Nueva instancia
        """
        return cls(array)
    
    @classmethod
    def desde_lista(cls, lista: List[List[Union[int, float, str]]]) -> 'MatrizNumPy':
        """
        Crea una MatrizNumPy desde una lista de listas.
        
        Parameters:
            lista (List[List]): Lista de listas con los datos
            
        Returns:
            MatrizNumPy: Nueva instancia
        """
        return cls(lista)
    
    @classmethod
    def crear_identidad(cls, tamaño: int, dtype: np.dtype = np.float64) -> 'MatrizNumPy':
        """Crea una matriz identidad."""
        matriz = cls(tamaño, tamaño, dtype=dtype, inicializar_ceros=False)
        matriz.datos = np.eye(tamaño, dtype=dtype)
        return matriz
    
    @classmethod
    def crear_ceros(cls, filas: int, columnas: int, dtype: np.dtype = np.float64) -> 'MatrizNumPy':
        """Crea una matriz de ceros."""
        return cls(filas, columnas, dtype=dtype, inicializar_ceros=True)
    
    @classmethod
    def crear_unos(cls, filas: int, columnas: int, dtype: np.dtype = np.float64) -> 'MatrizNumPy':
        """Crea una matriz de unos."""
        matriz = cls(filas, columnas, dtype=dtype, inicializar_ceros=False)
        matriz.datos = np.ones((filas, columnas), dtype=dtype)
        return matriz
    
    @classmethod
    def crear_aleatoria(cls, filas: int, columnas: int, min_val: float = 0.0, 
                       max_val: float = 1.0, dtype: np.dtype = np.float64, 
                       seed: Optional[int] = None) -> 'MatrizNumPy':
        """
        Crea una matriz con valores aleatorios.
        
        Parameters:
            filas, columnas: Dimensiones
            min_val, max_val: Rango de valores
            dtype: Tipo de datos
            seed: Semilla para reproducibilidad
            
        Returns:
            MatrizNumPy: Matriz con valores aleatorios
        """
        if seed is not None:
            np.random.seed(seed)
        
        matriz = cls(filas, columnas, dtype=dtype, inicializar_ceros=False)
        
        if dtype in [np.int32, np.int64]:
            # Para enteros, usar randint
            matriz.datos = np.random.randint(int(min_val), int(max_val) + 1, 
                                           size=(filas, columnas), dtype=dtype)
        else:
            # Para flotantes, usar uniform
            matriz.datos = np.random.uniform(min_val, max_val, size=(filas, columnas))
            matriz.datos = matriz.datos.astype(dtype)
        
        return matriz
    
    @classmethod
    def crear_diagonal(cls, valores: List[Union[int, float]], dtype: np.dtype = np.float64) -> 'MatrizNumPy':
        """Crea una matriz diagonal."""
        tamaño = len(valores)
        matriz = cls(tamaño, tamaño, dtype=dtype, inicializar_ceros=False)
        matriz.datos = np.diag(valores).astype(dtype)
        return matriz
    
    def llenar_manual(self, datos: List[List[Union[int, float, str]]]) -> None:
        """Llena la matriz con datos específicos."""
        if len(datos) != self.filas:
            raise ValueError(f"Se esperaban {self.filas} filas, se recibieron {len(datos)}")
        
        for i, fila in enumerate(datos):
            if len(fila) != self.columnas:
                raise ValueError(f"Fila {i} debe tener {self.columnas} elementos")
        
        # Convertir a array de NumPy directamente
        self.datos = np.array(datos, dtype=self.dtype)
    
    def llenar_aleatorio(self, min_val: float = -10, max_val: float = 10, seed: Optional[int] = None) -> None:
        """Llena la matriz con valores aleatorios."""
        if seed is not None:
            np.random.seed(seed)
        
        if self.dtype in [np.int32, np.int64]:
            self.datos = np.random.randint(int(min_val), int(max_val) + 1, 
                                         size=(self.filas, self.columnas), dtype=self.dtype)
        else:
            self.datos = np.random.uniform(min_val, max_val, size=(self.filas, self.columnas))
            self.datos = self.datos.astype(self.dtype)
    
    def obtener_elemento(self, fila: int, columna: int) -> Union[int, float]:
        """Obtiene un elemento específico."""
        return self.datos[fila, columna].item()
    
    def establecer_elemento(self, fila: int, columna: int, valor: Union[int, float]) -> None:
        """Establece un elemento específico."""
        self.datos[fila, columna] = valor
    
    def es_cuadrada(self) -> bool:
        """Verifica si la matriz es cuadrada."""
        return self.filas == self.columnas
    
    def transponer(self) -> 'MatrizNumPy':
        """Calcula la transpuesta de la matriz."""
        matriz_transpuesta = MatrizNumPy(self.columnas, self.filas, dtype=self.dtype, 
                                       inicializar_ceros=False)
        matriz_transpuesta.datos = self.datos.T.copy()
        return matriz_transpuesta
    
    def copiar(self) -> 'MatrizNumPy':
        """Crea una copia exacta de la matriz."""
        nueva_matriz = MatrizNumPy(self.filas, self.columnas, dtype=self.dtype, 
                                 inicializar_ceros=False)
        nueva_matriz.datos = self.datos.copy()
        return nueva_matriz
    
    # ============ OPERACIONES BÁSICAS ============
    
    def __add__(self, otra: 'MatrizNumPy') -> 'MatrizNumPy':
        """Suma de matrices usando el operador +."""
        if not self.son_dimensiones_compatibles(otra):
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumar")
        
        resultado = MatrizNumPy(self.filas, self.columnas, dtype=self.dtype, inicializar_ceros=False)
        resultado.datos = self.datos + otra.datos
        return resultado
    
    def __sub__(self, otra: 'MatrizNumPy') -> 'MatrizNumPy':
        """Resta de matrices usando el operador -."""
        if not self.son_dimensiones_compatibles(otra):
            raise ValueError("Las matrices deben tener las mismas dimensiones para restar")
        
        resultado = MatrizNumPy(self.filas, self.columnas, dtype=self.dtype, inicializar_ceros=False)
        resultado.datos = self.datos - otra.datos
        return resultado
    
    def __matmul__(self, otra: 'MatrizNumPy') -> 'MatrizNumPy':
        """Multiplicación de matrices usando el operador @."""
        if self.columnas != otra.filas:
            raise ValueError(f"Para multiplicar matrices, las columnas de la primera ({self.columnas}) "
                           f"deben ser iguales a las filas de la segunda ({otra.filas})")
        
        resultado = MatrizNumPy(self.filas, otra.columnas, dtype=self.dtype, inicializar_ceros=False)
        resultado.datos = self.datos @ otra.datos
        return resultado
    
    def __mul__(self, escalar: Union[int, float]) -> 'MatrizNumPy':
        """Multiplicación por escalar usando el operador *."""
        resultado = MatrizNumPy(self.filas, self.columnas, dtype=self.dtype, inicializar_ceros=False)
        resultado.datos = self.datos * escalar
        return resultado
    
    def __rmul__(self, escalar: Union[int, float]) -> 'MatrizNumPy':
        """Multiplicación por escalar (orden inverso)."""
        return self.__mul__(escalar)
    
    def __pow__(self, exponente: int) -> 'MatrizNumPy':
        """Potenciación de matrices usando el operador **."""
        if not self.es_cuadrada():
            raise ValueError("Solo se pueden elevar a potencias las matrices cuadradas")
        
        if exponente == 0:
            return MatrizNumPy.crear_identidad(self.filas, dtype=self.dtype)
        elif exponente == 1:
            return self.copiar()
        elif exponente < 0:
            # Potencia negativa requiere inversa
            inv_matriz = self.inversa()
            return inv_matriz ** (-exponente)
        else:
            resultado = self.copiar()
            for _ in range(exponente - 1):
                resultado = resultado @ self
            return resultado
    
    # ============ ÁLGEBRA LINEAL AVANZADA ============
    
    def determinante(self) -> float:
        """Calcula el determinante de la matriz."""
        if not self.es_cuadrada():
            raise ValueError("El determinante solo está definido para matrices cuadradas")
        
        return float(np.linalg.det(self.datos))
    
    def inversa(self) -> 'MatrizNumPy':
        """Calcula la inversa de la matriz."""
        if not self.es_cuadrada():
            raise ValueError("Solo las matrices cuadradas tienen inversa")
        
        det = self.determinante()
        if abs(det) < 1e-14:
            raise ValueError("La matriz es singular (no invertible)")
        
        resultado = MatrizNumPy(self.filas, self.columnas, dtype=self.dtype, inicializar_ceros=False)
        resultado.datos = np.linalg.inv(self.datos)
        return resultado
    
    def rango(self) -> int:
        """Calcula el rango de la matriz."""
        return int(np.linalg.matrix_rank(self.datos))
    
    def norma(self, tipo: str = 'fro') -> float:
        """
        Calcula diferentes normas de la matriz.
        
        Parameters:
            tipo (str): 'fro' (Frobenius), '1', '2', 'inf', 'nuc' (nuclear)
        """
        if tipo == 'fro':
            return float(np.linalg.norm(self.datos, 'fro'))
        elif tipo in ['1', '2', 'inf', 'nuc']:
            return float(np.linalg.norm(self.datos, tipo))
        else:
            raise ValueError(f"Tipo de norma no soportado: {tipo}")
    
    def eigenvalores(self) -> np.ndarray:
        """Calcula los eigenvalores de la matriz."""
        if not self.es_cuadrada():
            raise ValueError("Los eigenvalores solo están definidos para matrices cuadradas")
        
        return np.linalg.eigvals(self.datos)
    
    def eigenvectores(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calcula eigenvalores y eigenvectores.
        
        Returns:
            Tuple: (eigenvalores, eigenvectores)
        """
        if not self.es_cuadrada():
            raise ValueError("Los eigenvectores solo están definidos para matrices cuadradas")
        
        return np.linalg.eig(self.datos)
    
    def svd(self, computar_uv: bool = True) -> Union[Tuple[np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
        """
        Descomposición en valores singulares (SVD).
        
        Parameters:
            computar_uv (bool): Si computar las matrices U y V
            
        Returns:
            Si computar_uv=True: (U, s, Vt)
            Si computar_uv=False: s (solo valores singulares)
        """
        return np.linalg.svd(self.datos, compute_uv=computar_uv)
    
    def qr(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Descomposición QR.
        
        Returns:
            Tuple: (Q, R) donde Q es ortogonal y R es triangular superior
        """
        return np.linalg.qr(self.datos)
    
    def cholesky(self) -> 'MatrizNumPy':
        """
        Descomposición de Cholesky (para matrices definidas positivas).
        
        Returns:
            MatrizNumPy: Matriz triangular inferior L tal que A = L @ L.T
        """
        if not self.es_cuadrada():
            raise ValueError("La descomposición de Cholesky requiere una matriz cuadrada")
        
        if not self.es_definida_positiva():
            raise ValueError("La matriz debe ser definida positiva para Cholesky")
        
        resultado = MatrizNumPy(self.filas, self.columnas, dtype=self.dtype, inicializar_ceros=False)
        resultado.datos = np.linalg.cholesky(self.datos)
        return resultado
    
    def condicion(self) -> float:
        """Calcula el número de condición de la matriz."""
        return float(np.linalg.cond(self.datos))
    
    def es_definida_positiva(self) -> bool:
        """Verifica si la matriz es definida positiva."""
        if not self.es_cuadrada():
            return False
        
        try:
            np.linalg.cholesky(self.datos)
            return True
        except np.linalg.LinAlgError:
            return False
    
    def es_simetrica(self, tolerancia: float = 1e-10) -> bool:
        """Verifica si la matriz es simétrica."""
        if not self.es_cuadrada():
            return False
        
        return np.allclose(self.datos, self.datos.T, atol=tolerancia)
    
    def es_ortogonal(self, tolerancia: float = 1e-10) -> bool:
        """Verifica si la matriz es ortogonal."""
        if not self.es_cuadrada():
            return False
        
        producto = self.datos @ self.datos.T
        identidad = np.eye(self.filas)
        return np.allclose(producto, identidad, atol=tolerancia)
    
    # ============ UTILIDADES ============
    
    def son_dimensiones_compatibles(self, otra: 'MatrizNumPy') -> bool:
        """Verifica si las dimensiones son compatibles para suma/resta."""
        return self.filas == otra.filas and self.columnas == otra.columnas
    
    def mostrar(self, titulo: str = "Matriz", precision: int = 3) -> None:
        """
        Muestra la matriz de forma formateada.
        
        Parameters:
            titulo (str): Título a mostrar
            precision (int): Decimales a mostrar para números flotantes
        """
        print(f"\n{titulo}:")
        print("-" * len(titulo + ":"))
        print(f"Dimensiones: {self.filas}×{self.columnas}")
        print(f"Tipo de datos: {self.dtype}")
        print(f"Es cuadrada: {'Sí' if self.es_cuadrada() else 'No'}")
        
        if self.filas <= 20 and self.columnas <= 20:  # Solo mostrar matrices no muy grandes
            print("\nContenido:")
            
            # Formatear según el tipo de datos
            if self.dtype in [np.int32, np.int64]:
                print(self.datos)
            else:
                with np.printoptions(precision=precision, suppress=True):
                    print(self.datos)
        else:
            print(f"\n(Matriz muy grande para mostrar: {self.filas}×{self.columnas})")
        print()
    
    # ============ VISUALIZACIÓN ============
    
    def __str__(self) -> str:
        """Representación en string de la matriz."""
        return f"MatrizNumPy({self.filas}×{self.columnas}, dtype={self.dtype})\n{self.datos}"
    
    def __repr__(self) -> str:
        """Representación técnica de la matriz."""
        return f"MatrizNumPy(filas={self.filas}, columnas={self.columnas}, dtype={self.dtype})"
    
    def __eq__(self, otra: 'MatrizNumPy') -> bool:
        """Comparación de igualdad entre matrices."""
        if not isinstance(otra, MatrizNumPy):
            return False
        
        return (self.filas == otra.filas and 
                self.columnas == otra.columnas and
                np.array_equal(self.datos, otra.datos))
    
    def __getitem__(self, key) -> Union[float, np.ndarray]:
        """Permite indexación directa de la matriz."""
        return self.datos[key]
    
    def __setitem__(self, key, valor) -> None:
        """Permite asignación directa a la matriz."""
        self.datos[key] = valor
    
    # ============ MÉTODOS PRIVADOS ============
    
    @staticmethod
    def _validar_dimensiones(filas: int, columnas: int) -> None:
        """Valida que las dimensiones sean correctas."""
        if not isinstance(filas, int) or not isinstance(columnas, int):
            raise ValueError("Las dimensiones deben ser números enteros")
        
        if filas <= 0 or columnas <= 0:
            raise ValueError("Las dimensiones deben ser números positivos")
        
        # Para NumPy no limitamos el tamaño máximo (a diferencia de la versión vanilla)
    
    @staticmethod
    def _determinar_dtype(lista: List[List]) -> np.dtype:
        """Determina el tipo de datos más apropiado para una lista de listas."""
        # Inspeccionar algunos elementos para determinar el tipo
        muestra = []
        for fila in lista[:3]:  # Revisar solo las primeras 3 filas
            for elemento in fila[:3]:  # Y primeros 3 elementos de cada fila
                muestra.append(elemento)
        
        tiene_fracciones = any(isinstance(elem, (str, Fraction)) and 
                              ('/' in str(elem) if isinstance(elem, str) else True) 
                              for elem in muestra)
        tiene_flotantes = any(isinstance(elem, float) or 
                             ('.' in str(elem) if isinstance(elem, str) else False) 
                             for elem in muestra)
        
        if tiene_fracciones:
            return np.float64  # Las fracciones se convierten a float
        elif tiene_flotantes:
            return np.float64
        else:
            return np.int64
