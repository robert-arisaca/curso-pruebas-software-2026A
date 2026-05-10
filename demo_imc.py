"""
  Script de demostración interactivo del Calculador de IMC.
  """

from imc import IMCCalculator


def main():
      print("=" * 60)
      print("         CALCULADORA DE ÍNDICE DE MASA CORPORAL (IMC)")
      print("=" * 60)
      print()

      while True:
          try:
              peso = float(input("Ingresa tu peso (kg): "))
              altura = float(input("Ingresa tu altura (m): "))

              resultado = IMCCalculator.evaluar_imc_completo(peso, altura)

              print("\n" + "=" * 60)
              print(f"Tu IMC es: {resultado['imc']}")
              print(f"Categoría: {resultado['descripcion']}")
              print("=" * 60)
              print()

              otra = input("¿Calcular otro IMC? (s/n): ").lower()
              if otra != 's':
                  print("¡Gracias por usar la Calculadora de IMC!")
                  break

          except ValueError as e:
              print(f"❌ Error: {e}")
              print()


if __name__ == "__main__":
      main()