#script de python para GAMESS 1.20 V

bienvenida = "    _____          __  __ ______  _____ _____'\n'"\
"  / ____|   /\   |  \/  |  ____|/ ____/ ____|'\n'"\
" | |  __   /  \  | \  / | |__  | (___| (___  '\n'"\
" | | |_ | / /\ \ | |\/| |  __|  \___ \\___ \ '\n'"\
" | |__| |/ ____ \| |  | | |____ ____) |___) |'\n'"\
"  \_____/_/    \_\_|  |_|______|_____/_____/ "
                                             
print(bienvenida)                                             

print()

import os
create_job = input("DESEA CREAR EL ARCHIVO DE TRABAJO y/n ")


if(create_job=='y'):
	work = input("INGRESE EL NOMBRE DEL ARCHIVO ") + '.txt'
	job = open(work , 'w')

	ready =input("CUANTOS ARCHIVOS A CALCULAR ")
	ready_go = int(ready)
	job.write(ready)
	job.write('\n')
	print("INGRESE LOS NOMBRES DE LOS ARCHIVOS A CALCULAR")
	for i in range(0, ready_go):
		job.write(input())
		job.write('\n')

	job.close()
else:
	#mostrar = input("QUIERE VER LO QUE HAY EN LA CARPETA y/n ")
	#if(mostrar  == 'y'):
	#	os.system('dir')
	print()
	work = input("INGRESE EL NOMBRE DEL ARCHIVO CON LOS DATOS DE ENTRADA ") + '.txt'
	
print()
	
lista = open(work, 'r')
hasta = int(lista.readline())


for i in range(0, hasta):
	example = lista.readline().strip('\n')
	run = 'rungms ' + example + ' > ' + example + '.log'
	#print(run)
	os.system(run)
	
lista.close()	
	

