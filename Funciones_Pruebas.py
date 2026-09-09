from funciones import (
    validar_matrices,
    ocupacion_sobrecarga,
    balance_simetria,
    ext_submatriz_critica
)

def hacer_pruebas():
    print(" INICIANDO PRUEBAS UNITARIAS Y CASOS BORDE SOLICITADOS EN EL EXAMEN ")
    print("---------------------------------------------------------------------\n")

    # PRUEBA 1: Caso Normal
    # ----------------------------------------------------
    cargas_tipicas = [[100.0, 200.0], [50.0, 150.0]]
    capacidades_tipicas = [[200.0, 200.0], [100.0, 150.0]]
    
    valido = validar_matrices(cargas_tipicas, capacidades_tipicas)
    assert valido == True, "Error en Prueba 1: Debería ser True para matrices válidas"
    print("Prueba 1 Pasada: Validación con caso normal correcto.")
