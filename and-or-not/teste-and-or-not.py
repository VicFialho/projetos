imovel = input("Digite o tipo de imóvel (Comercial, Casa, Apartamento):")

while (imovel == "Comercial" or imovel == "Casa" or imovel == "Apartamento") == False:
    imovel = input("Tipo de imóvel não reconhecido. Digite 'Comercial', 'Casa' ou 'Apartamento':") 
else:
    consumoagua = float(input("Digite o consumo de água mensal em metros cúbicos:"))

if imovel == "Comercial":
    print("Tarifa de imóvel comercial aplicada. Consulte o plano corporativo.")

elif (imovel == "Casa" or imovel == "Apartamento") and consumoagua < 10:
    print("Consumo mensal baixo, excelente economia de água!!")
elif (imovel == "Casa" or imovel == "Apartamento") and consumoagua >= 11 and consumoagua <= 25:
    print("Consumo mensal moderado, dentro do padrão residencial!!")
elif (imovel == "Casa" or imovel == "Apartamento") and consumoagua > 25:
    print("Consumo excessivo, verifique o encanamento para possíveis vazamentos e adote medidas de economia de água!!")
