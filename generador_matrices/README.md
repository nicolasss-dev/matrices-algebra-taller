# Generador de Matrices

Un generador y manipulador de matrices implementado en Python vanilla (sin librerías externas).

## Características

- ✅ Creación de matrices de cualquier tamaño
- ✅ Operaciones matemáticas básicas (suma, resta, multiplicación)
- ✅ Soporte para números enteros, decimales y fracciones
- ✅ Interfaz de línea de comandos
- ✅ Interfaz gráfica con Tkinter
- ✅ Validación de entrada robusta
- ✅ Pruebas unitarias completas

## Estructura del Proyecto

```
generador_matrices/
│
├── README.md
├── main.py
│
├── src/
│   ├── __init__.py
│   ├── matriz.py              # Clase principal Matriz
│   ├── operaciones.py         # Operaciones matemáticas
│   ├── validadores.py         # Validación de entrada
│   └── utilidades.py          # Funciones auxiliares
│
├── interfaces/
│   ├── __init__.py
│   ├── consola.py            # Interfaz de línea de comandos
│   └── grafica.py            # Interfaz gráfica con Tkinter
│
├── tests/
│   ├── __init__.py
│   ├── test_matriz.py
│   ├── test_operaciones.py
│   └── test_validadores.py
│
└── ejemplos/
    ├── ejemplo_basico.py
    ├── ejemplo_fracciones.py
    └── ejemplo_operaciones.py
```

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/generador_matrices.git
cd generador_matrices
```

2. No se requieren dependencias externas, solo Python 3.6+

## Uso

### Ejecutar el programa principal:
```bash
python main.py
```

### Ejecutar ejemplos:
```bash
python ejemplos/ejemplo_basico.py
python ejemplos/ejemplo_fracciones.py
python ejemplos/ejemplo_operaciones.py
```

### Ejecutar pruebas:
```bash
python -m pytest tests/
```

## Ejemplos de Uso

```python
from src.matriz import Matriz

# Crear una matriz 3x3
matriz = Matriz(3, 3)
matriz.llenar_manual([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Mostrar la matriz
matriz.mostrar()

# Operaciones
from src.operaciones import sumar_matrices, multiplicar_matrices

matriz_a = Matriz(2, 2)
matriz_b = Matriz(2, 2)
# ... llenar matrices ...

resultado = sumar_matrices(matriz_a, matriz_b)
```

## Características Técnicas

- **Sin dependencias externas**: Solo usa la librería estándar de Python
- **Soporte para fracciones**: Manejo preciso de números racionales
- **Validación robusta**: Verificación de entrada en todos los métodos
- **Interfaces múltiples**: CLI y GUI disponibles
- **Pruebas completas**: Cobertura de pruebas unitarias

## Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Autor

**Nicolas** - [Tu perfil de GitHub](https://github.com/tu-usuario)
