distancia = float(input("Uma distância em metros: "))

print(f"A medida de {distancia:.2f}m corresponde a")
print(f"{(distancia / 1000):.3f}Km \n{(distancia / 100):.2f}hm \n{(distancia / 10):.1f}dam")
print(f"{(distancia * 10):.0f}dm \n{(distancia * 100):.0f}cm \n{(distancia * 1000):.0f}mm")

