# Script python para lectura y analisis de valores de para RMN de 13 C apartir de archivos 
# .log generado por GAMESS

#Version 1.40

import matplotlib.pyplot as plt #libreria de python necesaria para elaborar la grafica

print()
log = input("Ingrese el nombre del archivo del TMS ") + '.log' #ingreso del archivo patron del TMS

job_TMS = open(log, 'r') #abrir archivo anterior

cont=0
SHIELDING_TMS = []
aq_TMS = 0
RMN_13C_TMS =[]
suma_TMS = 0

lines = job_TMS.readlines()
#Busqueda de los picos en el archivo del TMS
for line in lines:
	cont = cont+1
	if(cont == aq_TMS):
		#uno = line
		SHIELDING_TMS = SHIELDING_TMS + line.split()
	if ("C         X" in line):
		aq_TMS=cont+3
		#print(val)

for i in range(0, len(SHIELDING_TMS)):		
	RMN_13C_TMS.append(float(str(SHIELDING_TMS[i])))
	suma_TMS = RMN_13C_TMS[i] + suma_TMS
	
valor_TMS = suma_TMS/len(RMN_13C_TMS) #Promedio de los picos calculados
#print(valor_TMS)


job_TMS.close()

print()

repertir = "y" #Iniciar repeticion 

while (repertir != "n"): #Ciclo repertitivo para multiples archivos .log 

	log = input("Ingrese el nombre del archivo a revisar ") + '.log' #apertura del archivo a analizar
	print()
	job = open(log, 'r')

	cont=0
	SHIELDING = []
	aq = 0
	RMN_13C =[]

	#Lectura, analisis de los picos y la comparacion con los del TMS
	lines = job.readlines()
	for line in lines:
		cont = cont+1
		if(cont == aq):
			#uno = line
			SHIELDING = SHIELDING + line.split()
		if ("C         X" in line):
			aq=cont+3
			#print(val)
			
	print('----------------------------------------------------------')
	cadena = "Valores en ppm 13C " + log
	print(                cadena.center(50, " ")                 )
	print('----------------------------------------------------------')
	print('----------------------------------------------------------')
		
	for i in range(0, len(SHIELDING)):		
		RMN_13C.append(float(str(SHIELDING[i])))
		if(RMN_13C[i] <= valor_TMS):
			RMN_13C[i] = valor_TMS - RMN_13C[i]
		else: RMN_13C[i] = RMN_13C[i] - valor_TMS
		print("\t \t" + str(round(RMN_13C[i],3)) + ' ppm         ')
		print()
		
	print('----------------------------------------------------------')
	#print(RMN_13C)

	job.close()

	question = input("Quiere guardar estos valores y/n ") #Guardar los valores en un archivos .txt
	if(question== 'y'):
		name = log.strip('.log')
		work = ("Valores en ppm 13C " + name) + '.txt'
		#print(work)
		doc = open(work , 'w')
		doc.write('ppm\n')
		RMN_13C.sort(reverse=True)
		for i in range(0, len(RMN_13C)):
			doc.write(str(round(RMN_13C[i],3)))
			doc.write('\n')
		print(" \nLISTO\n ")
		doc.close()

	generar_grafica = input("Desea hacer la grafica y/n: ")

	if(generar_grafica == 'y'): #Crear Grafica

		print()
		RMN_13C.sort(reverse=True)

		
		for i in range(0, len(RMN_13C)): #Redondeo de los valores ppm 
			RMN_13C[i] = round(RMN_13C[i], 3) 

		data_ppm = RMN_13C
		data_intensidad = []

		#print(data_ppm)

		for i in range(0, len(data_ppm)): #ingreso de las intensidades necesarias para la construccion de la grafica 
			data_intensidad.append(float(input("Ingrese el valor de la intensidad para " + str(data_ppm[i]) + " ppm : ")))

		#print(data_ppm)
		#print(data_intensidad)

		posicion = 950
		#Dibujo de los picos en la grafica 
		for i in range(0 , len(data_ppm)):	
			x = [data_ppm[i], data_ppm[i]]
			y = [0 , data_intensidad[i]]
			lines_setp = plt.plot(x, y)
			plt.setp(lines_setp , color = 'k')
			plt.text(-50, 1000, "   ppm  ")
			plt.text(-50, posicion, str(data_ppm[i]))
		#	plt.text(-40, 1000, " " , bbox = dict(fc = "none"))
			posicion= posicion-50


		# dibujar linea base
		line_x = [0,220]
		line_y = [0,0]
		lines = plt.plot(line_x, line_y)
		plt.setp(lines , color = 'k')
		Titulo = "Espectro de Resonancia Magnetica Nuclear de C 13"
		plt.title(Titulo, fontsize = 14)
		plt.yticks([])
		plt.xlabel('ppm', fontsize = 12)
		plt.show()

	else: print("Grafica no creada\n")

	repertir = input("\nDesea repertir con otro archivo y/n: ")

print("Gracias por utilizar este programa\n")