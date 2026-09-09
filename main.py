#Probando mi código
from funciones import validar_matrices, ocupacion_sobrecarga

cargas = [
    [100.0, 230.0, 200.0],
    [75.0,  700.0, 120.0]
]

capacidades = [
    [100.0, 230.0, 200.0],
    [75.0,  700.0, 120.0]
]

print ("----PRUEBA DE CARGA----")

es_valida = validar_matrices(cargas, capacidades)
print(f"1. ¿Matrices son válidas y también coherentes?: {es_valida}")

if es_valida:
  porcentajes, sobrecargas = ocupacion_sobrecargas(cargas, capacidades)
  print ("\n2. Matriz de Ocupación (%):")
  for fila in porcentajes:
    print (" ", fila)

  print("\n3. Celdas que tienen una sobrecarga peligrosa (>100%):")
  print("   Coordenadas (Fila, Columna):", sobrecargas)

else:
    print("Error: Las matrices ingresadas no son válidas.")
