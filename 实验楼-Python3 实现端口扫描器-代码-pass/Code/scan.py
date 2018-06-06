import socket
import getopt
import sys

def main(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.1)
	
	if type(port) == list:
		for p in range(int(port[0]), int(port[1]) + 1):
			status = s.connect_ex((host,int(p)))
			if status != 0:
				print('{} closed'.format(p))
			else:
				print('{} open'.format(p))
	else:
		 status = s.connect_ex((host,int(port)))
		 if status != 0:
		 	print('{} closed'.format(port))
		 else:
		 	print('{} open'.format(port))

	s.close()

def parse_arg(arg):
	try:
		options, args =  getopt.getopt(arg,'h:p:',['host=','port='])
	except getopt.GetoptError:
		print('Parameter Error')
		exit()

	for name, value in options:
		if name == '--host':
			host = value
		if name == '--port':
			port = value

	if '-' in port:
		port = port.split('-')

	if '.' not in host:
		print('Parameter Error')
		exit()
	elif host.count('.') != 3:
		print('Parameter Error')
		exit()

	return host, port

if __name__ == '__main__':
	host,port = parse_arg(sys.argv[1:])
	main(host, port)
