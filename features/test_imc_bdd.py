"""
Pruebas BDD para el calculador de IMC usando pytest-bdd.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.dirname(__file__))

from pytest_bdd import scenarios
# Importar los pasos para que pytest-bdd los encuentre
import steps.imc_steps  # noqa: F401

# Cargar todos los escenarios del archivo feature
scenarios('calcular_imc.feature')
