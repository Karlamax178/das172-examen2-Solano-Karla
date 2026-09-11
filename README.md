# Auditoría y Balance Matricial de Distribución de Carga en Bahía de Aeronave (AeroCargo-Matrix)
#das172-examen2-Solano-Karla

#Importancia operativa del balance de masa y la capacidad de piso en una aeronave.

En la industria aeronáutica, la correcta estiba y distribución del peso en la bodega de carga (cargo hold) es fundamental por dos razones operativas y estructurales principales: 

*Capacidad y Resistencia del piso:* Cada compartimiento del piso de carga tolera un peso máximo por unidad de área. El hecho de sobrepasar este límite estructural compromete la integridad del fuselaje y puede ocasionar deformaciones permanentes o fallas mecánicas en vuelo que serían muy catastróficas. 

*Balance y Simetría Lateral/Longitudinal:* Esta tiene que ver más por el lado aerodinámico. Para mantener la estabilidad aerodinámica y la maniobrabilidad de la aeronave, el centro de gravedad debe permanecer dentro de límites seguros. Un desbalance entre babor (izquierda) y estribor (derecha), o a lo largo del eje longitudinal, genera momentos de inclinación que dificultan el control del avión y aumentan el consumo de combustible. 

Para resolver esta problemática, la bodega de la aeronave se modelará como una matriz bidimensional de N x M que permitrá auditar computacionalmente los porcentajes de ocupación, validar el desbalance lateral y localizar regiones con sobrecarga crítica.
