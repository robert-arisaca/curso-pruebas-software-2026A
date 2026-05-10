Feature: Calculate Body Mass Index
  As a user
  I want to calculate my Body Mass Index (BMI)
  To know my health status

  Scenario: Calculate BMI for a person with normal weight
    Given I have a weight of 70 kg
    And I have a height of 1.75 m
    When I calculate my BMI
    Then my BMI is 22.86
    And my category is peso_normal
    And my description is Peso normal

  Scenario: Calculate BMI for a person with overweight
    Given I have a weight of 90 kg
    And I have a height of 1.75 m
    When I calculate my BMI
    Then my BMI is 29.39
    And my category is sobrepeso
    And my description is Sobrepeso

  Scenario: Calculate BMI for a person with underweight
    Given I have a weight of 50 kg
    And I have a height of 1.75 m
    When I calculate my BMI
    Then my BMI is 16.33
    And my category is bajo_peso
    And my description is Bajo peso

  Scenario: Calculate BMI for a person with obesity
    Given I have a weight of 120 kg
    And I have a height of 1.75 m
    When I calculate my BMI
    Then my BMI is 39.18
    And my category is obesidad
    And my description is Obesidad

  Scenario: Validate that weight must be positive
    Given I have a weight of -5 kg
    And I have a height of 1.75 m
    When I try to calculate my BMI
    Then I get an error saying "El peso debe ser un número positivo"

  Scenario: Validate that height must be positive
    Given I have a weight of 70 kg
    And I have a height of -1.75 m
    When I try to calculate my BMI
    Then I get an error saying "La altura debe ser un número positivo"

  Scenario: Validate that height is not greater than 2 meters
    Given I have a weight of 70 kg
    And I have a height of 2.5 m
    When I try to calculate my BMI
    Then I get an error saying "La altura debe ser menor a 2 metros"

  Scenario: Validate that weight is not greater than 150 kg
    Given I have a weight of 160 kg
    And I have a height of 1.75 m
    When I try to calculate my BMI
    Then I get an error saying "El peso debe ser menor a 150 kg"
