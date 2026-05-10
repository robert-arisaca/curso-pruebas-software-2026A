"""
Configuración de pytest para las pruebas de BDD.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest
from pytest_bdd import given, when, then, parsers
from imc import IMCCalculator


# Fixtures para almacenar el estado de la prueba
@pytest.fixture
def contexto():
    """Contexto para almacenar datos durante la prueba."""
    return {
        'peso': None,
        'altura': None,
        'imc': None,
        'categoria': None,
        'descripcion': None,
        'error': None
    }


# Steps GIVEN
@given(parsers.parse('I have a weight of {peso} kg'))
def step_weight(contexto, peso):
    """Almacena el peso en el contexto."""
    contexto['peso'] = float(peso)


@given(parsers.parse('I have a height of {altura} m'))
def step_height(contexto, altura):
    """Almacena la altura en el contexto."""
    contexto['altura'] = float(altura)


# Steps WHEN
@when('I calculate my BMI')
def step_calculate_bmi(contexto):
    """Calcula el IMC."""
    try:
        contexto['imc'] = IMCCalculator.calcular_imc(
            contexto['peso'],
            contexto['altura']
        )
        contexto['categoria'] = IMCCalculator.clasificar_imc(contexto['imc'])
        contexto['descripcion'] = IMCCalculator.obtener_descripcion(
            contexto['categoria']
        )
    except ValueError as e:
        contexto['error'] = str(e)


@when('I try to calculate my BMI')
def step_try_calculate_bmi(contexto):
    """Intenta calcular el IMC y captura errores."""
    try:
        contexto['imc'] = IMCCalculator.calcular_imc(
            contexto['peso'],
            contexto['altura']
        )
        contexto['categoria'] = IMCCalculator.clasificar_imc(contexto['imc'])
        contexto['descripcion'] = IMCCalculator.obtener_descripcion(
            contexto['categoria']
        )
    except ValueError as e:
        contexto['error'] = str(e)


# Steps THEN
@then(parsers.parse('my BMI is {imc_esperado}'))
def step_verify_bmi(contexto, imc_esperado):
    """Verifica que el IMC calculado sea correcto."""
    assert contexto['imc'] == float(imc_esperado), \
        f"IMC esperado {imc_esperado}, obtenido {contexto['imc']}"


@then(parsers.parse('my category is {categoria_esperada}'))
def step_verify_category(contexto, categoria_esperada):
    """Verifica que la categoría sea correcta."""
    assert contexto['categoria'] == categoria_esperada, \
        f"Categoría esperada {categoria_esperada}, obtenida {contexto['categoria']}"


@then(parsers.parse('my description is {descripcion_esperada}'))
def step_verify_description(contexto, descripcion_esperada):
    """Verifica que la descripción sea correcta."""
    assert contexto['descripcion'] == descripcion_esperada, \
        f"Descripción esperada {descripcion_esperada}, obtenida {contexto['descripcion']}"


@then(parsers.parse('I get an error saying "{mensaje_esperado}"'))
def step_verify_error(contexto, mensaje_esperado):
    """Verifica que se obtenga el error esperado."""
    assert contexto['error'] is not None, "Se esperaba un error pero no ocurrió"
    assert contexto['error'] == mensaje_esperado, \
        f"Error esperado: {mensaje_esperado}, obtenido: {contexto['error']}"
