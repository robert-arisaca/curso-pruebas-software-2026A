# Calculadora de IMC - Indice de Masa Corporal según OMS

## Descripción del Proyecto

Este proyecto es una implementación completa de un calculador de Índice de Masa Corporal (IMC) desarrollado siguiendo metodologías de Desarrollo Dirigido por Pruebas (TDD) y Behavior-Driven Development (BDD).

**IMC** (Índice de Masa Corporal) es una medida de la grasa corporal basada en la altura y el peso que se aplica a hombres y mujeres adultos. Se calcula dividiendo el peso en kilogramos por la altura en metros al cuadrado.

## Características

✅ Cálculo preciso del IMC siguiendo la fórmula estándar  
✅ Clasificación automática según estándares de la OMS  
✅ Validación robusta de entrada  
✅ 100% de cobertura de pruebas unitarias  
✅ Especificaciones en Gherkin con pytest-bdd  
✅ Código conforme a PEP 8  
✅ Documentación completa  

## Estructura del Proyecto

```
lab_01/
├── imc.py                          # Implementación principal
├── features/
│   ├── __init__.py                 # Inicializador del paquete
│   ├── calcular_imc.feature        # Especificaciones en Gherkin
│   └── steps/
│       └── imc_steps.py            # Pasos de BDD (pytest-bdd)
├── tests/
│   ├── __init__.py                 # Inicializador del paquete
│   └── test_imc.py                 # Pruebas unitarias (pytest)
├── README.md                        # Este archivo
├── ESPECIFICACION.md               # Documentación de especificaciones
└── IMPLEMENTACION.md               # Documentación de implementación
```

## Requisitos

- Python 3.14.4 o superior
- pytest >= 9.0.3
- pytest-cov >= 7.1.0
- pytest-bdd >= 8.1.0
- coverage >= 7.13.5
- behave >= 1.3.3

Los paquetes ya están instalados en el entorno virtual del proyecto.

## Instalación

El entorno virtual y dependencias ya están configurados. Para activar:

```bash
source /mnt/c/Ubuntu26/UNSA/Software_Testing/venv/bin/activate
```

## Uso

### Ejecutar las pruebas unitarias

```bash
pytest tests/test_imc.py -v
```

### Ver cobertura de pruebas

```bash
pytest tests/test_imc.py --cov=imc --cov-report=html --cov-report=term
```

### Ejecutar las especificaciones BDD

```bash
pytest features/ -v
```

### Ejecutar con behave

### Verificar compatibilidad PEP 8

```bash
python -m pycodestyle imc.py && echo "✅ Código conforme a PEP 8"
```

## Módulos Principales

### imc.py

Contiene la clase `IMCCalculator` con los siguientes métodos:

- **`validar_entrada(peso, altura)`**: Valida que peso y altura sean válidos
- **`calcular_imc(peso, altura)`**: Calcula el IMC
- **`clasificar_imc(imc)`**: Clasifica el IMC en una categoría
- **`obtener_descripcion(categoria)`**: Obtiene la descripción en español
- **`evaluar_imc_completo(peso, altura)`**: Realiza evaluación completa

### Restricciones de Validación

- Peso: Debe ser positivo y menor a 150 kg
- Altura: Debe ser positiva y menor a 2 metros

### Categorías de IMC

| Categoría | Rango IMC | Descripción |
|-----------|-----------|-------------|
| bajo_peso | IMC < 18.5 | Bajo peso |
| peso_normal | 18.5 ≤ IMC < 25.0 | Peso normal |
| sobrepeso | 25.0 ≤ IMC < 30.0 | Sobrepeso |
| obesidad | IMC ≥ 30.0 | Obesidad |

## Especificaciones BDD (Gherkin)

Las especificaciones están documentadas en `features/calcular_imc.feature` e incluyen:

- ✅ Cálculo de IMC para diferentes categorías
- ✅ Validación de entrada (peso positivo, altura positiva)
- ✅ Validación de rangos válidos
- ✅ Manejo de errores

Ver `ESPECIFICACION.md` para detalles.

## Pruebas Unitarias

El archivo `tests/test_imc.py` contiene 37 pruebas organizadas en clases:

- **TestValidarEntrada**: 11 pruebas
- **TestCalcularIMC**: 9 pruebas
- **TestClasificarIMC**: 9 pruebas
- **TestObtenerDescripcion**: 5 pruebas
- **TestEvaluarIMCCompleto**: 7 pruebas

**Cobertura: 100%**

Ver `IMPLEMENTACION.md` para detalles.

## Estándar PEP 8

El código cumple con los estándares PEP 8:

- Nombres descriptivos en inglés
- Docstrings para módulos, clases y funciones
- Máximo 79 caracteres por línea
- Espacios en blanco consistentes
- Comentarios cuando es necesario

## Ejemplos de Uso

### Calcular IMC simple

```python
from imc import IMCCalculator

imc = IMCCalculator.calcular_imc(70, 1.75)
print(f"IMC: {imc}")  # IMC: 22.86
```

### Evaluación completa

```python
resultado = IMCCalculator.evaluar_imc_completo(90, 1.75)
print(f"IMC: {resultado['imc']}")
print(f"Categoría: {resultado['categoria']}")
print(f"Descripción: {resultado['descripcion']}")
```

### Con manejo de errores

```python
try:
    imc = IMCCalculator.calcular_imc(-70, 1.75)
except ValueError as e:
    print(f"Error: {e}")
```

## Documentación Adicional

- **ESPECIFICACION.md**: Explicación detallada de las especificaciones en Gherkin
- **IMPLEMENTACION.md**: Detalles sobre la implementación y cobertura de pruebas

## Autor

Prof. Robert Arisaca
Desarrollado como parte del Curso de "Pruebas de Software" - 2026-A - EPIS UNSA

## Licencia

Este proyecto es educativo y de libre uso.
