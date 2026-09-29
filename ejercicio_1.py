temperatura = [18, 25, 31, 12, 28, 35, 20]
contador_dias_frios = 0
contador_dias_templados = 0
contador_dias_calurosos = 0

for temp in temperatura:
    if temp < 15:
        print(f"{temp}: fria")
        contador_dias_templados  +=1

    elif 15 <= temp <= 25:
        print(f"{temp}: templada")
        contador_dias_templados +=1

    else:
        print(f"{temp}: calurosa")
        contador_dias_calurosos +=1

        print(f"total de dias frios: {contador_dias_frios}, total de dias templados: {contador_dias_templados}, total de dias calurosos: {contador_dias_calurosos}")