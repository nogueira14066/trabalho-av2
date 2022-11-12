def converter_hora(hora):
    return hora

while True:
  hora = int(input("Hora: "))
  if hora == -1:
    break
  minuto = int(input("Minuto: "))

  if(hora<12):
   A  = (f"{hora}:{minuto} A.M.")
   print(A)

  elif(hora==12 and minuto<=59):
      P =(f"{12}:{minuto} P.M.")
      print(P)

  elif(hora==0):
      A =(f"{0}:{minuto} A.M.")
      print(A)

  else:
    hora = converter_hora(hora)
    P = (f"{hora-12}:{minuto} P.M.")
    print(P)