# Auditoría y Balance Matricial de Distribución de Carga en Bahía de Aeronave (AeroCargo-Matrix)
das172-examen2-Solano-Karla

## Importancia operativa del balance de masa y la capacidad de piso en una aeronave.

En la industria aeronáutica, la correcta estiba y distribución del peso en la bodega de carga (cargo hold) es fundamental por dos razones operativas y estructurales principales: 

**Capacidad y Resistencia del piso:** Cada compartimiento del piso de carga tolera un peso máximo por unidad de área. El hecho de sobrepasar este límite estructural compromete la integridad del fuselaje y puede ocasionar deformaciones permanentes o fallas mecánicas en vuelo que serían muy catastróficas. 

**Balance y Simetría Lateral/Longitudinal:** Esta tiene que ver más por el lado aerodinámico. Para mantener la estabilidad aerodinámica y la maniobrabilidad de la aeronave, el centro de gravedad debe permanecer dentro de límites seguros. Un desbalance entre babor (izquierda) y estribor (derecha), o a lo largo del eje longitudinal, genera momentos de inclinación que dificultan el control del avión y aumentan el consumo de combustible. 

Para resolver esta problemática, la bodega de la aeronave se modelará como una matriz bidimensional de N x M que permitrá auditar computacionalmente los porcentajes de ocupación, validar el desbalance lateral y localizar regiones con sobrecarga crítica.


## Diagrama de Flujo y Arquitectura Modular

## Arquitectura Modular del Sistema

## Arquitectura Modular del Sistema

```mermaid
flowchart TD
    A[main.py: Script Principal] -->|Envía cargas y capacidades| B[funciones.py: Módulo de Funciones]
    B -->|Retorna resultados de auditoría| A
    C[test_funciones.py: Pruebas] -->|Verifica casos límite| B

    subgraph Funciones en funciones.py
        F1[1. matrices: Valida dimensiones y datos]
        F2[2. ocupacion_sobrecarga: Calcula % y detecta sobrecargas]
        F3[3. balance_simetria: Calcula pesos por fila y desbalance lateral]
        F4[4. ext_submatriz_critica: Busca la submatriz k x p con mayor carga]
    end

## Análisis de Complejidad Computacional

**Tiempo de Ejecución: O (N X M)**
Para auditar la bodega del avión, nuestras funciones recorren la cuadrícula fila por fila y columna por columna usando bucles `for` anidados. Si la matriz tiene n filas y m columnas, el código realiza exactamente $N \times M$ operaciones (visita cada celda una sola vez para validar pesos y calcular porcentajes). 
Por lo tanto, el tiempo que tarda el programa en ejecutarse crece de manera directa y proporcional al número total de celdas de la bodega.

** Uso de Memoria (Espacio):**
Al calcular la ocupación de la carga, la función crea una nueva matriz para guardar los porcentajes sin modificar las matrices originales. Esta nueva matriz requiere el mismo tamaño que la bodega (n filas por m columnas), por lo que la cantidad de memoria que consume el programa en la computadora es exactamente proporcional al tamaño total de la matriz NxM

