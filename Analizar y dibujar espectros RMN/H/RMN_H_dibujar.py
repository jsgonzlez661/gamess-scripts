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
RMN_H_TMS =[]
suma_TMS = 0

lines = job_TMS.readlines()

for line in lines:
	cont = cont+1
	if(cont == aq_TMS):
		#uno = line
		SHIELDING_TMS = SHIELDING_TMS + line.split()
	if ("H         X" in line):
		aq_TMS=cont+3
		#print(val)

for i in range(0, len(SHIELDING_TMS)):		
	RMN_H_TMS.append(float(str(SHIELDING_TMS[i])))
	suma_TMS = RMN_H_TMS[i] + suma_TMS
	
valor_TMS = suma_TMS/len(RMN_H_TMS)
#print(valor_TMS)


job_TMS.close()

print()


log = input("Ingrese el nombre del archivo a revisar ") + '.log'
print()
job = open(log, 'r')

cont=0
SHIELDING = []
aq = 0
RMN_H =[]

lines = job.readlines()

for line in lines:
	cont = cont+1
	if(cont == aq):
		#uno = line
		SHIELDING = SHIELDING + line.split()
	if ("H         X" in line):
		aq=cont+3
		#print(val)
		
print('----------------------------------------------------------')
cadena = "Valores en ppm H " + log
print(                cadena.center(50, " ")                 )
print('----------------------------------------------------------')
print('----------------------------------------------------------')
	
for i in range(0, len(SHIELDING)):		
	RMN_H.append(float(str(SHIELDING[i])))
	if(RMN_H[i] <= valor_TMS):
		RMN_H[i] = valor_TMS - RMN_H[i]
	else: RMN_H[i] = RMN_H[i] - valor_TMS
	print("\t \t" + str(round(RMN_H[i],3)) + ' ppm         ')
	print()
	
print('----------------------------------------------------------')
#print(RMN_H)

job.close()

question = input("Quiere guardar estos valores y/n ")
if(question== 'y'):
	name = log.strip('.log')
	work = ("Valores en ppm H " + name) + '.txt'
	#print(work)
	doc = open(work , 'w')
	doc.write('ppm\n')
	RMN_H.sort(reverse=True)
	for i in range(0, len(RMN_H)):
		doc.write(str(round(RMN_H[i],3)))
		doc.write('\n')
	print(" \nLISTO ")
	doc.close()


#RMN_H.sort()

#x =[RMN_H[0],RMN_H[0]]
#y = [0, 1000]

#z =[RMN_H[1],RMN_H[1]]
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