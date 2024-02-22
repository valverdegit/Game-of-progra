monto= float(input("Ingrese el monto que desea solicitar: "))
interes_anuales= 0.20
intereses_mensuales= (monto/12)*interes_anuales

mesesCorrecto=True
while mesesCorrecto==True:
    plazoMeses=int(input("Porfavor digite el tiempo en meses que desea que dure el prestamo:\nSolose permiten entre 6 y 60"))
    if plazoMeses>=6 and plazoMeses<=60:
        mesesCorrecto=False
    else:
        print("Porfavor indique un plazo entre 6 meses y 60 meses")
cuotaMensual = (monto/plazoMeses) + intereses_mensuales

print(f"El monto total a pagar es de: ₡{cuotaMensual* plazoMeses}")
