#WRITTEN BY DX.RONI
#---------import---------#
import os
from os import system as clr
import random
#---------color---------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
my_color=[B,C,P,H]
warna=random.choice(my_color)
#---------logo---------#
logo=("""
\t\033[38;5;46m╔══════════════════════════════════╗
\t\033[38;5;46m║\033[38;5;46m███╗░░██╗\33[38;5;196m██╗\033[34;1m██╗░░██╗\033[38;5;46m░█████╗\33[38;5;196m░███╗░░██╗
\t\033[38;5;46m║\033[38;5;46m████╗░██║\33[38;5;196m██║\033[34;1m██║░░██║\033[38;5;46m██╔══██╗\033[38;5;46m████╗░██║
\t\033[38;5;46m║\033[38;5;46m██╔██╗██║\33[38;5;196m██║\033[34;1m███████║\033[38;5;46m███████║\33[38;5;196m██╔██╗██║
\t\033[38;5;46m║\033[38;5;46m██║╚████║\33[38;5;196m██║\033[34;1m██╔══██║\033[38;5;46m██╔══██║\033[38;5;46m██║╚████║
\t\033[38;5;46m║\033[38;5;46m██║░╚███║\33[38;5;196m██║\033[34;1m██║░░██║\033[38;5;46m██║░░██║\33[38;5;196m██║░╚███║
\t\033[38;5;46m║\033[38;5;46m╚═╝░░╚══╝\33[38;5;196m╚═╝\033[34;1m╚═╝░░╚═╝\033[38;5;46m╚═╝░░╚═╝\033[38;5;46m╚═╝░░╚══╝
\t\033[38;5;46m║
\t\033[38;5;46m╚══════════════════════════════════╝
\33[38;5;196m     ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46m𝗚𝗫\33[38;5;196m━━━━━━━━━━━━━━━━━━━━┓
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙉𝘼𝙈𝙀\33[38;5;196m        : [★]𝗚𝗫 𝗡𝗜𝗛𝗔𝗡\33[38;5;196m         ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\33[38;5;196m    : [★]𝗧𝗢𝗠 𝗖𝗪\33[38;5;196m         ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙂𝙄𝙏𝙃𝙐𝘽\33[38;5;196m      : [★]𝗚𝗫 𝗡𝗜𝗛𝗔𝗡\33[38;5;196m       ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\33[38;5;196m  : [★]𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\33[38;5;196m        ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋\33[38;5;196m    : [★]+880198100555\33[38;5;196m     ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\33[38;5;196m  : [★]𝗥𝟰𝗡𝗗𝗢𝗠-𝗖𝗟𝗢𝗡𝗜𝗡𝗚\33[38;5;196m     ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙎𝙏𝘼𝙏𝙐𝙎\33[38;5;196m: [★]𝗣𝗥𝗘𝗠𝗜𝗨𝗠-𝗩𝟲\33[38;5;196m         ┃
 \33[38;5;196m    ┗━━━━━━━━━━━━━━━━━━━\033[1;31m𝙁𝙄𝙍𝙀\33[38;5;196m-------------------------{B}""")
 #---------linex def---------#
 	print(f'{warna}-------------------------{B}')
#---------clear def---------#
def clear():
	clr('clear')
	print(logo)
#---------main def---------#
def DX_RONI():
	clear()
	print(f'{B} [{warna}01{B}] RANDOM CLONING')
	print(f'{B} [{warna}00{B}] EXIT TERMINAL')
	option=input(f' {B}[{warna}??{B}] CHOICE MENU >>')
	if option in ['01','1']:
		BD_CLONING()
	else:
		exit('thanks for video using dear :)')
#---------bd clone def---------#
def BD_CLONING():
	print ('NEXT PART ABD CLONING FUNCTION/DEF NIYA KAJ KORBO :)')
	exit()
#---------end---------#
DX_RONI()