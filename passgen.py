#!/usr/bin/python
from colorama import Fore, init
from data import *
import random
import os
init()

os.system('clear')

banner = """
 ######                                            
 #     #   ##    ####   ####   ####  ###### #    # 
 #     #  #  #  #      #      #    # #      ##   # 
 ######  #    #  ####   ####  #      #####  # #  # 
 #       ######      #      # #  ### #      #  # # 
 #       #    # #    # #    # #    # #      #   ## 
 #       #    #  ####   ####   ####  ###### #    # 
 """


def switch():
	print(Fore.YELLOW)
	print(banner)
	print("\n++++++ By Blackster +++++++")
	menu = """
1- Generar contraseña de 12 caracteres.
2- Generar contraseña de 16 caracteres.

00- salir del script.
"""
	print(Fore.CYAN)
	print(menu)

while True:
	switch()
	ask = int(input("Escoge una opcion:>> "))
	if ask==1:
		print(Fore.GREEN)
		generador_1()
		print("\nPresione enter para cotinuar")
		input()
		os.system('clear')

	elif ask==2:
		print(Fore.GREEN)
		generador_2()
		print("\nPresione enter para cotinuar")
		input()
		os.system('clear')

	else:
		if ask==00:
			print("See you")
			break