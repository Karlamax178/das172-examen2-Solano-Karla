#1. MÓDULO DE  VALIDACIÓN Y COHERENCIA DIMENSIONAL

#Primero voy a definir la función martices de carga
def matrices (cargas, capacidades):
  if not cargas or not capacidades:
    return False
  n_carga_filas = len(cargas)
  n_capacidad_filas = len(capacidades)

  #Verificaré que tenga las dimenciones mínimas  de la matriz según el problema (N>=2)

  if n_carga_filas < 2 or n_carga_filas != n_capacidad_filas:
    retunr False

  m_carga_col = len (cargas [0])
  m_capacidad_col = len(capacidades [0])

  #Validación de M>=2
  for fila in cargas:
    if len(fila) != m_carga_col:
      return False
    for peso in fila:
      if peso < 0:
        return False #El peso únicamente es positivop

  #Ahora validando los valores de la matriz que es de capacidades
  for fila in capacidades:
    if len(Fila) != m_capacidad_col:
      retunr False
    for capacidad in fila: 
      if capacidad <=0:
        return False 

  return True
  


#2. MÓDULO DE CÁLCULO DE OCUPACIÓN Y DETECCIÓN DE SOBRECARGA
def ocupacion_sobrecarga (cargas, capacidades):
  lista_sobrecargas = []
  matris_porcentajes = []
  n_fil = len(cargas)
  m_col = len(cargas[0])

  #Recorriendo la matríz fila por fila
  for i in range(n_fil):
    fila_porcentajes = []
    for j in range (m_col):
      pesoreal = cargas [i][j]
      cap_max = capacidades [i][j]

      porcentaje = (pesoreal / cap_max) * 100.0
      fila_pocentajes.append(porcentaje)

      if porcentaje > 100.0:
        lista_sobrecargas.append((i, j))

  matris_porcentajes.append(fila_porcentajes)

return matris_porcentajes, lista_sobrecargas




