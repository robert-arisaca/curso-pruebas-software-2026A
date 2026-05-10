"""
Módulo para calcular el Índice de Masa Corporal (IMC).

Este módulo proporciona funcionalidades para calcular el IMC de una persona
basado en su peso (en kilogramos) y altura (en metros), y clasificar el
resultado según los estándares de la OMS.
"""


class IMCCalculator:
    """Clase para calcular el Índice de Masa Corporal."""

    # Rango de categorías IMC según la OMS
    CATEGORIAS = {
        'bajo_peso': (0, 18.5),
        'peso_normal': (18.5, 25.0),
        'sobrepeso': (25.0, 30.0)
    }

    @staticmethod
    def validar_entrada(peso: float, altura: float) -> tuple[bool, str]:
        """
        Valida que el peso y altura sean valores válidos.

        Args:
            peso: Peso en kilogramos (debe ser positivo)
            altura: Altura en metros (debe ser positivo)

        Returns:
            Tupla (es_válido, mensaje_error)
        """
        if not isinstance(peso, (int, float)) or peso <= 0:
            return False, "El peso debe ser un número positivo"

        if not isinstance(altura, (int, float)) or altura <= 0:
            return False, "La altura debe ser un número positivo"

        if altura > 2:
            return False, "La altura debe ser menor a 2 metros"

        if peso > 150:
            return False, "El peso debe ser menor a 150 kg"

        return True, ""

    @staticmethod
    def calcular_imc(peso: float, altura: float) -> float:
        """
        Calcula el Índice de Masa Corporal.

        Formula: IMC = peso (kg) / (altura (m) ** 2)

        Args:
            peso: Peso en kilogramos
            altura: Altura en metros

        Returns:
            El valor del IMC redondeado a 2 decimales

        Raises:
            ValueError: Si el peso o altura no son válidos
        """
        es_valido, mensaje_error = IMCCalculator.validar_entrada(
            peso, altura
        )
        if not es_valido:
            raise ValueError(mensaje_error)

        imc = peso / (altura ** 2)
        return round(imc, 2)

    @staticmethod
    def clasificar_imc(imc: float) -> str:
        """
        Clasifica el IMC según los estándares de la OMS.

        Args:
            imc: Valor del IMC calculado

        Returns:
            La categoría del IMC como string:
            - 'bajo_peso'
            - 'peso_normal'
            - 'sobrepeso'
            - 'obesidad'

        Raises:
            ValueError: Si el IMC es negativo
        """
        if imc < 0:
            raise ValueError("El IMC no puede ser negativo")

        for categoria, (minimo, maximo) in IMCCalculator.CATEGORIAS.items():
            if minimo <= imc < maximo:
                return categoria

        return 'obesidad'

    @staticmethod
    def obtener_descripcion(categoria: str) -> str:
        """
        Obtiene una descripción en español de la categoría de IMC.

        Args:
            categoria: La categoría del IMC

        Returns:
            Descripción en español de la categoría

        Raises:
            ValueError: Si la categoría no es válida
        """
        descripciones = {
            'bajo_peso': 'Bajo peso',
            'peso_normal': 'Peso normal',
            'sobrepeso': 'Sobrepeso',
            'obesidad': 'Obesidad'
        }

        if categoria not in descripciones:
            raise ValueError(f"Categoría inválida: {categoria}")

        return descripciones[categoria]

    @classmethod
    def evaluar_imc_completo(
        cls,
        peso: float,
        altura: float
    ) -> dict:
        """
        Realiza una evaluación completa del IMC.

        Args:
            peso: Peso en kilogramos
            altura: Altura en metros

        Returns:
            Diccionario con:
            - 'imc': valor del IMC
            - 'categoria': categoría del IMC
            - 'descripcion': descripción en español

        Raises:
            ValueError: Si el peso o altura no son válidos
        """
        imc = cls.calcular_imc(peso, altura)
        categoria = cls.clasificar_imc(imc)
        descripcion = cls.obtener_descripcion(categoria)

        return {
            'imc': imc,
            'categoria': categoria,
            'descripcion': descripcion
        }
