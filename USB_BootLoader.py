#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import datetime
import time
import sys

cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
amarelo= '\033[1;33m'
today = datetime.datetime.today()
t = today.strftime("[%H:%M:%S] - ")
os.system('clear')

banner = '''

╔╗─╔╦═══╦══╗─╔══╗──────╔╗╔╗──────────╔╗
║║─║║╔═╗║╔╗║─║╔╗║─────╔╝╚╣║──────────║║
║║─║║╚══╣╚╝╚╗║╚╝╚╦══╦═╩╗╔╣║──╔══╦══╦═╝╠══╦═╗  łαbørαŧøriø Ŧαηŧαรмα
║║─║╠══╗║╔═╗║║╔═╗║╔╗║╔╗║║║║─╔╣╔╗║╔╗║╔╗║║═╣╔╝  Coded By : łuŧЋ1єr
║╚═╝║╚═╝║╚═╝║║╚═╝║╚╝║╚╝║╚╣╚═╝║╚╝║╔╗║╚╝║║═╣║   Telegram : @DreadPirateRobertt
╚═══╩═══╩═══╝╚═══╩══╩══╩═╩═══╩══╩╝╚╩══╩══╩╝

+=========================+
| Default USB = /dev/sdc  |
+=========================+

'''
print amarelo + banner

def main():
	try:	
		iso = raw_input(vermelho+t+azul+'Digite o diretorio da ISO > ')
		print('')
		live = raw_input(vermelho+t+azul+'Deseja alterar o diretório UBS y/N >')
		print('')
		if live == 'n' or live == 'N':
			comand = "dd if="+iso+" of=/dev/sdc bs=4M && sync"
			time.sleep(0.5)
			print vermelho+t+verde+'Aguarde o Pendrive está sendo Bootado...'
			process = os.popen(comand)
			results = str(process.read())
			return vermelho+t+azulresults
		elif live == 'y' or live == 'Y':
			part = raw_input(vermelho+t+azul+'Digite o Diretorio da Partição > ')
			print('')
			comand = "dd if="+iso+" of="+part+" bs=4M && sync"
			time.sleep(0.5)
			print vermelho+t+verde+'Aguarde o Pendrive está sendo Bootado...'
			process = os.popen(comand)
			results = str(process.read())
			return vermelho+t+azulresults
	except KeyboardInterrupt:
		print('\n')
		print(vermelho + '[*] Exiting...')
		print('')
		sys.exit(1)
if __name__ == '__main__':
	main()

