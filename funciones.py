#1. MÓDULO DE  VALIDACIÓN Y COHERENCIA DIMENSIONAL

#Primero voy a definir la función martices de carga
def matrices (cargas, capacidades):
  if not cargas or not capacidades:
    return False
  n_carga_filas = len(cargas)
  n_capacidad_filas = len(capacidades)

  #Verificaré que tenga las dimenciones mínimas  de la matriz según el problema (N>=2)

  if n_carga_filas < 2 or n_carga_filas != n_capacidad_filas:
    return False

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
    if len(fila) != m_capacidad_col:
      return False
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
      fila_porcentajes.append(porcentaje)

      if porcentaje > 100.0:
        lista_sobrecargas.append((i, j))

  matris_porcentajes.append(fila_porcentajes)

  return matris_porcentajes, lista_sobrecargas

#3. MÓDULO DE EVALUACIÓN DE SIMETRIA Y BALANCE
#Ahora calculare el peso total por fila, el desbalance latera y si la distribución 
#del peso esta equilibrada correctamente
def balance_simetria(carga, tol_desbalance):
  n_fil = len(cargas)
  m_col = len(cargas[0])

  peso_longitudinales = []
  for fila in cargas:
    suma_fila = sum(fila)
    peso_longitudinales.append(suma_fila)

  mitad_col = m_col//2
  suma_izq = 0.0
  suma_der = 0.0

  for fila in cargas:
    for j in range (0, mitad_col):
      suma_izq += fila[j]
    inicio_der = mitad_col if (m_col % 2==0) else mitad_col +1
    for j in range (inicio_der, m_col):
      suma_der += fila[j]

  desbalance_lateral = abs(suma_izq - suma_der)
  esta_balanceado = desbalance_lateral <= tol_desbalance
  return peso_longitudinales, desbalance_lateral, esta_balanceado

#4. MÓDULO DE EXTRACCIÓN DE SUBMATRIZ DE SOBRECARGA CRÍTICAP

def ext_submatriz_critica(matris_porcentajes, k, p):
  n_fil = len(matris_porcentajes)
  m_col = len(matris_porcentajes[0])

  if k > n_fil or p > m_col:
    return []

  max_prom = -1.0
  submatriz_critica =[]

  for r in range (n_fil - k +1):
    for c in range (m_col - p +1):
      submatriz_actual=[]
      suma_porcentajes = 0.0

      for i in range (k):
        fila_sub = []
        for j in range (p):
          valor=matris_porcentajes [r+i][c+j]
          fila_sub.append(valor)
          suma_porcentajes += valor
        submatriz_actual.append(fila_sub)

      promedio_actual = suma_porcentajes/(k*p)
      if promedio_actual > max_prom:
        max_prom = promedio_actual
        submatriz_critica = submatriz_actual
    return submatriz_critica
      


