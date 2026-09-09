from funciones import (
    validar_matrices,
    ocupacion_sobrecarga,
    balance_simetria,
    ext_submatriz_critica
)

def hacer_pruebas():
    print(" INICIANDO PRUEBAS UNITARIAS Y CASOS BORDE SOLICITADOS EN EL EXAMEN ")
    print("---------------------------------------------------------------------\n")

    # PRUEBA 1: Caso Típico
    # ----------------------------------------------------
    cargas_tipicas = [[100.0, 200.0], [50.0, 150.0]]
    capacidades_tipicas = [[200.0, 200.0], [100.0, 150.0]]
    
    valido = validar_matrices(cargas_tipicas, capacidades_tipicas)
    assert valido == True, "Error en Prueba 1: Debería ser True para matrices válidas"
    print("Prueba 1 Pasada con Éxito: Validación con caso normal correcto.")
   
    # PRUEBA 2: Caso Borde - Pesos  que son negativos
    # ----------------------------------------------------
    cargas_negativas = [[-15.0, 200.0], [50.0, 150.0]]
    valido_negativo = validar_matrices(cargas_negativas, capacidades_tipicas)
    assert valido_negativo == False, "Error en Prueba 2: Debería detectar el peso negativo"
    print("Prueba 2 Pasada con Éxito : Rechaza correctamente pesos negativos.")

    # PRUEBA 3: Caso Borde - Dimensiones Mínimas (2x2) y Sobrecarga
    # ----------------------------------------------------
    cargas_limite = [[270.0, 100.0], [50.0, 80.0]] # Celda (0,0) sobrecargada (250/200 = 125%)
    capacidades_limite = [[200.0, 200.0], [100.0, 100.0]]
    
    porcentajes, sobrecargas = ocupacion_sobrecarga(cargas_limite, capacidades_limite)
    assert (0, 0) in sobrecargas, "Error en Prueba 3: Debería detectar la celda (0,0) en sobrecarga"
    print("Prueba 3 Pasada con Éxito: Detecta correctamente sobrecarga en matriz mínima 2x2.")

    # PRUEBA 4: Caso Borde - Columnas Impares en Balance Lateral
    # ----------------------------------------------------
    # Matriz 2x3: La columna central (índice 1) debe ser ignorada en el balance
    cargas_impares = [
        [100.0, 999.0, 100.0], 
        [50.0,  888.0, 50.0]  
    ]
    # Suma Izquierda = 150 kg | Suma Derecha = 150 kg -> Desbalance = 0 kg
    _, desbalance, balanceado = balance_simetria(cargas_impares, tol_desbalance=10.0)
    assert desbalance == 0.0, "Error en Prueba 4: La columna central impar no fue ignorada"
    assert balanceado == True, "Error en Prueba 4: Debería estar balanceado"
    print("Prueba 4 Pasada con Éxito: Omite de manera correca la columna central en matrices impares.")

    # PRUEBA 5: Caso Borde - Submatriz fuera de rango
    # ----------------------------------------------------
    # Solicitar submatriz 3x3 en una matriz que solo mide 2x2
    submatriz = ext_submatriz_critica([[100.0, 100.0], [100.0, 100.0]], k=3, p=3)
    assert submatriz == [], "Error en Prueba 5: Debería retornar lista vacía si la ventana excede el tamaño"
    print("Prueba 5 Pasada con Éxito: Maneja adecuadamente tamaños de ventana fuera de rango.")

    print("\n--------------------------------------------------------")
    print(" ¡TODAS LAS PRUEBAS SE EJECUTARON DE MANERA EXITOSA :D !")
   

if _name_ == "__main__":
    hacer_pruebas()
