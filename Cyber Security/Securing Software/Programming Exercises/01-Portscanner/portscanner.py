#!/usr/bin/env python3
import sys
import socket
	 
	 
def get_accessible_ports(address, min_port, max_port):
    found_ports = []
	 
	# Iterating through the ports
	for port in range(min_port, max_port + 1):
	    s = socket.socket() # Create a new socket
        s.settimeout(1) # Set a timeout
		
        try:
	        s.connect((address, port))
			# If connection is possible, port is added to the list
	        found_ports.append(port)
	    except (socket.timeout, ConnectionRefusedError):
			# Port is not accessible so it gets passed
	        pass
	 
	    s.close() # Close the socket
	 
	return found_ports
	 
	 
def main(argv):
	address = sys.argv[1]
	min_port = int(sys.argv[2])
	max_port = int(sys.argv[3])
	ports = get_accessible_ports(address, min_port, max_port)
	if ports:
		for p in ports:
			print(p)
	else:
		print("No accessible ports found!")
	 
# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 4:
		print('usage: python %s address min_port max_port' % sys.argv[0])
	else:
		main(sys.argv)

