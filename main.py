#Probando mi código
from funciones import matrices, ocupacion_sobrecarga

cargas = [
    [100.0, 250.0, 200.0],
    [20.0,  300.0, 125.0]
]

capacidades = [
    [200.0, 200.0, 200.0],
    [100.0, 250.0, 150.0]
]

print ("----PRUEBA DE CARGA----")

es_valida = matrices(cargas, capacidades)
print(f"1. ¿Matrices son válidas y también coherentes?: {es_valida}")

if es_valida:
  porcentajes, sobrecargas = ocupacion_sobrecarga(cargas, capacidades)
  print ("\n2. Matriz de Ocupación (%):")
  for fila in porcentajes:
    print (" ", fila)


# Cargas de prueba (2 filas x 3 columnas -> impar)
cargas_ejemplo = [
    [100.0, 250.0, 200.0],  
    [50.0,  300.0, 120.0]   
]

tolerancia = 100.0  # Tolerancia máxima permitida en kg
longitudinales, desbalance, balanceado = balance_simetria(cargas_ejemplo, tolerancia)

print("--- RESULTADOS MÓDULO 3 ---")
print("Pesos longitudinales (por fila):", longitudinales) 
print(f"Desbalance lateral: {desbalance} kg")             
print("¿Está dentro de la tolerancia?:", balanceado)


# Matriz de porcentajes de ejemplo (2 filas x 3 columnas)
porcentajes_prueba = [
    [50.0, 125.0, 100.0],
    [50.0, 120.0,  80.0]
]

k = 2  # 2 filas
p = 2  # 2 columnas

submatriz = ext_submatriz_critica(porcentajes_prueba, k, p)

print("--- SUBMATRIZ CRÍTICA EXTRAÍDA (2x2) ---")
for fila in submatriz:
    print(fila)
  print("\n3. Celdas que tienen una sobrecarga peligrosa (>100%):")
  print("   Coordenadas (Fila, Columna):", sobrecargas)

else:
    print("Error: Las matrices ingresadas no son válidas.")
