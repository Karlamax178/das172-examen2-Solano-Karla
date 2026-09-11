#Probando mi código
from funciones import matrices, ocupacion_sobrecarga, balance_simetria, ext_submatriz_critica

cargas = [
    [100.0, 250.0, 200.0],
    [20.0,  300.0, 125.0]
]

capacidades = [
    [200.0, 200.0, 200.0],
    [100.0, 250.0, 150.0]
]

print("----PRUEBA DE CARGA----")

es_valida = matrices(cargas, capacidades)
print(f"1. ¿Matrices son válidas y también coherentes?: {es_valida}")

if es_valida:
    # Módulo 2
    porcentajes, sobrecargas = ocupacion_sobrecarga(cargas, capacidades)
    print("\n2. Matriz de Ocupación (%):")
    for fila in porcentajes:
        print("  ", fila)
    print("   Celdas con sobrecarga (>100%):", sobrecargas)

    # Módulo 3
    tolerancia = 100.0
    longitudinales, desbalance, balanceado = balance_simetria(cargas, tolerancia)
    print("\n3. Resultados Módulo 3 (Balance):")
    print("   Pesos longitudinales:", longitudinales)
    print(f"   Desbalance lateral: {desbalance} kg")
    print("   ¿Está dentro de tolerancia?:", balanceado)

    # Módulo 4
    k = 2
    p = 2
    submatriz = ext_submatriz_critica(porcentajes, k, p)
    print("\n4. Submatriz Crítica Extraída (2x2):")
    for fila in submatriz:
        print("  ", fila)
else:
    print("Error: Las matrices ingresadas no son válidas.")
