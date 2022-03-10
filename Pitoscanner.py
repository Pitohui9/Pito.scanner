import socket as s

ip = str(input('Ip de la cible : '))
port = int(input('Le protocol de la cible :'))


sock = s.socket(s.AF_INET,s.SOCK_STREAM)
print('Scann de la cible...')
if sock.connect_ex((ip,port)):
    print('[+] Le port est fermer ou anti scann il faudra trouver une autre strategie')
    exit(1)

else:
    print('{+} Port'+str(port)+' est ouvert ca a marcher !')
    print('Regardons si il ya des cameras connecter decu !')
    exit(0)




