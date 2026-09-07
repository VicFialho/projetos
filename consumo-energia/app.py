aparelho=(input("Digite o nome do aparelho:"))

potencia= float (input("Digite a potência do aparelho:"))

uso= float (input("Digite o tempo médio de uso diário do aparelho em horas:"))

consumomensal= (potencia * uso * 30) / 1000

print(f"O eletrodómestico {aparelho} tem um consumo mensal do aparelho é de: {consumomensal} kWh")