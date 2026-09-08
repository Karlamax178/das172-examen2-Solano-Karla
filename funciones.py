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
  
  
