#!/usr/bin/env python

import sys
import paramiko
from Queue import Queue

def query(target):
	username, hostname = target.split('@')
	port = 22
	if hostname.find(':') >= 0:
		hostname, portstr = hostname.split(':')
		port = int(portstr)

	try:
	    client = paramiko.SSHClient()
	    client.load_system_host_keys()
	    client.set_missing_host_key_policy(paramiko.WarningPolicy)
	    client.connect(hostname, port, username)
	    stdin, stdout, stderr = client.exec_command('uptime')
	    for line in stdout:
	    	print line.strip('\n')
	    client.close()

	except Exception, e:
	    print 'Caught exception: %s: %s' % (e.__class__, e)
	    traceback.print_exc()
	    try:
	        client.close()
	    except:
	        pass
	    sys.exit(1)

def main():
	# Destination nodes to be queried
	node_list = Queue()
	with open(sys.argv[1], 'r') as f:
		for line in f:
			node_list.put(line.strip())

	# Collection of query responses to be consumed by write thread
	# log_entries = Queue()

	while node_list.empty() is False:
		query(node_list.get())

	print "Done!"



if __name__ == '__main__':
	main()