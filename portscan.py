#!/usr/bin/python3

#So vai ter saida de portas abertas
#Implementei um Banner Grabbing

import socket
import sys

if (len(sys.argv)) <=1:
	print (f"Informe o ip no primeiro argumento")

else:
	ip = sys.argv[1]

	for porta in range(1,65535):
		meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		res = meusocket.connect_ex((ip,porta)
		if (res == 0):
			banner = meusocket.recv(1024)
			print(f"porta {porta} Aberta!")
			print (banner)
		#else:
			#print(f"porta {porta} Fechada!")
