#Programa Tablas de Multiplicar

for x in range (1,11):				
	print("Tabla del " + str(x))
	print("------------")	
	for y in range (1,11):
		Result = x*y
		print(str(x) + " por " + str(y) + " es: " + str(Result))
