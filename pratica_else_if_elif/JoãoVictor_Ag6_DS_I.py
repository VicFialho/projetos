compra=float(input("Digite o valor da compra em R$:"))
# Váriavel que define o valor da compra

desconto= (compra*0.05) if compra < 200 else (compra*0.10) if compra >= 200 and compra < 300 else (compra*0.15)
# Váriavel que define o valor do desconto de acordo com o valor da compra

if compra < 200:
    print(f"Parabéns!! Você ganhou um desconto de 5% em sua compra, oque deixa o valor final em R${desconto:.2f} reais")
elif compra >= 200 and compra < 300: 
    print(f"Parabéns!! Você ganhou um desconto de 10% em sua compra, oque deixa o valor final em R${desconto:.2f} reais")
else:
    print(f"Parabéns!! Você ganhou um desconto de 15% em sua compra, oque deixa o valor final em R${desconto:.2f} reais")
# Mostra para o usuário tanto o desconto quanto o valor final da compra após o desconto