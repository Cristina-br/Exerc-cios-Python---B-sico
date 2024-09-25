largura_parede = float(input("Digite a largura da sua parede: "))
altura_parede = float(input("Digite a altura da sua parede: "))
area_parede = largura_parede * altura_parede
quantidade_tinta = area_parede / 2

print(f"A sua parede, de {largura_parede:.2f} metros de largura por {altura_parede:.2f} metros de altura, precisará de {quantidade_tinta:.2f} litros de tinta para ser coberta.")