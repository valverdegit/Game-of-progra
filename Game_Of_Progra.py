monto= float(input("Ingrese el monto que desea solicitar: "))
plazo= int(input("Ingrese un plazo de 6 a 60 meses: "))
intereses_anuales= 0.20
intereses_mensuales= intereses_anuales/ 12

cuotaMensual = (monto/plazo) = intereses_mensuales
mesesCorrecto=True
while mesesCorrecto==True:
    plazoMeses=int(input("Porfavor digite el tiempo en meses que desea que dure el prestamo:\nSolose permiten entre 6 y 60"))
    if plazoMeses>=6 and plazoMeses<=60:
        mesesCorrecto=False
    else:
        print("Porfavor indique un plazo entre 6 meses y 60 meses")
