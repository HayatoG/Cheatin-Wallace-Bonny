#!/usr/bin/python3.5
import subprocess

listing = subprocess.check_output(["ls", "-la", "/home/goliveira/" ])

month = input("Insira o Mes a ser buscado (minusculo): ")

#Mes maiusculo para o VSCODE
#Mes minusculo diretamente no terminal
#month = "Jan"
#month = "jan"
print("\n")
if 'month' != None:
    print("Passou do IF")
    for line in listing.decode('utf-8').split('\n'):
        #print(month)
        #full = line.decode('utf-8')
        #print(line)
        if month in line:
            print("User *"+(line)[14:23]+"* alterou os arquivos: "+(line)[56:90]+" às "+(line)[50:55]+" horas.")
            #print("Hora: "+(line)[50:55])
            #print("Arquivo: "+(line)[56:90])