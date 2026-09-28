exce= 0
ruim= 0

for num in range(1,11):
    print(f"Entrevistado {num}")
    nome= input("Digite seu nome:")
    idade= int(input("Digite sua idade:"))
    nota= input("Como você avalia seu atendimento? (Excelente, Bom, Ruim.):")
   
    while nota not in ["Excelente", "Bom", "Ruim"]:
     print("Opção inválida. Por favor, digite uma das opções: Excelente, Bom, Ruim.")
     nota= input("Como você avalia seu atendimento? (Excelente, Bom, Ruim.):")


    if nota == "Excelente":
        exce += 1
    elif nota == "Ruim":
        ruim += 1

print(f"Total de avaliações Excelentes: {exce}")
print(f"Total de avaliações Ruins: {ruim}")