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

  print("\n3. Celdas que tienen una sobrecarga peligrosa (>100%):")
  print("   Coordenadas (Fila, Columna):", sobrecargas)

else:
    print("Error: Las matrices ingresadas no son válidas.")
