"""
Pruebas unitarias para el módulo IMCCalculator.

Proporciona cobertura completa (100%) de todas las funciones
y casos de uso del módulo imc.py.
"""

import pytest
from imc import IMCCalculator


class TestValidarEntrada:
    """Pruebas para la validación de entrada."""

    def test_validar_entrada_valores_validos(self):
        """Prueba que valores válidos pasen la validación."""
        es_valido, mensaje = IMCCalculator.validar_entrada(70, 1.75)
        assert es_valido is True
        assert mensaje == ""

    def test_validar_entrada_peso_negativo(self):
        """Prueba que peso negativo sea rechazado."""
        es_valido, mensaje = IMCCalculator.validar_entrada(-70, 1.75)
        assert es_valido is False
        assert mensaje == "El peso debe ser un número positivo"

    def test_validar_entrada_peso_cero(self):
        """Prueba que peso cero sea rechazado."""
        es_valido, mensaje = IMCCalculator.validar_entrada(0, 1.75)
        assert es_valido is False
        assert mensaje == "El peso debe ser un número positivo"

    def test_validar_entrada_peso_no_numerico(self):
        """Prueba que peso no numérico sea rechazado."""
        es_valido, mensaje = IMCCalculator.validar_entrada("70", 1.75)
        assert es_valido is False
        assert mensaje == "El peso debe ser un número positivo"

    def test_validar_entrada_altura_negativa(self):
        """Prueba que altura negativa sea rechazada."""
        es_valido, mensaje = IMCCalculator.validar_entrada(70, -1.75)
        assert es_valido is False
        assert mensaje == "La altura debe ser un número positivo"

    def test_validar_entrada_altura_cero(self):
        """Prueba que altura cero sea rechazada."""
        es_valido, mensaje = IMCCalculator.validar_entrada(70, 0)
        assert es_valido is False
        assert mensaje == "La altura debe ser un número positivo"

    def test_validar_entrada_altura_no_numerica(self):
        """Prueba que altura no numérica sea rechazada."""
        es_valido, mensaje = IMCCalculator.validar_entrada(70, "1.75")
        assert es_valido is False
        assert mensaje == "La altura debe ser un número positivo"

    def test_validar_entrada_altura_mayor_2_metros(self):
        """Prueba que altura mayor a 2 metros sea rechazada."""
        es_valido, mensaje = IMCCalculator.validar_entrada(70, 2.5)
        assert es_valido is False
        assert mensaje == "La altura debe ser menor a 2 metros"

    def test_validar_entrada_altura_exactamente_2_metros(self):
        """Prueba que altura de exactamente 2 metros sea válida."""
        es_valido, mensaje = IMCCalculator.validar_entrada(70, 2.0)
        assert es_valido is True
        assert mensaje == ""

    def test_validar_entrada_peso_mayor_150_kg(self):
        """Prueba que peso mayor a 150 kg sea rechazado."""
        es_valido, mensaje = IMCCalculator.validar_entrada(160, 1.75)
        assert es_valido is False
        assert mensaje == "El peso debe ser menor a 150 kg"

    def test_validar_entrada_peso_exactamente_150_kg(self):
        """Prueba que peso de exactamente 150 kg sea válido."""
        es_valido, mensaje = IMCCalculator.validar_entrada(150, 1.75)
        assert es_valido is True
        assert mensaje == ""


class TestCalcularIMC:
    """Pruebas para la función calcular_imc."""

    def test_calcular_imc_peso_normal(self):
        """Prueba el cálculo de IMC para peso normal."""
        imc = IMCCalculator.calcular_imc(70, 1.75)
        assert imc == 22.86

    def test_calcular_imc_sobrepeso(self):
        """Prueba el cálculo de IMC para sobrepeso."""
        imc = IMCCalculator.calcular_imc(90, 1.75)
        assert imc == 29.39

    def test_calcular_imc_bajo_peso(self):
        """Prueba el cálculo de IMC para bajo peso."""
        imc = IMCCalculator.calcular_imc(50, 1.75)
        assert imc == 16.33

    def test_calcular_imc_obesidad(self):
        """Prueba el cálculo de IMC para obesidad."""
        imc = IMCCalculator.calcular_imc(120, 1.75)
        assert imc == 39.18

    def test_calcular_imc_redondea_a_2_decimales(self):
        """Prueba que el IMC se redondea a 2 decimales."""
        imc = IMCCalculator.calcular_imc(70, 1.73)
        assert len(str(imc).split('.')[-1]) <= 2

    def test_calcular_imc_peso_invalidro_lanza_error(self):
        """Prueba que peso inválido lanza ValueError."""
        with pytest.raises(ValueError) as exc_info:
            IMCCalculator.calcular_imc(-70, 1.75)
        assert "El peso debe ser un número positivo" in str(exc_info.value)

    def test_calcular_imc_altura_invalida_lanza_error(self):
        """Prueba que altura inválida lanza ValueError."""
        with pytest.raises(ValueError) as exc_info:
            IMCCalculator.calcular_imc(70, -1.75)
        assert "La altura debe ser un número positivo" in str(exc_info.value)

    def test_calcular_imc_altura_muy_grande_lanza_error(self):
        """Prueba que altura muy grande lanza ValueError."""
        with pytest.raises(ValueError) as exc_info:
            IMCCalculator.calcular_imc(70, 2.5)
        assert "La altura debe ser menor a 2 metros" in str(exc_info.value)

    def test_calcular_imc_peso_muy_grande_lanza_error(self):
        """Prueba que peso muy grande lanza ValueError."""
        with pytest.raises(ValueError) as exc_info:
            IMCCalculator.calcular_imc(160, 1.75)
        assert "El peso debe ser menor a 150 kg" in str(exc_info.value)


class TestClasificarIMC:
    """Pruebas para la función clasificar_imc."""

    def test_clasificar_imc_bajo_peso_limite_inferior(self):
        """Prueba clasificación de bajo peso en límite inferior."""
        categoria = IMCCalculator.clasificar_imc(0.1)
        assert categoria == 'bajo_peso'

    def test_clasificar_imc_bajo_peso_limite_superior(self):
        """Prueba clasificación de bajo peso en límite superior."""
        categoria = IMCCalculator.clasificar_imc(18.49)
        assert categoria == 'bajo_peso'

    def test_clasificar_imc_peso_normal_limite_inferior(self):
        """Prueba clasificación de peso normal en límite inferior."""
        categoria = IMCCalculator.clasificar_imc(18.5)
        assert categoria == 'peso_normal'

    def test_clasificar_imc_peso_normal_limite_superior(self):
        """Prueba clasificación de peso normal en límite superior."""
        categoria = IMCCalculator.clasificar_imc(24.99)
        assert categoria == 'peso_normal'

    def test_clasificar_imc_sobrepeso_limite_inferior(self):
        """Prueba clasificación de sobrepeso en límite inferior."""
        categoria = IMCCalculator.clasificar_imc(25.0)
        assert categoria == 'sobrepeso'

    def test_clasificar_imc_sobrepeso_limite_superior(self):
        """Prueba clasificación de sobrepeso en límite superior."""
        categoria = IMCCalculator.clasificar_imc(29.99)
        assert categoria == 'sobrepeso'

    def test_clasificar_imc_obesidad_limite_inferior(self):
        """Prueba clasificación de obesidad en límite inferior."""
        categoria = IMCCalculator.clasificar_imc(30.0)
        assert categoria == 'obesidad'

    def test_clasificar_imc_obesidad_valor_alto(self):
        """Prueba clasificación de obesidad con valor alto."""
        categoria = IMCCalculator.clasificar_imc(50.0)
        assert categoria == 'obesidad'

    def test_clasificar_imc_negativo_lanza_error(self):
        """Prueba que IMC negativo lanza ValueError."""
        with pytest.raises(ValueError) as exc_info:
            IMCCalculator.clasificar_imc(-1)
        assert "El IMC no puede ser negativo" in str(exc_info.value)


class TestObtenerDescripcion:
    """Pruebas para la función obtener_descripcion."""

    def test_obtener_descripcion_bajo_peso(self):
        """Prueba descripción para bajo peso."""
        desc = IMCCalculator.obtener_descripcion('bajo_peso')
        assert desc == 'Bajo peso'

    def test_obtener_descripcion_peso_normal(self):
        """Prueba descripción para peso normal."""
        desc = IMCCalculator.obtener_descripcion('peso_normal')
        assert desc == 'Peso normal'

    def test_obtener_descripcion_sobrepeso(self):
        """Prueba descripción para sobrepeso."""
        desc = IMCCalculator.obtener_descripcion('sobrepeso')
        assert desc == 'Sobrepeso'

    def test_obtener_descripcion_obesidad(self):
        """Prueba descripción para obesidad."""
        desc = IMCCalculator.obtener_descripcion('obesidad')
        assert desc == 'Obesidad'

    def test_obtener_descripcion_invalida_lanza_error(self):
        """Prueba que categoría inválida lanza ValueError."""
        with pytest.raises(ValueError) as exc_info:
            IMCCalculator.obtener_descripcion('invalida')
        assert "Categoría inválida" in str(exc_info.value)


class TestEvaluarIMCCompleto:
    """Pruebas para la función evaluar_imc_completo."""

    def test_evaluar_imc_completo_peso_normal(self):
        """Prueba evaluación completa para peso normal."""
        resultado = IMCCalculator.evaluar_imc_completo(70, 1.75)
        assert resultado['imc'] == 22.86
        assert resultado['categoria'] == 'peso_normal'
        assert resultado['descripcion'] == 'Peso normal'

    def test_evaluar_imc_completo_sobrepeso(self):
        """Prueba evaluación completa para sobrepeso."""
        resultado = IMCCalculator.evaluar_imc_completo(90, 1.75)
        assert resultado['imc'] == 29.39
        assert resultado['categoria'] == 'sobrepeso'
        assert resultado['descripcion'] == 'Sobrepeso'

    def test_evaluar_imc_completo_bajo_peso(self):
        """Prueba evaluación completa para bajo peso."""
        resultado = IMCCalculator.evaluar_imc_completo(50, 1.75)
        assert resultado['imc'] == 16.33
        assert resultado['categoria'] == 'bajo_peso'
        assert resultado['descripcion'] == 'Bajo peso'

    def test_evaluar_imc_completo_obesidad(self):
        """Prueba evaluación completa para obesidad."""
        resultado = IMCCalculator.evaluar_imc_completo(120, 1.75)
        assert resultado['imc'] == 39.18
        assert resultado['categoria'] == 'obesidad'
        assert resultado['descripcion'] == 'Obesidad'

    def test_evaluar_imc_completo_retorna_diccionario(self):
        """Prueba que el resultado es un diccionario con las claves esperadas."""
        resultado = IMCCalculator.evaluar_imc_completo(70, 1.75)
        assert isinstance(resultado, dict)
        assert 'imc' in resultado
        assert 'categoria' in resultado
        assert 'descripcion' in resultado

    def test_evaluar_imc_completo_peso_invalido_lanza_error(self):
        """Prueba que peso inválido lanza ValueError."""
        with pytest.raises(ValueError):
            IMCCalculator.evaluar_imc_completo(-70, 1.75)

    def test_evaluar_imc_completo_altura_invalida_lanza_error(self):
        """Prueba que altura inválida lanza ValueError."""
        with pytest.raises(ValueError):
            IMCCalculator.evaluar_imc_completo(70, -1.75)
