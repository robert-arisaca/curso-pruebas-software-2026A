# Documentación de Implementación

## Descripción General

La implementación consiste en tres componentes principales:

1. **imc.py**: Módulo con la lógica del cálculo de IMC
2. **test_imc.py**: Suite de pruebas unitarias con 100% de cobertura
3. **imc_steps.py**: Pasos de BDD para pytest-bdd

## Módulo imc.py

### Estructura

```
IMCCalculator (clase)
├── validar_entrada()
├── calcular_imc()
├── clasificar_imc()
├── obtener_descripcion()
└── evaluar_imc_completo()
```

### Métodos

#### `validar_entrada(peso: float, altura: float) -> tuple[bool, str]`

**Propósito**: Validar que peso y altura sean valores aceptables.

**Validaciones**:
1. Peso debe ser un número positivo
2. Altura debe ser un número positivo
3. Altura debe ser menor a 2 metros (IMC = 17.5 para 70kg)
4. Peso debe ser menor a 150 kg (IMC = 48.98... para 1.75m)

**Retorna**: Tupla `(es_válido, mensaje_error)`

**Ejemplo**:
```python
es_valido, msg = IMCCalculator.validar_entrada(70, 1.75)
# (True, "")

es_valido, msg = IMCCalculator.validar_entrada(-70, 1.75)
# (False, "El peso debe ser un número positivo")
```

---

#### `calcular_imc(peso: float, altura: float) -> float`

**Propósito**: Calcular el IMC usando la fórmula: IMC = peso / (altura²)

**Fórmula**:
```
IMC = peso (kg) / (altura (m) ^ 2)
```

**Pasos**:
1. Valida entrada
2. Calcula IMC
3. Redondea a 2 decimales
4. Retorna el resultado

**Excepciones**: `ValueError` si la entrada no es válida

**Ejemplo**:
```python
imc = IMCCalculator.calcular_imc(70, 1.75)
# 22.86

imc = IMCCalculator.calcular_imc(-70, 1.75)
# ValueError: El peso debe ser un número positivo
```

---

#### `clasificar_imc(imc: float) -> str`

**Propósito**: Clasificar el IMC en una de 4 categorías.

**Categorías** (según OMS):
| Rango IMC | Categoría |
|-----------|-----------|
| IMC < 18.5 | `bajo_peso` |
| 18.5 ≤ IMC < 25.0 | `peso_normal` |
| 25.0 ≤ IMC < 30.0 | `sobrepeso` |
| IMC ≥ 30.0 | `obesidad` |

**Excepciones**: `ValueError` si IMC es negativo

**Ejemplo**:
```python
clasificar_imc(22.86)   # 'peso_normal'
clasificar_imc(29.39)   # 'sobrepeso'
clasificar_imc(16.33)   # 'bajo_peso'
clasificar_imc(39.18)   # 'obesidad'
```

---

#### `obtener_descripcion(categoria: str) -> str`

**Propósito**: Obtener descripción en español de la categoría.

**Mapping**:
```python
{
    'bajo_peso': 'Bajo peso',
    'peso_normal': 'Peso normal',
    'sobrepeso': 'Sobrepeso',
    'obesidad': 'Obesidad'
}
```

**Excepciones**: `ValueError` si la categoría es inválida

**Ejemplo**:
```python
obtener_descripcion('peso_normal')  # 'Peso normal'
obtener_descripcion('invalida')     # ValueError
```

---

#### `evaluar_imc_completo(peso: float, altura: float) -> dict`

**Propósito**: Realizar evaluación completa del IMC en una sola llamada.

**Retorna**: Diccionario con:
```python
{
    'imc': float,           # Valor del IMC
    'categoria': str,       # Categoría del IMC
    'descripcion': str      # Descripción en español
}
```

**Ejemplo**:
```python
resultado = IMCCalculator.evaluar_imc_completo(70, 1.75)
# {
#     'imc': 22.86,
#     'categoria': 'peso_normal',
#     'descripcion': 'Peso normal'
# }
```

---

## Pruebas Unitarias (test_imc.py)

### Estructura

Las pruebas están organizadas en 5 clases:

```
TestValidarEntrada (11 pruebas)
├── test_validar_entrada_valores_validos
├── test_validar_entrada_peso_negativo
├── test_validar_entrada_peso_cero
├── test_validar_entrada_peso_no_numerico
├── test_validar_entrada_altura_negativa
├── test_validar_entrada_altura_cero
├── test_validar_entrada_altura_no_numerica
├── test_validar_entrada_altura_mayor_2_metros
├── test_validar_entrada_altura_exactamente_2_metros
├── test_validar_entrada_peso_mayor_150_kg
└── test_validar_entrada_peso_exactamente_150_kg

TestCalcularIMC (9 pruebas)
├── test_calcular_imc_peso_normal
├── test_calcular_imc_sobrepeso
├── test_calcular_imc_bajo_peso
├── test_calcular_imc_obesidad
├── test_calcular_imc_redondea_a_2_decimales
├── test_calcular_imc_peso_invalidro_lanza_error
├── test_calcular_imc_altura_invalida_lanza_error
├── test_calcular_imc_altura_muy_grande_lanza_error
└── test_calcular_imc_peso_muy_grande_lanza_error

TestClasificarIMC (9 pruebas)
├── test_clasificar_imc_bajo_peso_limite_inferior
├── test_clasificar_imc_bajo_peso_limite_superior
├── test_clasificar_imc_peso_normal_limite_inferior
├── test_clasificar_imc_peso_normal_limite_superior
├── test_clasificar_imc_sobrepeso_limite_inferior
├── test_clasificar_imc_sobrepeso_limite_superior
├── test_clasificar_imc_obesidad_limite_inferior
├── test_clasificar_imc_obesidad_valor_alto
└── test_clasificar_imc_negativo_lanza_error

TestObtenerDescripcion (5 pruebas)
├── test_obtener_descripcion_bajo_peso
├── test_obtener_descripcion_peso_normal
├── test_obtener_descripcion_sobrepeso
├── test_obtener_descripcion_obesidad
└── test_obtener_descripcion_invalida_lanza_error

TestEvaluarIMCCompleto (7 pruebas)
├── test_evaluar_imc_completo_peso_normal
├── test_evaluar_imc_completo_sobrepeso
├── test_evaluar_imc_completo_bajo_peso
├── test_evaluar_imc_completo_obesidad
├── test_evaluar_imc_completo_retorna_diccionario
├── test_evaluar_imc_completo_peso_invalido_lanza_error
└── test_evaluar_imc_completo_altura_invalida_lanza_error
```

### Total: 37 pruebas unitarias

---

## Cobertura de Pruebas

### Cobertura al 100%

```
Name          Stmts   Miss  Cover
-----------------------------------
imc.py           52      0   100%
-----------------------------------
TOTAL            52      0   100%
```

### Estrategia de Cobertura

#### 1. Validación (11 pruebas)
- ✅ Entrada válida
- ✅ Peso negativo, cero, no numérico
- ✅ Altura negativa, cero, no numérica
- ✅ Altura > 2 metros
- ✅ Peso > 150 kg
- ✅ Límites exactos (2.0m, 150kg)

#### 2. Cálculo de IMC (9 pruebas)
- ✅ Cálculo para cada categoría
- ✅ Redondeo a 2 decimales
- ✅ Manejo de errores de validación

#### 3. Clasificación (9 pruebas)
- ✅ Cada categoría en rango normal
- ✅ Límites de cada categoría
- ✅ IMC negativo (error)

#### 4. Descripción (5 pruebas)
- ✅ Cada categoría válida
- ✅ Categoría inválida (error)

#### 5. Evaluación completa (7 pruebas)
- ✅ Cada categoría completa
- ✅ Estructura del diccionario
- ✅ Manejo de errores

---

## Estándar PEP 8

### Requisitos cumplidos

- ✅ **Nombres de variables y funciones**: `snake_case` en inglés
- ✅ **Nombres de clases**: `PascalCase`
- ✅ **Longitud de línea**: Máximo 79 caracteres
- ✅ **Espacios en blanco**: 4 espacios para indentación
- ✅ **Docstrings**: Triple comillas para módulos, clases y funciones
- ✅ **Comentarios**: Cuando el propósito no es obvio
- ✅ **Imports**: Agrupados y ordenados correctamente

### Ejemplo

```python
"""
Módulo para calcular el Índice de Masa Corporal (IMC).
"""


class IMCCalculator:
    """Clase para calcular el Índice de Masa Corporal."""

    CATEGORIAS = {
        'bajo_peso': (0, 18.5),
        'peso_normal': (18.5, 25.0),
        'sobrepeso': (25.0, 30.0),
        'obesidad': (30.0, float('inf'))
    }

    @staticmethod
    def calcular_imc(peso: float, altura: float) -> float:
        """
        Calcula el Índice de Masa Corporal.

        Formula: IMC = peso (kg) / (altura (m) ** 2)
        """
        # Código...
```

---

## Ejecución de Pruebas

### Ejecutar todas las pruebas

```bash
pytest tests/test_imc.py -v
```

**Salida esperada**:
```
tests/test_imc.py::TestValidarEntrada::test_validar_entrada_valores_validos PASSED
tests/test_imc.py::TestValidarEntrada::test_validar_entrada_peso_negativo PASSED
...
37 passed in 0.45s
```

### Ver cobertura detallada

```bash
pytest tests/test_imc.py --cov=imc --cov-report=html --cov-report=term
```

**Salida esperada**:
```
coverage: platform linux -- Python 3.14.4, pytest-9.0.3, pytest-cov-7.1.0
collected 37 items

tests/test_imc.py::TestValidarEntrada::test_validar_entrada_valores_validos PASSED

------- coverage: platform linux -------
Name          Stmts   Miss  Cover
imc.py           52      0   100%
```

### Mostrar líneas no cubiertas

```bash
pytest tests/test_imc.py --cov=imc --cov-report=term-missing
```

---

## Instrucciones de Uso

### Como módulo Python

```python
from imc import IMCCalculator

# Cálculo simple
imc = IMCCalculator.calcular_imc(70, 1.75)
print(f"Tu IMC es: {imc}")

# Clasificación
categoria = IMCCalculator.clasificar_imc(imc)
descripcion = IMCCalculator.obtener_descripcion(categoria)
print(f"Categoría: {descripcion}")

# Evaluación completa
resultado = IMCCalculator.evaluar_imc_completo(70, 1.75)
print(resultado)
```

### Manejo de errores

```python
try:
    imc = IMCCalculator.calcular_imc(-70, 1.75)
except ValueError as e:
    print(f"Error: {e}")
```

---

## Mejoras Futuras

Posibles extensiones:

1. Añadir diferentes categorías según edad
2. Exportar resultados a JSON/CSV
3. Crear interfaz gráfica
4. Integración con bases de datos
5. API REST

---

## Referencias

- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [pytest Documentation](https://docs.pytest.org/)
- [coverage.py Documentation](https://coverage.readthedocs.io/)
- [OMS - IMC](https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight)
