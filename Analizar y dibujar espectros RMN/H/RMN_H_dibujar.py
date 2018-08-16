# Script python para lectura y analisis de valores de para RMN de 13 C apartir de archivos 
# .log generado por GAMESS

#Version 1.10

#import matplotlib.pyplot as plt

print()
log = input("Ingrese el archivo del TMS ") + '.log'

job_TMS = open(log, 'r')

cont=0
SHIELDING_TMS = []
aq_TMS = 0
RMN_13C_TMS =[]
suma_TMS = 0

lines = job_TMS.readlines()

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
	
valor_TMS = suma_TMS/len(RMN_13C_TMS)
#print(valor_TMS)


job_TMS.close()

print()


log = input("Ingrese el nombre del archivo a revisar ") + '.log'
print()
job = open(log, 'r')

cont=0
SHIELDING = []
aq = 0
RMN_13C =[]

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

question = input("Quiere guardar estos valores y/n ")
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
	print(" \nLISTO ")
	doc.close()


#RMN_13C.sort()

#x =[RMN_13C[0],RMN_13C[0]]
#y = [0, 1000]

#z =[RMN_13C[1],RMN_13C[1]]
#w = [0, 212]

#l = [-5,200]
#top = [0,0]
#plt.figure()
#plt.plot(x, y)
#plt.plot(z, w)
#plt.plot(l, top)
#plt.xlabel('ppm')
#plt.yticks([])
#plt.show()