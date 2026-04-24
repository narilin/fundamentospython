# Crear variables
john = 3
mary = 5
adam = 6

# Imprimir variables en una sola línea
print(john, mary, adam)

# Crear variable con la suma
total_apples = john + mary + adam

# Imprimir total
print(total_apples)

# Imprimir con texto
print("Numero total de manzanas:", total_apples)



manzanas_regaladas = 7
manzanas_comidas = 3


print("Manzanas regaladas:", manzanas_regaladas)
print("Manzanas comidas:", manzanas_comidas)


total_actual = total_apples + manzanas_regaladas - manzanas_comidas
print("Total actual de manzanas:", total_actual)


print("Mitad de las manzanas:", total_actual / 2)
print("Manzanas por persona (entero):", total_actual // 3)


promedio = total_actual / 3
print("Promedio por persona:", promedio)