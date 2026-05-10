# Especificaciones BDD - Calculadora de IMC

## Introducción

Las especificaciones están redactadas en Gherkin y se implementan con **pytest-bdd**. Estas especificaciones definen el comportamiento esperado del calculador de IMC.

## Archivo Feature

**Ubicación**: `features/calcular_imc.feature`

El archivo está estructurado según el formato Gherkin y especifica:
- Característica principal: Calcular el Índice de Masa Corporal
- Escenarios de prueba: 8 escenarios diferentes

## Escenarios Definidos

### 1. Calcular IMC de una persona con peso normal

**Descripción**: Verifica que una persona con peso normal (IMC entre 18.5 y 25) sea clasificada correctamente.

**Pasos**:
```gherkin
Dado que tengo un peso de 70 kg
Y tengo una altura de 1.75 m
Cuando calculo mi IMC
Entonces mi IMC es 22.86
Y mi categoría es peso_normal
Y mi descripción es Peso normal
```

**Valores esperados**:
- IMC: 22.86 (70 / (1.75²) = 22.857... → 22.86)
- Categoría: `peso_normal`
- Descripción: "Peso normal"

---

### 2. Calcular IMC de una persona con sobrepeso

**Descripción**: Verifica que una persona con sobrepeso (IMC entre 25 y 30) sea clasificada correctamente.

**Pasos**:
```gherkin
Dado que tengo un peso de 90 kg
Y tengo una altura de 1.75 m
Cuando calculo mi IMC
Entonces mi IMC es 29.39
Y mi categoría es sobrepeso
Y mi descripción es Sobrepeso
```

**Valores esperados**:
- IMC: 29.39
- Categoría: `sobrepeso`
- Descripción: "Sobrepeso"

---

### 3. Calcular IMC de una persona con bajo peso

**Descripción**: Verifica que una persona con bajo peso (IMC < 18.5) sea clasificada correctamente.

**Pasos**:
```gherkin
Dado que tengo un peso de 50 kg
Y tengo una altura de 1.75 m
Cuando calculo mi IMC
Entonces mi IMC es 16.33
Y mi categoría es bajo_peso
Y mi descripción es Bajo peso
```

**Valores esperados**:
- IMC: 16.33
- Categoría: `bajo_peso`
- Descripción: "Bajo peso"

---

### 4. Calcular IMC de una persona con obesidad

**Descripción**: Verifica que una persona con obesidad (IMC ≥ 30) sea clasificada correctamente.

**Pasos**:
```gherkin
Dado que tengo un peso de 120 kg
Y tengo una altura de 1.75 m
Cuando calculo mi IMC
Entonces mi IMC es 39.18
Y mi categoría es obesidad
Y mi descripción es Obesidad
```

**Valores esperados**:
- IMC: 39.18
- Categoría: `obesidad`
- Descripción: "Obesidad"

---

### 5. Validar que el peso debe ser positivo

**Descripción**: Verifica que se rechace un peso negativo.

**Pasos**:
```gherkin
Dado que tengo un peso de -5 kg
Y tengo una altura de 1.75 m
Cuando intento calcular mi IMC
Entonces obtengo un error diciendo "El peso debe ser un número positivo"
```

**Comportamiento esperado**:
- Se lanza una excepción `ValueError`
- Mensaje de error: "El peso debe ser un número positivo"

---

### 6. Validar que la altura debe ser positiva

**Descripción**: Verifica que se rechace una altura negativa.

**Pasos**:
```gherkin
Dado que tengo un peso de 70 kg
Y tengo una altura de -1.75 m
Cuando intento calcular mi IMC
Entonces obtengo un error diciendo "La altura debe ser un número positivo"
```

**Comportamiento esperado**:
- Se lanza una excepción `ValueError`
- Mensaje de error: "La altura debe ser un número positivo"

---

### 7. Validar que la altura no sea mayor a 2 metros

**Descripción**: Verifica que se rechace una altura irreal (mayor a 2 metros).

**Pasos**:
```gherkin
Dado que tengo un peso de 70 kg
Y tengo una altura de 2.5 m
Cuando intento calcular mi IMC
Entonces obtengo un error diciendo "La altura debe ser menor a 2 metros"
```

**Comportamiento esperado**:
- Se lanza una excepción `ValueError`
- Mensaje de error: "La altura debe ser menor a 2 metros"

---

### 8. Validar que el peso no sea mayor a 150 kg

**Descripción**: Verifica que se rechace un peso irreal (mayor a 150 kg).

**Pasos**:
```gherkin
Dado que tengo un peso de 160 kg
Y tengo una altura de 1.75 m
Cuando intento calcular mi IMC
Entonces obtengo un error diciendo "El peso debe ser menor a 150 kg"
```

**Comportamiento esperado**:
- Se lanza una excepción `ValueError`
- Mensaje de error: "El peso debe ser menor a 150 kg"

---

## Implementación de Pasos

Los pasos están implementados en `features/steps/imc_steps.py` usando decoradores de **pytest-bdd**:

| Decorador | Tipo | Descripción |
|-----------|------|-------------|
| `@given` | Setup | Define las condiciones iniciales |
| `@when` | Acción | Ejecuta la acción a probar |
| `@then` | Verificación | Valida los resultados |

### Ejemplo de Paso

```python
@given('que tengo un peso de <peso> kg')
def step_peso(contexto, peso):
    """Almacena el peso en el contexto."""
    contexto['peso'] = float(peso)
```

## Estructura de Contexto

Los pasos utilizan un fixture `contexto` que almacena:

```python
{
    'peso': float,           # Peso en kg
    'altura': float,         # Altura en metros
    'imc': float,            # Valor del IMC calculado
    'categoria': str,        # Categoría del IMC
    'descripcion': str,      # Descripción en español
    'error': str            # Mensaje de error si ocurre
}
```

## Ejecución de Especificaciones

### Con pytest-bdd

```bash
pytest features/ -v
```

### Con behave

```bash
behave features/
```

## Ventajas del enfoque BDD

1. **Legibilidad**: Los escenarios se pueden entender sin conocimiento técnico
2. **Documentación**: Los escenarios sirven como documentación viva
3. **Trazabilidad**: Cada requisito tiene un escenario de prueba
4. **Colaboración**: Facilita la comunicación entre desarrolladores y stakeholders

## Cobertura de Requisitos

| Requisito | Escenarios | Estado |
|-----------|-----------|--------|
| Calcular IMC | 1, 2, 3, 4 | ✅ |
| Validar peso positivo | 5 | ✅ |
| Validar altura positiva | 6 | ✅ |
| Validar altura máxima | 7 | ✅ |
| Validar peso máximo | 8 | ✅ |

## Referencias

- [Gherkin Reference](https://cucumber.io/docs/gherkin/)
- [pytest-bdd Documentation](https://pytest-bdd.readthedocs.io/)
- [OMS - Índice de Masa Corporal](https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight)
